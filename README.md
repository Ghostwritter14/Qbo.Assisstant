
## Qbo Assisstant 
This project forms a part of my MSc. dissertation at University of Kent (Topic: EMPATHETIC SOCIALLY ASSISTIVE ROBOTS). 

The aim of this software is to test levels of human robot interraction that Qbo.One robot can achieve utilising modern trends in technology.




## Acknowledgements

I want to acknowledge all the people from whoom I got the idea of how an AI assisstant looks like and how to build one. I am also gratefull to the people that helped me throughout the journey to build the base program and help with debugging of it.  

 - Dr Giovanni Luca Masala - Senior Lecturer in Computer Science, University of Kent.
 - Dr. Ioanna Giorgi - Lecturer in Artificial Intelligence, University of Kent.
 - https://github.com/Mikael-Codes. Youtube - Mikael Codes.
 - https://github.com/NeuralNine. Youtube - NeuralNine.
 - https://github.com/Pythoholic. Youtube - Pythoholic.
 - https://github.com/murtazahassan. Youtube - Murtaza's Workshop - Robotics and AI.
 

## Use Case

Robotics is playing a greater and greater role for abstracting in places where humans might fall short. Likewise my project is aimed towards the medical sector in the field of elderly care. 

Though nothing can replace the crucial role played by caregivers, yet as humans even they are not able to be present all the time. This program aims to abstract when a caregiver is not available to give company to their client. It aims at boosting the mental well being of an elderly person and well as a medium of entertainment in times there is no one to give them comapny.    

## Features

- Full voice functionality - the program is totally controlled with voice commands and doesn't require the user to type anything.
- Facial Recognition- to make the interaction between the user and the robot more personal the assistant uses facial recognition to address its user with their name at the begining of the program.
- FAQs - the program is able to answer common questions for e.g. date, time, or day.
- Take notes - The assisstant is capable of taking notes for the user. It is currently able to store them in a .txt file and can also read out the notes that a user may have jotted down.
- Question mode- The assisstant is able to answer any question based on general knowledge and current events as far as 2021 when question mode is prompted. It uses the GPT3.5 framework to achieve such. 
- News mode - The assisstant can display the latest news (top 10) within the United Kingdom. In the news mode the titles of the articles will be displayed in the screen. clicking on any article opens up a browser window redirecting the user to the news article in question.
- Exit - The program exits through voice command of the user stating the assisstant to shut-down/exit/close. 



## Prerequisites

To run this program you would need atleast python 3.10 or higher as well as C++ visual studio build tool.
## Installation
- Clone the repository. 
- Setup Virtual environment (not necessary but reccomended).

- Install the dependencies. run this command in the terminal:
    
     `pip install -r requirements.txt` 


## Environment Variables

To run this project, there is an additional need to setup an environment variable within the operating system. This is mainly for the openai api key as OpenAI does't allow sharing of api key in a public environment. 

`API_KEY is provided within my dissertation pdf document`




## Walkthrough

To run this program you need to run main.py.

If there are no pictures in the program directory, prior to running main.py a couple things need to be done if you would want the robot to address you via your name. you need to take a couple of pictures of youreself or the person who would be using the assisstant preferably with the camera on the device the program will run on. 

First a directory has to be made within the program directory named Ref_pics or you have to change the code in face_trainer.py line 7 to the name the directory has been named. within the main directory a subdirectory has to created in the name of the person for whoom pictures were inserted. the structure is like. 
    
    ---- RootDir -> Dir named after person -> pic1, pic2, pic3

After doing this crucial step run face_trainer.py file to generate the trained data using pickle. 

after the pickle files have been generated. Please run the main.py file which will start the assisstant. 

The user can ask several things to the assisstant. For instance ask 'what is your name' or 'can you tell me the time' and likewise. These are all FAQ questions which will be answered by the assisstant.

The user can ask Qbo to take notes by asking it to take a note. for instance ask "Create a note for me"/"Create a note"/"Can you make a note". Qbo will start taking down notes. 

The user can ask qbo to read out the notes by stating it to read notes. for e.g. "read my notes", "read note",
                "read my note", "tell me my notes"

The user can go into question mode for questions like who won the football worldcup in 2012 and alike questions. to enter into question mode the user has to make a certain prompt that he/she have a question. for e.g. "I have a question", "Can I ask a question". 

The user can ask for the news of the day like asking qbo to show the news. for e.g. "get me the news",
                    "tell me the news",
                    "what's the news". This will open a new window with the article titles displayed for the top 10 trending news of the moment. Clicking an article redirects to the default webbrowser where the news article will be opened for the user to read. 

To exit the program the user can tell Qbo to shut down. for e.g. "exit","close","shut down". 



 


## Tech Stack

List of Technologies used are:
  
   - OpenCV
   - dlib
   - face_recognition
   - gtts
   - pygame
   - tkinter
   - openai
   - pickle
   - Json
   - requests
   - speech_recognition
   - mediastack
   - numpy
   - 
   
## Roadmap

The program is in an alpha stage and is still under developement. But here are some features planned for the comming days going ahead. 

- Building a more robust note taking system via integrating MongoDB. Notes will be stored for upto 7 days after which the oldest note will be deleted on the next run. 
- Personalisation of news. Though the assisstant displays news, there are plans to upgrade it where it can display news based on preferance of the user.



## Contribution

I would very much appreciate anyone who wants to contribute to this project in form of code, bug-fixes, bug- detection. 

But as protocol goes since it is a part of my dissertation, contributions cannot be accepted for the time-being. This section will be updated after the formal procedures of marking have been completed. 