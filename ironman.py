#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os

tts = gTTS(text='Good morning Sir, What would you like me to do.', lang='en')
tts.save("good.mp3")
playsound('good.mp3')
os.remove("good.mp3")

# obtain audio from the microphone
r = sr.Recognizer()


while True:
    clock = (time.ctime())
    hour = clock[11:13]
    minute = clock[14:16]
    currenttime = 60*int(hour) + int(minute)
    day = clock[0:3]
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    micinput = 0
    micinput = r.recognize_google(audio)
    
    print(micinput)
    if micinput == ("who is Travis"):
        tts = gTTS(text='Travis is an idiot', lang='en')
        tts.save("travis.mp3")
        playsound('travis.mp3')
        os.remove("travis.mp3")
    elif micinput == ("what time is it"):
        clock = (time.ctime())
        hour = clock[11:13]
        minute = clock[14:16]
        currenttime = 60*int(hour) + int(minute)
        day = clock[0:3]
        print("time")
        tts = gTTS(text='The time is ' + hour + ' ' + minute, lang='en')
        tts.save("time.mp3")
        playsound('time.mp3')
        os.remove("time.mp3")
    elif micinput == ("fire"):
        print("PEW")
        tts = gTTS(text='PEW', lang='en')
        tts.save("PEW.mp3")
        playsound('PEW.mp3')
        os.remove("PEW.mp3")
    elif micinput == ("shut down"):
        print("shutdown")
        tts = gTTS(text='Shuting Down', lang='en')
        tts.save("shutingdown.mp3")
        playsound('shutingdown.mp3')
        os.remove("shutingdown.mp3")
        break
    else:
        print("error")
        tts = gTTS(text='I do not understand ' + micinput, lang='en')
        tts.save("understand.mp3")
        playsound('understand.mp3')
        os.remove("understand.mp3")
    tts = gTTS(text='Is there anything else you would like me to do sir?', lang='en')
    tts.save("else.mp3")
    playsound('else.mp3')
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        micinput = r.recognize_google(audio)
    if micinput == 'no':
        tts = gTTS(text='Ok Sir.', lang='en')
        tts.save("oksir.mp3")
        playsound('oksir.mp3')
        os.remove("oksir.mp3")
        break
    if micinput == 'yes':
        tts = gTTS(text='Ok Sir, what would you like to do', lang='en')
        tts.save("oksir2.mp3")
        playsound('oksir2.mp3')        
        os.remove("oksir2.mp3")

