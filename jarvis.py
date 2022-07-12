from random import random
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess as sp
import requests

jarvis = pyttsx3.init('sapi5')
voices = jarvis.getProperty('voices')

jarvis.setProperty('voice', voices[1].id)


def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()#speech willbe audible to us.


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your computer assistent Sir. Please tell me how may I help you ?")       
 #It takes microphone input from the user and returns string output
def takeCommand():
    

    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

    try:
        print("Recognizing...")    
        query = rec.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("sir!Please Say that again.")  
        return "None"#None string will be returned
    return query

#Open camera
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
#open calculator
def open_calculator():
    sp.Popen(paths['calculator'])
#Open cmd
def open_cmd():
    os.system('start cmd')

#Tell usjokes
def get_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() # It will convert the user speech to lower case
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results) #It will speak about the topic 
        if 'play music' in query or 'play a song' in query:
             music_dir = "D:\\Music\\favoritesng"
             songs = os.listdir(music_dir)   
             os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))

        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'joke' in query:
            
            joke = get_joke()
            speak(joke)
            speak(f"Hope you like this one sir")
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)
        elif 'how are you' in query:
            speak('I am Fine, How are you.')
            ans = takeCommand().lower()
            if 'fine' in ans:
                speak('Glad to here it')
            elif 'not' in ans:
                speak('feel sorry to hear it')
        
        

        elif 'write a note' in query:
            speak('What should I write, Sir!')
            notes = takeCommand()
            file = open('notes.txt','w')
            speak('Sir should I include Date and Time also?')
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, Sir!')
            else:
                file.write(notes)

            

        elif 'show notes' in query:
            speak('Showing Notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())
            
     
        elif 'close' in query:
            speak("Terminating the process")
            quit()  
               
    
       
            
   