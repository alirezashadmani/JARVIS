import pyttsx3                                  #pip install pyttsx3
import datetime
import speech_recognition as sr     #pip install speechRecognition
import wikipedia                              #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import  pyautogui
import random
import wolframalpha
import json
import requests
from urlib.request import urlopen
import time

engine = pyttsx3.init()
wolframalpha_app_id = 'wolfram alpha id will go here'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)
    


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Ali!")
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    if hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Jarvis at your service. Please tell me how can I help you today")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-US')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #for this function, you must enable low security in your email which you are going to use as sender

    server.login('username@gmail.com', 'password')
    server.sendmail('username@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/MAK/Desktop/screenshot.png')
    
def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at '+usage)

    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)
    
def jokes():
    speak(pyjokes.get_jokes())
    



if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()

        #All command will be stored in lower case in query
        #for easy recognition

        if 'time' in query:
            time_()

        if 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace('wikipedia', '')
            result=wikipedia.summary(query, sentence=3)
            speak('Accrding to wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak('What should I say?')
                content=TakeCommand()
                #provide recieved email address

                speak('Who is the Reciever?')
                reciever=input('Enter Recievers Email: ')
                to=reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak('Unable to send Email.')


        elif 'search in chrome' in query:
            speak('What should I search?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')  #only open websites with '.com' at end.


        elif 'search youtube' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Here we go to YOUTUBE')
            wb.open('https://www.youtube.com/result?search_query='+search_Term)

        elif 'search google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Searching....')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cppu' in query:
            cpu()

        elif 'jokes' in query:
            joke()

        elif 'go offline' in query:
            speak('Going Offline Sir!')
            quit()


        elif 'word' in query:
            speak('Opening MS Word')
            ms_word = r'C:/Office/Office19/WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak('What should I write, Sir?')
            note = TakeCommand()
            file = open('notes.txt', 'w')
            speak('Sir should I include Date ad Time?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, Sir!')
            else:
                file.write(notes)

        elif 'show notes' in query:
            speak('showing notes')
            file  = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()
        
    elif 'play music' in query:
        songs_dir = 'D:/Music'
        music = os.listdir(songs_dir)
        speak('What should I play?')
        speak('select a number...')
        ans = TakeCommand().lower()
        if 'number' in ans:
            no = int(ans.replace('number', ''))
        elif 'random' or 'you choose' in ans:
            no = random.randint(1,100)
        
        os.strartfile(os.path.join(songs_dir, music[no]))
        
    if 'play songs' in query:
        video ='D:/Music/Videosclips'
        audio = 'D:/Music'
        speak("What songs should i play? Audio or Video")
        ans = (TakeCommand().lower())
        while(ans != 'audio' and ans != 'video'):
            speak("I could not understand you. Please Try again.")
            ans = (TakeCommand().lower())
        if 'audio' in ans:
            songs_dir = audio
            songs = os.listdir(songs_dir)
            print(songs)
        elif 'video' in ans:
            songs_dir = video
            songs = os.listdir(songs_dir)
            print(songs)
        speak("select a random number")
        rand = (TakeCommand().lower())
        while('number' not in rand and rand != 'random'):
            speak("I could not understand you. Please Try again.")
            rand = (TakeCommand().lower())
            if 'number' in rand:
                rand = int(rand.replace("number ",""))
                os.startfile(os.path.join(songs_dir,songs[rand]))
                continue            
            elif 'random' in rand:
                rand = random.randint(1,219)
                os.startfile(os.path.join(songs_dir,songs[rand]))
                continue
    elif 'calculate' in query:
        client = wolframalpha.Client(wolframalpha_app_id)
        index = query.lower().split().index('calculate')
        query = query .split()[index + 1:]
        res = clientquery(''.join(query))
        answer = next(res.results).text
        print('The Answer is :' + answer)
        speak('The Answer is :' + answer)
        
    elif 'what is' in query or 'who is' in query:
        # use the same API key that we generated earlier i.e. wolframalpha
        client = wolframalpha.Client(wolframalpha_app_id)
        res = client.query(query)
        
        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print('No Results')
            
    elif 'remember that' in query:
        speak('What should I remember?')
        memory = TakeCommand()
        speak('You asked me to remember that' + memory)
        remember = open('memory.txt', 'w')
        remember.write(memory)
        remember.close()
        
    elif 'do you remember anything' in query:
        remember = open('memory.txt', 'r')
        speak('You asked me to remember that' + remember.read())
        
    elif 'where is' in query:
        query = query.replace('where is', '')
        location = query
        speak('User asked to locate' + location)
        wb.open_new_tab('http://www.google.com/maps/place/' + location)
        
    elif 'news' in query:
        try:
            jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d5664f46c0084d468854ae04e87fc80b')
            data = json.load(jsonObj)
            i = 1
            
            speak('Here are some top headlines from the Business Industry')
            print('=============TOP HEADLINES=============', '\n')
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n']
                speak(item['title'])
                i += 1
        except Exception as e:
            print(str(e))
            
    elif 'stop listening' in query:
        speak('For How many second you want me to stop listening to your commands?')
        ans = int(TakeCommand())
        time.sleep(ans)
        print(ans)
    
    elif 'log out' in query:
        os.system('shutdown -1')
    elif 'restart' in query:
        os.system('shutdown /r /t 1')
    elif 'shutdown' in query:
        os.system('shutdown /s /t 1')
        
        
        
        
        
# In the last session, you should install pyinstaller to convert .py to .exe
# After installing and converting, we will get 3 file which contain 'dist', 'build', 'file_name.spec'

