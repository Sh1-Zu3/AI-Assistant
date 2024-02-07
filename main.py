# Resize the Window - Non Pep8 Compliant, mandated by Kivy
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

import speech_recognition as sr
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import pyttsx3

#INTELLIGENT CHATBOT
import openai

#SPEAK 
from gtts import gTTS
import playsound
import os 

#TRANSLATE
#import Language_Translate_Python
#from chat_with_chatgpt import chat_with_chatgpt
#oajwofjaow
USER = "USER"
AI = "Ci"

openai.api_key = "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"
messages = [{"role":"system","content":"You are a itelligent assistant."}]

def Speak(text,lan):
            tts = gTTS(text=text,lang=lan)
            filename = "voice.mp3"
            tts.save(filename)
            playsound.playsound(filename,True)
            os.remove(filename)


r = sr.Recognizer()
m = sr.Microphone()
t = pyttsx3.init()
t.setProperty('rate', 90)
t.setProperty('voice', t.getProperty('voices')[1].id)




#english_bot = ChatBot("Rao")

#Custom conversation list
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "do you have boyfriend",
    "yes",
    "what is gold plan?",
    "lets explain about the gold plan.. are you clear about this?",
    "quit",
    "bye bye",
    "search for power tools",
    "power tools"
]

#set the type of trainer to chatbot
#english_bot.set_trainer(ListTrainer)
#set the list for train
#english_bot.train(conversation)

MAIN_LANGUAGES = "vi"

# Root Widget
class Root(BoxLayout):
    pass

class RecordButton(Button):
    # String Property to Hold output for publishing by Textinput
    output = StringProperty('')
    inputarea = StringProperty('')
    
    def record(self):
        # GUI Blocking Audio Capture
        #while True: 
        with m as source:
            audio = r.listen(source)
        
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio,language = MAIN_LANGUAGES)
            
            #translate
            #value_tran = Language_Translate_Python.translates(value,MAIN_LANGUAGES,"en")
            
            for i in range(100):
                print(value)
            
            self.inputarea = "\"{}\"".format(value)
            
            #respstr = chat_with_chatgpt(value_tran)
            for i in range(100):
                print(value)
            
            #respstr = Language_Translate_Python.translates(respstr,"en",MAIN_LANGUAGES)
            
            Speak(value,MAIN_LANGUAGES)
            
            #t.runAndWait()
            
            self.output = "Reply by me \"{}\"".format(value)
            
            if value=='quit':
                return
            
        
        except sr.UnknownValueError:
            self.output = ("Oops! I failed to catch you :")
        
        except sr.RequestError as e:
            
            self.output = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


class SpeechChatBotApp(App):
    
    def build(self):
        # Calibrate the Microphone to Silent Levels
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
        # Create a root widget object and return as root
        return Root()


# When Executed from the command line (not imported as module), create a new SpeechApp
if __name__ == '__main__':
    SpeechChatBotApp().run()
