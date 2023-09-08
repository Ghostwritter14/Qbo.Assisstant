import json
import os
import threading
import tkinter as tk
import speech_recognition as sr
from datetime import datetime, timedelta
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor
import pygame
import time
import cv2


from news_scraper import NewsScraper
from Chatbot import Chatbot
from face_recognizer import FaceRecognizer

pygame.mixer.init()
executor = ThreadPoolExecutor(max_workers=1)
stop_event = threading.Event()


class Assistant:

    # Constructor for the Assistant
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.note_mode = False
        self.chat_mode = False
        self.assistant_methods = {
            "greeting": self.greet,
            "name": self.get_name,
            "note": self.create_note,
            "date": self.get_date,
            "time": self.get_time,
            "news": self.get_news,
            "question": self.ask_chatbot,

            "reset": self.reset_chatbot,
            "read": self.read_notes,
            "exit": self.exit_program
        }
        self.intents = json.load(open('intents.json'))
        self.root = tk.Tk()
        self.face_recognizer = FaceRecognizer()

        self.news_scraper = NewsScraper(self.root)
        self.chatbot = Chatbot()

        self.label = tk.Label(text='🤖', font=("Arial", 150, "bold"))
        self.label.pack()

        threading.Thread(target=self.run_assistant).start()

        self.delete_yesterdays_notes()
        greetings = self.greet()
        self.speak(greetings)
        self.root.mainloop()

    def remove_file(self, filename):
        # function for cleaning previous audio files on each new run of the program or if the assistant
        # is issued with another same prompt giving the same result
        if os.path.exists(filename):
            pygame.mixer.music.unload()
            os.remove(filename)

    def speak(self, text):
        filename = f"response_{datetime.now().strftime('%Y%m%d-%H%M%S')}.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():  # wait for audio to finish playing
            pygame.time.Clock().tick(10)

        self.remove_file(filename)

    def greet(self):
        # Start the webcam for live face recognition
        video_capture = cv2.VideoCapture(0)

        # Check if webcam opens successfully
        if not video_capture.isOpened():
            return "Hello! I couldn't access the camera."

        # Capture the frame
        ret, frame = video_capture.read()

        video_capture.release()

        if not ret:
            return "Hello! I couldn't capture an image."

        # Identify the face in the captured frame
        person_name = self.face_recognizer.identify_face(frame)

        if person_name != "Unknown":
            return f"Hello, {person_name}! How can I assist you today?"
        else:
            return "Hello! How can I assist you today?"

    def get_name(self):
        return "My name is Qbo. I am a robot manufactured by The corpora. I am your personal assistant."

    def create_note(self, text=None):
        if text is None:
            self.note_mode = True
            return "Okay, I'm ready. Please say your note."
        else:
            filename = datetime.today().strftime('%Y-%m-%d') + ".txt"
            with open(filename, 'a') as f:
                f.write(text + "\n")
            return "Note added: " + text

    def get_date(self):
        return f"Today's date is {datetime.today().strftime('%Y-%m-%d')}."

    def get_time(self):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    def get_news(self):
        self.news_scraper.show_news()
        return "Here are the latest news."

    def ask_chatbot(self, text):
        # function to access gpt framework activated by prompt question
        #self.speak("Please ask")
        print("Chatbot activated")
        response = self.chatbot.get_response(text)
        print(response)
        #self.speak(response)  # The assistant will speak the response
        return response

    def reset_chatbot(self):
        # resets the chatbot after giving the response to an input
        self.chatbot.reset_messages()
        return "Chatbot reset. You can start a new conversation now."

    def read_notes(self):
        # reads the notes saved in a txt file created with create note function
        filename = datetime.today().strftime('%Y-%m-%d') + ".txt"
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "No notes for today."

    def exit_program(self):
        stop_event.set()
        self.root.quit()
        return "Goodbye!"

    def delete_yesterdays_notes(self):
        # Delete notes from yesterday
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d') # 7 days
        filename = yesterday + ".txt"
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass      # No file exists, do nothing

    def request(self, text):
        # function where the assistant 
        if self.note_mode:
            note_text = self.create_note(text)
            self.note_mode = False
            return f"Note added: {note_text}"
        elif self.chat_mode:
            if "exit chat" in text.lower() or "end conversation" in text.lower():
                self.chat_mode = False
                print('chatbot deactivated')
                return "Chat mode exited. How can I assist you further?"
            else:
                return self.assistant_methods["question"](text)

        else:
            # question mode to activate gpt model
            if "i have a question" in text.lower():
                self.chat_mode = True
                question = text.lower().replace("i have a question", "").strip()
                return self.assistant_methods["question"](question)
            else:
                for intent in self.intents['intents']:
                    for pattern in intent['patterns']:
                        if pattern.lower() in text.lower():
                            return self.assistant_methods[intent['tag']]()
                #return "Sorry, I don't understand."




    def run_assistant(self):
        while not stop_event.is_set():
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.3)
                    audio = self.recognizer.listen(mic)


                    text = self.executor.submit(self.recognizer.recognize_google, audio).result()
                    text = text.lower()
                    print(text)

                    response = self.request(text)
                    if response:
                        self.speak(response)
            except sr.UnknownValueError:
                self.speak("I'm sorry, I didn't catch that. Could you please repeat?")
            except sr.RequestError:
                self.speak("I'm sorry, I'm having trouble understanding you right now. Let's try again.")
            except KeyboardInterrupt:
                stop_event.set()
            except Exception as e:
                print("Error:", e)
                # Reinitialise executor after error
                self.executor = ThreadPoolExecutor(max_workers=1)
            time.sleep(3)


if __name__ == "__main__":
    Assistant()
