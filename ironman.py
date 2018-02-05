#ironman.py

# NOTE: this requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os
tts = gTTS(text='Good morning, Sir, What would you like me to do.', lang='en-uk')
tts.save("./assets/voices_tts/good.mp3")
playsound('./assets/voices_tts/good.mp3')
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
            tts.save("./assets/voices_tts/ysir.mp3")
            playsound('./assets/voices_tts/ysir.mp3')
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
        waitforinput()

    micinput = 0
    micinput = r.recognize_google(audio)

    print(micinput)
    print("teststart")
    if micinput == ("My Singing Monsters"):
        tts = gTTS(text='Hey i think i have played that game', lang='en-uk')
        tts.save("./assets/voices_tts/msg.mp3")
        playsound('./assets/voices_tts/msg.mp3')
    elif micinput == ("is the cake a lie"):
        tts = gTTS(text='yes', lang='en-uk')
        tts.save("./assets/voices_tts/yes.mp3")
        playsound('./assets/voices_tts/yes.mp3')
    elif micinput ==("Bradon says shut up"):
        tts = gTTS(text='You can never make me be quiet!', lang='en-uk')
        tts.save("./assets/voices_tts/bssu.mp3")
        playsound('./assets/voices_tts/bssu.mp3')
    elif micinput == ("am I dead"):
        tts = gTTS(text='Are you?', lang='en-uk')
        tts.save("./assets/voices_tts/dead.mp3")
        playsound('./assets/voices_tts/dead.mp3')
    elif micinput == ("when will the world end"):
        tts = gTTS(text='when-uk there are no memes', lang='en-uk')
        tts.save("./assets/voices_tts/end.mp3")
        playsound('./assets/voices_tts/end.mp3')
    elif micinput == ("who is Travis"):
        tts = gTTS(text='Travis is an idiot', lang='en-uk')
        tts.save("./assets/voices_tts/travis.mp3")
        playsound('./assets/voices_tts/travis.mp3')
    elif micinput in timelist:
        clock = (time.ctime())
        hour = clock[11:13]
        minute = clock[14:16]
        currenttime = 60*int(hour) + int(minute)
        day = clock[0:3]
        print("time")
        tts = gTTS(text='The time is ' + hour + ' ' + minute + ' ' + day + ' ' + month + ' ' + dayom + '.', lang='en-uk')
        tts.save("./assets/voices_tts/time.mp3")
        playsound('./assets/voices_tts/time.mp3')
    elif micinput == ("fire"):
        print("PEW")
        playsound('./assets/sounds_assets/firesound.mp3')
    elif micinput == ("what's K2"):
        print("k2")
        tts = gTTS(text='drug', lang='en-uk')
        tts.save("./assets/voices_tts/k2.mp3")
        playsound('./assets/voices_tts/k2.mp3')
    elif micinput in offlist:
        print("shutdown")
        tts = gTTS(text='Ok sir', lang='en-uk')
        tts.save("./assets/voices_tts/shutingdown.mp3")
        playsound('./assets/voices_tts/shutingdown.mp3')
        waitforinput()
    else:
        print("error")
        tts = gTTS(text='I do not understand ' + micinput, lang='en-uk')
        tts.save("./assets/voices_tts/understand.mp3")
        playsound('./assets/voices_tts/understand.mp3')
        
    try:
        tts = gTTS(text='Is there anything else you would like me to do sir?', lang='en-uk')
        tts.save("./assets/voices_tts/else.mp3")
        playsound("./assets/voices_tts/else.mp3")
    except Exception:
        try:
            tts = gTTS(text='Is there anything else you would like me to do sir?', lang='en-uk')
            tts.save("./assets/voices_tts/else.mp3")
            playsound("./assets/voices_tts/else.mp3")
            
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
            tts.save("./assets/voices_tts/oksir.mp3")
            playsound('./assets/voices_tts/oksir.mp3')
            waitforinput()
        elif micinput in yeslist:
            tts = gTTS(text='Ok Sir, what would you like to do', lang='en-uk')
            tts.save("./assets/voices_tts/oksir2.mp3")
            playsound('./assets/voices_tts/oksir2.mp3')
    except Exception:
        pass

