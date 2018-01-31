#!/usr/bin/en-ukv python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os

tts = gTTS(text='Good morning Sir, What would you like me to do.', lang='en-uk')
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
    if micinput == ("who created you"):
        tts = gTTS(text='I made myself thank you very much!', lang='en-uk')
        tts.save("creator.mp3")
        playsound('creator.mp3')
        os.remove("creator.mp3")
    elif micinput == ("My Singing Monsters"):
        tts = gTTS(text='Hey i think i have played that game', lang='en-uk')
        tts.save("msg.mp3")
        playsound('msg.mp3')
        os.remove("msg.mp3")
    elif micinput == ("is the cake a lie"):
        tts = gTTS(text='yes', lang='en-uk')
        tts.save("yes.mp3")
        playsound('yes.mp3')
        os.remove("yes.mp3")
    elif micinput ==("Braydon says shut up"):
        tts = gTTS(text='You can never make me be quiet!', lang='en-uk')
        tts.save("bssu.mp3")
        playsound('bssu.mp3')
        os.remove("bssu.mp3")
    elif micinput == ("am I dead"):
        tts = gTTS(text='Are you?', lang='en-uk')
        tts.save("dead.mp3")
        playsound('dead.mp3')
        os.remove("dead.mp3")
    elif micinput == ("when will the world end"):
        tts = gTTS(text='when-uk there are no memes', lang='en-uk')
        tts.save("end.mp3")
        playsound('end.mp3')
        os.remove("end.mp3")
    elif micinput == ("who is Travis"):
        tts = gTTS(text='Travis is an idiot', lang='en-uk')
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
        tts = gTTS(text='The time is ' + hour + ' ' + minute, lang='en-uk')
        tts.save("time.mp3")
        playsound('time.mp3')
        os.remove("time.mp3")
    elif micinput == ("fire"):
        print("PEW")
        tts = gTTS(text='PEW', lang='en-uk')
        tts.save("PEW.mp3")
        playsound('PEW.mp3')
        os.remove("PEW.mp3")
    elif micinput == ("shut down"):
        print("shutdown")
        tts = gTTS(text='Shuting Down', lang='en-uk')
        tts.save("shutingdown.mp3")
        playsound('shutingdown.mp3')
        os.remove("shutingdown.mp3")
        break
    else:
        print("error")
        tts = gTTS(text='I do not understand ' + micinput, lang='en-uk')
        tts.save("understand.mp3")
        playsound('understand.mp3')
        os.remove("understand.mp3")
    tts = gTTS(text='Is there anything else you would like me to do sir?', lang='en-uk')
    tts.save("else.mp3")
    playsound('else.mp3')
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        micinput = r.recognize_google(audio)
    if micinput == 'no':
        tts = gTTS(text='Ok Sir.', lang='en-uk')
        tts.save("oksir.mp3")
        playsound('oksir.mp3')
        os.remove("oksir.mp3")
        break
    if micinput == 'yes':
        tts = gTTS(text='Ok Sir, what would you like to do', lang='en-uk')
        tts.save("oksir2.mp3")
        playsound('oksir2.mp3')
        os.remove("oksir2.mp3")
