import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser 
import pywhatkit as wk 
import random
import os
import pyautogui
import cv2 
import time
import requests
import sys
import pyjokes
import subprocess
import psutil
import winshell
import imdb 
from GoogleNews import GoogleNews 
import pandas as pd 
from random import randint
import smtplib
from twilio.rest import Client

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am your personal assistant. What can I do for you ?")  

def news():
    news=GoogleNews (period='id')
    news.search("India")
    result=news.result()
    data=pd.DataFrame.from_dict(result)
    data=data.drop(columns=["img"])
    data.head()
    for i in result:
        print(i["title"] )
        speak(i["title"])  

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query             

def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery=str(psutil.sensors_battery())
    speak("CPU is at"+battery)

def send_email(to, content):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("palwaidheerajreddy@gmail.com", "vjfn nvfx fetj svkt")
    server.sendmail("palwaidheerajreddy@gmail.com", to, content)
    server.close()




def movie():
    moviesdb=imdb.IMDb()
    speak("please tell me the movie name sir")
    text=takeCommand()
    movies=moviesdb.search_movie(text)
    speak("searching for " +text)
    if len(movies) ==0:
        speak("No result found")
        print("No result found")
    else:
        print("I found these: ")
        speak("I found these: ")
        for movie in movies:
            title=movie["title"]
            year=movie["year"]
            print(f'{title}-{year}')
            speak(f'{title}-{year}')
            info=movie.getID()
            movie=moviesdb.get_movie(info)
            rating=movie.get("rating", "N/A")
            plot=movie.get("plot outline", "plot outline not available")
            if year<int(datetime.datetime.now().strftime("%Y")):
                print(f'{title} was released in {year} has IMDB ratings of {rating}. The plot summary of movie is {plot}')
                speak(f'{title} was released in {year} has IMDB ratings of {rating}. The plot summary of movie is {plot}')
                break 
            else:
                print(f'{title} will release in {year} has IMDB ratings of {rating}. The plot summary of movie is {plot}')
                speak(f'{title} will release in {year} has IMDB ratings of {rating}. The plot summary of movie is {plot}')
                break 

def rock():
    you=int(input("please enter your choice:- \n 1-Rock \n2-Paper \n3-Scissor"))
    shapes= {1:'rock', 2:'paper', 3:'scissor'}
    if you not in shapes:
        print("please enter a valid number")
        exit()
    comp=random.randint(1,3)
    print("you choose", you)
    print("computer choose", comp)
    if (you==1) and (comp==3) or (you==2) and (comp==1) or (you==3) and (comp==2):
        speak("congratulations you won!")
        print("congratulations you won!")
    elif(you==comp):
        speak("Match tied") 
        print("Match tied")   
    else:
        speak("you loose")
        print("you loose") 


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'jarvis' in query:
            print("yes sir")
            speak("yes sir")

        elif 'how are you' in query:
            speak("I am fine sir,Thankyou.")
            speak("How are you, sir?") 
      
        elif "who are you" in query:
            print('My Name is Jarvis')
            speak('My Name is Jarvis')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')  

        elif "who created you" in query:
            print('I Do not know His Name, I created with python language, in Visual studio code.')
            speak('I Do not know His Name, I created with python language, in Visual studio code.')

        elif 'what is' in query:
            speak('Searching Wikipedia...')
            query=query.replace("what is", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('Searching Wikipedia...')
            query=query.replace("who is", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)  
            speak(results)

        elif 'open chrome' in query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            pyautogui.moveTo(x=1307, y=464, duration=1)
            pyautogui.click(x=1307, y=464, clicks=1, interval=0, button='left')  

        elif 'maximize the window'  in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')

        elif 'google search' in query:
            query=query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')         

        elif 'youtube search' in query:
            query=query.replace("youtube search", "")
           # pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
            
        elif "click on first" in query:
            pyautogui.moveTo(x=703, y=388, duration=1)
            pyautogui.click(x=703, y=388, clicks=1, interval=0, button='left')    
        
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')

        elif 'open new tab' in query:
            pyautogui.hotkey('ctrl', 't')    

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')    

        elif 'minimise the window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('N')

        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')

        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')

        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')

        elif 'next tab' in query:
            pyautogui.hotkey('ctrl','tab')

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')
                                                      
        elif 'just open google' in query:
            webbrowser.open('google.com')

        elif 'open google' in query:
            speak("What should I search ?")
            qry=takeCommand().lower()
            webbrowser.open(f"{qry}")
            results=wikipedia.summary(qry,sentences=1)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak("What would you like to watch?")
            search_query = takeCommand().lower()
            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(search_url)    

        elif 'search on youtube' in query:
            query=query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'close browser' in query:
           os.system("C:\\Windows\\System32\\taskkill /f /im msedge.exe")

        elif 'close chrome' in query:
            os.system("C:\\Windows\\System32\\taskkill /f /im chrome.exe") 

        elif "open paint" in query:
            npath="C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2311.30.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe"
            os.startfile(npath)

        elif "draw a line" in query:
            pyautogui.moveTo(x=400, y=300, duration=1)
            pyautogui.leftClick
            pyautogui.dragRel(400, 0, 1)

        elif "draw a square" in query:
            pyautogui.moveTo(x=1000, y=300, duration=1)
            pyautogui.mouseDown()
            #pyautogui.leftClick
            distance=400
            pyautogui.click();
            pyautogui.dragRel(distance, 0, duration=1)
            pyautogui.dragRel(0, distance, duration=1)  
            pyautogui.dragRel(-distance, 0, duration=1)  
            pyautogui.dragRel(0, -distance, duration=1) 
            pyautogui.mouseUp()  

        elif "red colour" in query:
            pyautogui.moveTo(x=1156, y=122, duration=1)
            pyautogui.click(x=1156, y=122, clicks=1, interval=0, button='left')

        elif "undo" in query:
            pyautogui.hotkey('ctrl', 'z')               

        elif "close paint" in query:
            os.system("C:\\Windows\\System32\\taskkill /f /im mspaint.exe")   

        elif "open notepad" in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)  

        elif "close notepad" in query:
             os.system("C:\\Windows\\System32\\taskkill /f /im notepad.exe") 

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("C:\\Windows\\System32\\taskkill /f /im cmd.exe")   

        elif 'play music' in query or 'play songs' in query:
            music_dir="C:\\Users\\ADMIN\\Music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'close music' in query:
            os.system("C:\\Windows\\System32\\taskkill /f /im Microsoft.Media.Player.exe")

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'shutdown' in query or 'turn off' in query:
            speak('ok sir')
            speak('Make sure all of your applications are closed')
            time.sleep(5)
            subprocess.call(['shutdown', '/s'])
            
        elif 'restart' in query:
            subprocess.call(['shutdown', '/r'])

        elif "lock the screen" in query:
            subprocess.call(['shutdown', '/i'])

        elif "hibernate" in query:
            speak('Hibernating...')
            subprocess.call(['shutdown', '/h']) 

        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam', img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "take snapshot" in query or 'take photo' in query:
            cap = cv2.VideoCapture(0)
            ret, img = cap.read()
            snapshot_filename = "snapshot.jpg"
            cv2.imwrite(snapshot_filename, img)
            cap.release()
            cv2.destroyAllWindows()
            print("Snapshot taken and saved as", snapshot_filename)
            
            
        elif "exit" in query:
            speak('alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name=takeCommand().lower()
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")         

        elif "my ip address" in query:
            speak("checking")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip address is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")       

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")   
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
       
        elif "write project title in notepad" in query:
            pyautogui.press('win', 1)
            pyautogui.write(' notepad', 0.5)
            pyautogui.press('enter', 1)
            time.sleep(1)        
            pyautogui.typewrite("  AI-Based Desktop virtual Assistant", 0.3)

        elif 'type' in query:
            query=query.replace("type", "")
            pyautogui.typewrite(f"{query}", 0.1)

        elif 'open amazon' in query:
            speak("here we go to amazon sir. happy shopping")
            webbrowser.open("amazon.in")

        elif 'where is' in query:
            query=query.replace("where is", "")
            location=query
            speak("Locating...")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"") 

        elif 'file save' in query:
            speak('ok sir')
            pyautogui.hotkey('ctrl', 's')  
            time.sleep(1)
            pyautogui.write(f"Jarviis.txt")
            time.sleep(2)
            pyautogui.press("enter")
            speak("notes saved") 

        elif 'tell me joke' in query:
            speak(pyjokes.get_joke(language="en",category="neutral"))

        elif 'switch window' in query:
            pyautogui.hotkey('alt', 'tab')

        elif 'cpu status' in query:
            cpu()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("recycle bin recycled")

        elif "movie" in query:
            movie()

        elif "news" in query:
            news()  

        elif "play game" in query:
            rock() 

        elif 'open mail' in query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            pyautogui.moveTo(x=1307, y=464, duration=1)
            pyautogui.click(x=1307, y=464, clicks=1, interval=0, button='left') 
            pyautogui.moveTo(x=1157, y=474, duration=1)
            pyautogui.click(x=1157, y=474, clicks=1, interval=0, button='left') 

        elif 'email to computer' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="palwaidheeraj2003@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email") 

        elif 'send mail' in query:
            try:
                speak("What message do you want me to sent?")
                content=takeCommand()
                speak("whom should i send")
                to=input("Enter to address:")
                #to=takeCommand()
                send_email(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email") 


        elif 'send message' in query or 'send a message' in query:
            account_sid="AC33f6637516e9cc27bc114503c1888b22"
            auth_token="e084ddc0315ef6058b12b1c3de9bddc0"
            client=Client(account_sid,auth_token)
            speak("What should i send")
            message=client.messages.create(
                body=takeCommand(), from_="+ 13612647756", to="+919618535423")
            speak("message send succesfully")



      








               



            

                





