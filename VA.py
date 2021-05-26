import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 5 and hour<12:
        speak("Good Morning Pritam!")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Pritam!")
    elif hour>= 18 and hour<21:
        speak("Good Evening Pritam!!")
    else:
        speak("Good Night Pritam!")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print("User said: {query}\n")
    except:
        #print(e)
        print("Please say again...")
        return "none"
    return query
    
if __name__ == "__main__":
    
    wishme()
    speak(" Yo Yo Heisenberg is here! How may i help you bro")

    while True:
        query = takecommand(). lower()
        if "wikipedia" in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", ' ')
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open('youtube.com')
        elif "open google" in query:
            webbrowser.open('google.com')
        elif "open facebook" in query:
            webbrowser.open('facebook.com')
        elif "open hackerearth" in query:
            webbrowser.open('hackearth.com')
        elif "open game" in query:
            codepath="C:\\Games\\FIFA 19\\FIFA19.exe"
            os.startfile(codepath)
        elif "How are you bro" in query:
            speak("I'm good and u")   
        elif "ok bro" in query:
            speak("See you soon bro")
            break



            
