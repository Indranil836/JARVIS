#module

import pyttsx3      #pip install pyttsx
import datetime
import speech_recognition as sr     #pip install speech_recognition
import wikipedia        #pip install wikipedia
import webbrowser       #pip install webbrowser
import os
import smtplib




engine=pyttsx3.init("sapi5")             #for using inbild voice function of windows
voices=engine.getProperty("voices")     #for making a voices object
#print(voices[0].id)                    #to know male or female voice are using
engine.setProperty("voices", voices[0].id)  #to select perticular voice


#function
def speak(audio):
    engine.say(audio)            #to speak to audio string
    engine.runAndWait()

def wishMe():           #for wishing me
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("good evening")
    speak("I am  your jarvis,please say how can i help you")

def takeCommand():          #it take microphone input and string output generate
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenig...")
        r.pause_threshold=1     #to increase the listening time
        audio=r.listen(source)  #convert it to string

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-US")   #to search the result and en-in for english india
        print(f"User Said : {query}\n") #query=user said

    except Exception as e:      
        print(e)
        print("Say that again please...")
        return "None"   #if exception occurs than return None

    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gamil.com", password)
    server.sendmail("targeremail@gamil.com",to,content)
    server.close()




if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        #logic to exicute your task

        if 'wikipedia' in query:                    #wikidepia "install wikipedia"
            speak("Searching wikipedia...")
            query=query.replace("wikipedia", "")    
            results=wikipedia.summary(query,sentences=2)
            speak("Accourding to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("Here is the result")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("Here is the result")
            webbrowser.open("google.com")
        elif "open facebook" in query:
            speak("Here is the result")
            webbrowser.open("facebook.com")
        elif "open stackoverFlow" in query:
            speak("Here is the result")
            webbrowser.open("stackoverFlow.com")

        elif "play song" in query:
            music_dir="F:\\pendrive\\song 2017-18"      
            songs=os.listdir(music_dir)     #list dir
            os.startfile(os.path.join(music_dir,songs[4]))      #start music player

        elif "what is the time" in query:
            str_time=datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Sir the time is {str_time}")

        elif "who is your master" in query:
            speak("Here is the result")
            speak("Indranil roy is my boss and he made me...")

        elif "open firefox" in query:
            speak("Here is the result")
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif "open file" in query:
            speak("Here is the result")
            os.startfile("C:\\Users\\dell\\Downloads\\movies\\abdul sir")

        elif "open vscode" in query:
            os.startfile("E:\\Microsoft VS Code\\Code.exe")

        elif "email to indra" in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to="targetemail@gmail.com"
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send the email at the moment")

        elif "jarvis quit" in query:
            quit()




        

