import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
from bhavi import key


today = date.today()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning sir")
    elif hour>=12 and hour < 18:
        speak("good Afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am Jarvis. please tell me how may i help you")

def takecommand():
    '''
    it takes microphone input and returns string outpur'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("say that again please....")
        return "None"
    
    return query

def sendEmail(to, content):
    pass


if __name__ =="__main__":
    WishMe()
    while True:
        query = takecommand().lower()

    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia......')
            # query = query.replace("wikipedia", "")
            query = takecommand()
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'spotify' in query:
            webbrowser.open("spotify.com")

        elif 'kaise' in query:
            webbrowser.open("youtube.com/watch?v=WWXm39leYew")

        elif 'saiyaara' in query:
            webbrowser.open("youtube.com/watch?v=BSJa1UytM8w")

        elif 'jo tum' in query:
            webbrowser.open("youtube.com/watch?v=ilNt2bikxDI")

        elif 'husn' in query:
            webbrowser.open("youtube.com/watch?v=gJLVTKhTnog")

        elif 'tujhe kitna ' in query:
            webbrowser.open("youtube.com/watch?v=92J9p0VplTo")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'bekhayali' in query:
            webbrowser.open("youtube.com/watch?v=VOLKJJvfAbg")

        elif 'date' in query:
            speak(f"Today's date is{today}")

        elif 'stack overflow' in query:
            webbrowser.open("stack overflow.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\bhavi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'pycharm' in query:
            cPath = "C:\\Users\\bhavi\\Downloads\\pycharm-professional-2024.3.5.exe"
            os.startfile(cPath)

        elif 'music' in query:
            codePath = "C:\\Users\\bhavi\\Downloads\\song.mp3"
            os.startfile(codePath)

        


        elif ('search' and 'youtube') in query:
            speak("what i have to search")
            search = takecommand()
            words = search.split(" ")
            result = "+".join(words)
            url = f" youtube.com/results?search_query={result}"
            webbrowser.open(url)

        elif 'email' in query:
                pass
                   

        elif 'quit' in query:
            exit()