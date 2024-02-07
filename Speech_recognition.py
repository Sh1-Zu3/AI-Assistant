import speech_recognition as sr
from gtts import gTTS
import os 
import time 
import playsound

r = sr.Recognizer()


#SPEAK
def Speak(text):
    tts = gTTS(text=text,lang="vi")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    
#LISTEN
while True:
    with sr.Microphone() as source:
        audio_data = r.record(source,duration=5)
    try:
        text = r.recognize_google(audio_data,language="vi")
    except:
        text=''
    print(text)
    
    if text=='':
        text_AI="Bạn muốn đặt câu hỏi gì tôi?"
        print(text_AI)
        Speak(text_AI)