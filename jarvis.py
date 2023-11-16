
import speech_recognition as sr
import smtplib
import os
import webbrowser
import wikipedia
import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good night sir")

    speak("i am jarvis , how can i help you ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing....")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en - in')
        print(f"user said : {query }\n")
        return query

    except Exception as e:
        print("say that again please ......")
        return "None"


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=5)
            speak('acroding to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('https://stackoverflow.com')

        elif 'open video on youtube' in query:
            webbrowser.open('https://www.youtube.com/watch?v=B7SkAq_94J8')

        elif 'open spotify' in query:
            webbrowser.open(
                'https://open.spotify.com/playlist/28pb6YKdLEvL6Q8Foo7sK4')

        elif 'what is the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strtime}")

        elif 'open vlc media player' in query:
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(path)

        elif 'open vs code' in query:
            codepath = "C:\\Users\\praja\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
