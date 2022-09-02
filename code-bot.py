# importing speech recognition package from google api
import speech_recognition as sr
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import sys
import webbrowser
import time
import subprocess
import json
import smtplib
import ssl
# here we define the opening path for the webbrowser module.
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# This is where we setup voice recognition
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# here it we create a custom 'speak' code
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
num = 1


#It takes microphone input from the user and returns string output
def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query
def wishMe1():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!")

    else:
        speak("Good Evening!") 
        print("Good Evening!") 
    
    speak ("I am C0D3X")

def search_web():
    query= takeCommand1().lower()
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in query():

        speak("Opening in youtube")
        indx = query().split().index('youtube')
        query1 = query.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
    elif 'wikipedia' in query():

        speak("Opening Wikipedia")
        indx = query().split().index('wikipedia')
        query1 = query.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
    elif 'google' in input or 'search' in input:

        indx = query().split().index('google')
        query1 = query.split()[indx + 1:]
        driver.get("https://www.google.com/search?q =" + '+'.join(query))

    else:

        driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
        


# function used to open application
# present inside the system.
def open_application():
	if " open chrome" in input:
		speak("Google Chrome")
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
	elif "open firefox" in input or "mozilla" in input:
		speak("Opening Mozilla Firefox")
		os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
	elif "open word" in input:
		speak("Opening Microsoft Word")
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')

	elif "open excel" in input:
		speak("Opening Microsoft Excel")
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')

	else:
		speak("Application not available")
	
def Study1():
    while True:
        query = takeCommand1().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)
        elif 'quit' in query:
            speak("okay. quitting. thank you for using me. this is Edubot signing off.")
            print("okay. quitting. thank you for using me. this is Edubot signing off.")
            os._exit(0)
        elif 'search' in query or 'play' in query:
            search_web()
        elif "who are you" in query or "define yourself" in query:
            speak1 = '''Hello, I am C0D3X. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etc'''

            speak(speak1)
        elif "who made you" in input or "created you" in input:
            speak2 = "I have been created by Shouvik Maiti and Parth Agrawal."
            speak(speak2)
        elif "calculate" in query.lower():
            app_id = ["WOLFRAMALPHA_APP_ID"]
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query1 = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak(f"The answer is {answer}")
        elif 'open' in input:
            open_application(query.lower())
        else:
            print("okay. quitting. thank you for using me. this is C0D3X signing off.")
            speak("okay. quitting. thank you for using me. this is C0D3X signing off.")
            os._exit(0)

# Driver Code
if __name__ == "__main__":
    wishMe1()
    Study1()
