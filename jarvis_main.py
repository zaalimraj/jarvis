import datetime
import pyttsx3
import speech_recognition
import requests
from bs4  import BeautifulSoup
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said:{query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
if __name__ =="__main__":
    while True:
        query =takeCommand().lower()
        if "Hello Rahul" in query: 
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("OK sir , You can call me anytime")
                    break
                
                elif "hello" in query:
                    speak("Hello sir, How are you sir?")
                    
                    
                elif "i am fine" in query:
                    speak("Good to hear that, sir")
                    
                    
                elif "how are you" in query:
                    speak("I am fine, sir")
                    
                    
                elif "thanks jarvis" in query:
                    speak("You are welcome, sir")
                    
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    
                    
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                    
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                    
                    
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                    
                elif "temperature in jaipur" in query:
                    search = "temperature in jaipur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe iBp4i AP7Wnd").text
                    speak(f"current{search}is{temp}")
                    
                    
                elif "set an Alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done, Sir")

                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                    
                elif "finally sleep" in query:
                    speak("Going to sleep, Sir")
                    exit()
                      
                
                     