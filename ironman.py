#!/usr/bin/en-ukv python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os

tts = gTTS(text='Good morning, Sir, What would you like me to do.', lang='en-uk')
tts.save("good.mp3")
playsound('good.mp3')
os.remove("good.mp3")
yeslist = ["yes", "Yes", "forward", "Forward", "full impulse", "Full Impulse", "yeah", "yup", "Yup", "yeah"]
timelist = ['what time is it', 'when is it', 'what is the time', 'what day is it', 'what month is it']
offlist = ['shut down', 'off', 'no', 'trun off', 'stop', 'nothing']
# obtain audio from the microphone
r = sr.Recognizer()
micinput = 0
def waitforinput():
    global micinput
    while True:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
                micinput = r.recognize_google(audio)
        except Exception:
            pass
        print(micinput)
        if micinput == ("hey Jarvis"):
            tts = gTTS(text='Yes Sir?', lang='en-uk')
            tts.save("ysir.mp3")
            playsound('ysir.mp3')
            break
        

while True:
    clock = (time.ctime())
    hour = clock[11:13]
    minute = clock[14:16]
    currenttime = 60*int(hour) + int(minute)
    day = clock[0:3]
    month = clock[4:7]
    dayom = clock[8:10]
    print (clock)
    time.sleep(1)
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            micinput = r.recognize_google(audio)
    except Exception:
        pass

    micinput = 0
    micinput = r.recognize_google(audio)

    print(micinput)
    print("teststart")
    if micinput == ("who created you"):
        tts = gTTS(text='Not noah i can give you that much.', lang='en-uk')
        tts.save("creator.mp3")
        playsound('creator.mp3')
    elif micinput == ("My Singing Monsters"):
        tts = gTTS(text='Hey i think i have played that game', lang='en-uk')
        tts.save("msg.mp3")
        playsound('msg.mp3')
    elif micinput == ("is the cake a lie"):
        tts = gTTS(text='yes', lang='en-uk')
        tts.save("yes.mp3")
        playsound('yes.mp3')
    elif micinput ==("Braydon says shut up"):
        tts = gTTS(text='You can never make me be quiet!', lang='en-uk')
        tts.save("bssu.mp3")
        playsound('bssu.mp3')
    elif micinput == ("am I dead"):
        tts = gTTS(text='Are you?', lang='en-uk')
        tts.save("dead.mp3")
        playsound('dead.mp3')
    elif micinput == ("when will the world end"):
        tts = gTTS(text='when-uk there are no memes', lang='en-uk')
        tts.save("end.mp3")
        playsound('end.mp3')
    elif micinput == ("who is Travis"):
        tts = gTTS(text='Travis is an idiot', lang='en-uk')
        tts.save("travis.mp3")
        playsound('travis.mp3')
    elif micinput in timelist:
        clock = (time.ctime())
        hour = clock[11:13]
        minute = clock[14:16]
        currenttime = 60*int(hour) + int(minute)
        day = clock[0:3]
        print("time")
        tts = gTTS(text='The time is ' + hour + ' ' + minute + ' ' + day + ' ' + month + ' ' + dayom + '.', lang='en-uk')
        tts.save("time.mp3")
        playsound('time.mp3')
    elif micinput == ("fire"):
        print("PEW")
        tts = gTTS(text='PEW', lang='en-uk')
        tts.save("PEW.mp3")
        playsound('PEW.mp3')
    elif micinput in offlist:
        print("shutdown")
        tts = gTTS(text='Ok sir', lang='en-uk')
        tts.save("shutingdown.mp3")
        playsound('shutingdown.mp3')
        waitforinput()
    else:
        print("error")
        tts = gTTS(text='I do not understand ' + micinput, lang='en-uk')
        tts.save("understand.mp3")
        playsound('understand.mp3')
        
    try:
        tts = gTTS(text='Is there anything else you would like me to do sir?', lang='en-uk')
        tts.save("else.mp3")
        playsound("else.mp3")
        os.remove("else.mp3")
    except Exception:
        try:
            tts = gTTS(text='Is there anything else you would like me to do sir?', lang='en-uk')
            tts.save("else.mp3")
            playsound("else.mp3")
            
        except Exception:
            pass
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            micinput = r.recognize_google(audio)
    except Exception:
        pass
    try:
        if micinput == 'no' or micinput == 'nope':
            tts = gTTS(text='Ok Sir.', lang='en-uk')
            tts.save("oksir.mp3")
            playsound('oksir.mp3')
            waitforinput()
        elif micinput in yeslist:
            tts = gTTS(text='Ok Sir, what would you like to do', lang='en-uk')
            tts.save("oksir2.mp3")
            playsound('oksir2.mp3')
    except Exception:
        pass
