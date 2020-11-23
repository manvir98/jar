
#J.A.R.V.I.S = Just A Rather Very Intelligent System 

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser 
import os
import smtplib
from selenium import webdriver
import random
import wolframalpha #make your id on wolframalpha to get the API
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
client = wolframalpha.Client('23X9QV-4YQ65HYJ8T')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    (engine.say(audio))
    (engine.runAndWait())




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!") 

def hello():
    wishMe()
    print("I am JARVIS. Please tell me how may I help you")
    speak("I am JARVIS. Please tell me how may I help you")


           

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manvir9824@gmail.com', 'Manvir@98')
    server.sendmail('manvir9824@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    hello()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wish me' in query:
            wishMe()

        elif 'project' in query:
            print("Jarvis said: This project is made by Guneet Kaur from CSE 2 Third year student. Her roll number 02813202717.")
            speak("This project is made by Guneet Kaur from CSE 2 Third year student. Her roll number 02813202717.")
     
        elif 'open youtube' in query:
            print("Jarvis said: Opening youtube")
            speak("Opening youtube")
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.youtube.com//")
            
        elif 'how are you' in query:
            print(query)
            speak("I am good.")

        elif 'open google' in query:
            print("Jarvis said: Opening Google")
            speak("Opening google")
        
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.com//")
         
       
        elif 'open facebook' in query:
            print("Jarvis said: Opening Facebook")
            speak("Opening facebook")
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.facebook.com//")

        elif 'open gmail' in query:
            print("Jarvis said: Opening Gmail")
            speak("Opening gmail")
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.gmail.com//")
      
        
        elif 'Hy' in query or 'Hello' in query or 'hi' in query:
            stMsgs = ['Hello', 'Hy']
            speak(random.choice(stMsgs))
        
        
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "Do you love me" in query or 'talk to me for some time' in query or 'talk to me' in query:
            stMsgs = ['Well I am not free as you. So, get lost']
            speak(stMsgs)

        elif 'play music' in query:
            print("Jarvis said: Jarvis playing the music for you")
            speak("Jarvis playing the music for you")
            music_dir = 'C://Users//hp//Desktop//New folder (6)//'
            songs = os.listdir(music_dir)
            l=len(songs)
            print(l)
            print(songs)
            #for i in range(l):    
            os.startfile(os.path.join(music_dir, songs[0]))
            takeCommand()

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print("Javis said: The time is"+ strTime)   
            speak(f"The time is {strTime}")
        
        elif 'sleep mode' in query:
            print("Jarvis said: okay jarvis is sleeping the system ")
            speak("okay jarvis is sleeping the system")
            #speekmodule.speek(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        
        elif 'thanks' in query or ('thank you') in query:
            stMsgs=['You are welcome', 'no problem']

            speak(random.choice(stMsgs))   
        
        elif 'shut down' in query:
            print("Jarvis: Okay Jarvis is shutting down the system")
            speak("okay Jarvis is shutting down the system")
            os.system('shutdown -s -t 6')
        
        elif ('google maps') in query:
            speak("Jarvis said: Which place you are searching")
            message= takeCommand()
            print("Jarvis said: Opening"+ message +"on google maps")
            speak("Opening"+message+"on google maps")
            stopwords = ['delhi', 'google', 'maps']
            querywords = message.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            #result = ' '.join(resultwords)
            result=stopwords[0]
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+message+"/")
            takeCommand()
            rand = [result+'on google maps']
        
        elif 'close gmail tab in chrome window' in query:
            print("Jarvis said: Closing gmail tab")
            speak("Closing gmail tab")

        elif 'minimize the chrome window' in query:
            print("Jarvis said: Minimizing Chrome Window")
            speak("Minimizing Chrome Window")

        elif 'open notepad' in query:
            print("Jarvis said: Opening notepad")
            speak("opening notepad ")
            osCommandString = "notepad.exe file.txt"
            os.system(osCommandString)
            

        elif ('.com') in query :
            print("Jarvis said: Opening" + query)
            speak("Opening" + query)         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open('http://www.'+query)

        elif 'email send' in query:
            try:
                print("Jarvis said: What should be the message of the email")
                speak("What should be the message of the email")
                content = takeCommand()
                print("Jarvis said: Can you please tell me email id to whom you want the mail.")
                speak("Can you please tell me email id to whom you want the mail.")
                receiver= takeCommand()
                to = receiver    
                sendEmail(to, content)
                print("Jarvis said: Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Jarvis said: Sorry my friend. I am not able to send this email due to some technical issues")
                speak("Sorry my friend. I am not able to send this email due to some technical issues")    

        elif 'pause music' in query:
            print("Jarvis said: Music Player Paused")
            speak("Music Player paused")
            

        elif 'stop music' in query:
            print("Jarvis said: Music Player Stop")
            speak("Music Player Stop")
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + 'wmplayer' + '.exe /f')

        elif 'open chrome' in query:
            print("Jarvis said: Opening Google Chrome")
            speak("Opening Google Chrome")
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.com//")
            
            

        elif 'I want to search' in query:
            print("Jarvis said: I am opening google chrome for you here u can search anything")
            speak("I am opening google chrome for you here u can search anything")
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.com//")  
        
        elif 'close chrome' in query:
            print("Jarvis said: Closing All Chrome tabs and Windows")
            speak("Closing chrome windows") 
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + 'chrome' + '.exe /f')  
        
        elif 'bye jarvis' in query:
            print("Jarvis said: Okay bye, Thanks for using me. Have a nice day!")
            speak("Okay bye, Thanks for using me. Have a nice day!")
            exit()
        
        elif 'jarvis stop' in query:
            print("Jarvis said: Okay bye, Have a nice day!")
            speak("Okay bye, Have a nice day!")
            exit()


        elif 'none' in query:
            speak("")

        elif 'what is my location' in query or 'where am I' in query or 'my location' in query:
            w = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1275004&appid=5fc29900336d19d1d912723dc3d1e117')
            json_object = w.json()
            loc_lon = (float(json_object['coord']['lon']))
            rand1 = str(loc_lon)
            loc_lat = (float(json_object['coord']['lat']))
            rand2 = str(loc_lat)
            print("Jarvis said: The current position is "+rand1+" longitude and "+rand2+" latitude")
            speak("The current position is "+rand1+" longitude and "+rand2+" latitude")

        else:
            print(query)
            query = query
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('Got it.')
                print(results)
                speak(results)

            except:
                    pass
      