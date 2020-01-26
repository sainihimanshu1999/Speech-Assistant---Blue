import speech_recognition as sr
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts from gTTS

r =sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            blue_say(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)   
        except sr.UnknownValueError:
            blue_say('Sorry, i did not recognize that')
        except sr.RequestError:
            blue_say('sorry, our speech service is down')
        return voice_data

def blue_say(audio_string):
    tts = gTTS(text = audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    

def respond(voice_data):
    if 'how are you' in voice_data:
        blue_say('I am fine')
    if 'what is your name' in voice_data:
        blue_say('My name is blue')
    if 'what time is it' in voice_data:
        blue_say(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        blue_say('Here is what i found for' + search)
    if 'find location' in voice_data:
        location = record_audio('Which location do you want to search for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        blue_say('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
blue_say('How can i help you?')
while 1:
    voice_data= record_audio()
    respond(voice_data)

