import pyttsx3
import datetime
import smtplib
import re

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Identity():
    name=input("Enter your username!!\n")
    return name

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<14:
        speak("Good Noon")
    elif hour>=14 and hour<18:
        speak("Good AfterNoon")
    elif hour>=18 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night")

def email(to,content):
    ser=smtplib.SMTP('smtp.gmail.com', 587)
    ser.ehlo()
    ser.starttls()
    ser.login('Sender Email Address', 'Sender password')
    ser.sendmail('Sender Email Address', to, content)
    ser.close()

def mailer():
        #print(content)
    speak("Write your valid email's destination!!!")
    to=input()
    string='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(string,to):
        email(to,content)
        speak(f"Your Email has been sent {var}!! Thank You!!")
    else:
        mailer()

#MainFunction
if __name__=="__main__":
    var=Identity()
    wishMe()
    speak(f"{var}!! How Can I help You??")
  #  while True:
    speak("Write! What do you wanna send??")
    content=input()
    mailer()
        
    
