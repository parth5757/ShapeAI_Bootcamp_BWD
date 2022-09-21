from pynput import keyboard
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit #pip install pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    speak("I am avneet kaur. Please tell me how may I help you")       

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
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return takeCommand()
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('psthakkar2@gmail.com', '21502I.T@parth')
    server.sendmail('psthakkar2@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open 1' in query:
            webbrowser.open("https://www.google.com/")     

        elif 'google' in query:
            speak("say want you search")
            content = takeCommand()
            webbrowser.open('https://www.google.co.in/?#q=' +content)                  

        elif 'open 2' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'youtube' in query:
            speak("say want you search")
            content = takeCommand()
            webbrowser.open('https://www.youtube.com/results?search_query=' +content)

        elif 'open problem solver' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open linkdin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")

        elif 'open gaana' in query:
            webbrowser.open("https://gaana.com/")

        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/h")

        elif 'open TC 5' in query:
            webbrowser.open("file:///D:/HtML%20CSS%20&%20JAVASCRIPT/time%20table/responsive-table-v2/Table_Responsive_v2/index.html")

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open 5757' in query:
            webbrowser.open("https://github.com/")

        elif 'open channel one' in query:
            webbrowser.open("https://www.youtube.com/channel/UCStj-ORBZ7TGK1FwtGAUgbQ")

        elif 'open channel 2' in query:
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww") 

        elif 'open my chat' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'open Grow' in query:
            webbrowser.open("https://groww.in/dashboard/explore/stocks")

        elif 'open Stocke analyzer' in query:
            webbrowser.open("https://www.screener.in/watchlist/")

        elif 'open hotstar' in query:
            webbrowser.open("https://www.hotstar.com/in")            
            
        elif 'password' in query:
            print("sir your Google Password is 21502I.T@parth")
            print("sir your phone Password is 2157")
            print("sir your laptop Password is parth21")
            print("sir your Google Password is 21502I.T@parth")
            print("sir your wif  Password is 2157I.T@parth")
            print("sir your git hub Password is 21502I.T@parth")
            print("sir your ms office Password is 21502I.T@parth")
            print("sir your outlook Password is dell1234")
            print("sir your mcafee Password is 21502I.T@parth")
            print("sir your Programing guruji Password is 21502I.T@parth")
        
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\PARTH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)        

        elif 'open brave' in query:
            codePath = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
            os.startfile(codePath) 
            
        elif 'open college time table' in query:
            codePath = "C:\\Users\\PARTH\\OneDrive\\Desktop\\sem 4 time table.jpeg"
            speak("opening time table") 
            os.startfile(codePath)
            print("parth time table is opened")

        elif 'open 3rd sem' in query:
            codePath = "E:\sal\SEM - 3"
            os.startfile(codePath)

        elif 'open 4th sem' in query:
            codePath = "E:\sal\SEM - 4"
            os.startfile(codePath)
            
        elif 'open 5th sem' in query:
            codePath = "E:\sal\SEM - 5"
            os.startfile(codePath)            

        # elif 'close browser' or 'stop browser' or 'shut down browser' in query:
        #     os.system("taskkill/im chrome.exe")

        # elif 'close app' or 'stop app' in query:
        #     os.system("taskkill/im Code.exe")
        
        elif 'mummy' in query:
                speak("What should I say?")
                content = takeCommand()
                # speak("at which hours")
                # hours = takeCommand()
                # speak("at which miutes")
                # minutes = takeCommand()
                pywhatkit.sendwhatmsg('+919173142133', content, 11, 27)        

        elif 'parth' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "psthakkar2@outlook.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my love parth. I am not able to send this email")























        #     elif 'open monday' in query:
        #     webbrowser.open("https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9")
        #     webbrowser.open("https://www.youtube.com/watch?v=DD3ou9sa3Z8&list=PLu0W_9lII9agAiWp6Y41ueUKx1VcTRxmf")

        # elif 'open tuesday' in query:
        #     webbrowser.open("https://www.youtube.com/watch?v=gfDE2a7MKjA&t=6031s")
        #     webbrowser.open("https://www.youtube.com/watch?v=61a7UkDO50s&t=3s")

        # elif 'open wednesday' in query:
        #     webbrowser.open("https://www.youtube.com/watch?v=_u-PaJCpwiU&list=PLu0W_9lII9ai6fAMHp-acBmJONT7Y4BSG")
        #     webbrowser.open("https://www.youtube.com/results?search_query=artificial+intelligence+using+python")
        #     webbrowser.open("https://www.youtube.com/watch?v=XIrOM9oP3pA&t=1173s")

        # elif 'open thursday' in query:
        #     webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agK8pojo23OHiNz3Jm6VQCH")
        #     webbrowser.open("https://www.youtube.com/results?search_query=artificial+intelligence+using+python")

        # elif 'open friday' in query:
        #     webbrowser.open("https://www.youtube.com/watch?v=Rbh1rieb3zc")
        #     webbrowser.open("https://www.youtube.com/watch?v=Q-__8Xw9KTM")

        # elif 'open saturday' in query:
        #     webbrowser.open("https://www.youtube.com/watch?v=6mbwJ2xhgzM&list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg")
        #     webbrowser.open("https://www.youtube.com/watch?v=hKB-YGF14SY")
        #     webbrowser.open("https://youtube.com/playlist?list=PLbGui_ZYuhiihdSW-kg50d0L4or1DWvko")

        # elif 'open sunday' in query:
        #     webbrowser.open("https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9")
        #     webbrowser.open("https://www.youtube.com/watch?v=DD3ou9sa3Z8&list=PLu0W_9lII9agAiWp6Y41ueUKx1VcTRxmf")
        #     webbrowser.open("https://www.youtube.com/watch?v=gfDE2a7MKjA&t=6031s")
        #     webbrowser.open("https://www.youtube.com/watch?v=61a7UkDO50s&t=3s")
        #     webbrowser.open("https://www.youtube.com/watch?v=_u-PaJCpwiU&list=PLu0W_9lII9ai6fAMHp-acBmJONT7Y4BSG")
        #     webbrowser.open("https://www.youtube.com/results?search_query=artificial+intelligence+using+python")
        #     webbrowser.open("https://www.youtube.com/watch?v=pF-h1YCS5GE&list=PLu0W_9lII9agK8pojo23OHiNz3Jm6VQCH-")
        #     webbrowser.open("https://www.youtube.com/results?search_query=artificial+intelligence+using+python")
        #     webbrowser.open("https://www.youtube.com/watch?v=Rbh1rieb3zc")
        #     webbrowser.open("https://www.youtube.com/watch?v=Q-__8Xw9KTM")
        #     webbrowser.open("https://www.youtube.com/watch?v=6mbwJ2xhgzM&list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg")
        #     webbrowser.open("https://www.youtube.com/watch?v=hKB-YGF14SY")
        #     webbrowser.open("https://youtube.com/playlist?list=PLbGui_ZYuhiihdSW-kg50d0L4or1DWvko")