import os
import openai


class Chatbot:
    def __init__(self):
        # please replace with your api key
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # define the role to the chatbot
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

    def get_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            max_tokens=550,
            temperature=0.3
        )

        # workflow of the chatbot
        assistant_message = response['choices'][0]['message']['content']

        # Replace undesired replies with a custom message
        if "as an AI model I can't" in assistant_message:
            assistant_message = "Sorry, I can't assist you with that request."

        self.messages.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    def reset_messages(self):
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

if __name__ == "__main__":
    bot = Chatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")







