#INTELLIGENT CHATBOT
import openai



#TRANSLATE
import Language_Translate_Python

#SPEAK 
from gtts import gTTS
import playsound
import os 

#SPEECH RECOGNITION
from datetime import datetime
import speech_recognition as sr
import pyttsx3


#TIME
import datetime

#LISTEN TO MUSIC
#import Listen_to_music
#using selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import cv2


#READ NEWPAPER
import random
import types_crawler as ReadPaper


def main_():
        #oajwofjaow
        USER = "USER"
        AI = "Ci"

        #API CHATBOT
        openai.api_key = "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"
        messages = [{"role":"system","content":"You are a itelligent assistant."}]

        #simply print:))
        def PRINTF(text,role):
            print(role,": ",text)

        #DEF SPEAK
        def Speak(text,lan):
            tts = gTTS(text=text,lang=lan)
            filename = "voice.mp3"
            tts.save(filename)
            playsound.playsound(filename,True)
            os.remove(filename)
            
        def SpeakPaper(text,lan):
            tts = gTTS(text=text,lang=lan)
            filename = "voice.mp3"
            tts.save(filename)
            playsound.playsound(filename,False)
            os.remove(filename)

        #SEND AND HAVE ANSWER FROM CHATBOT
        def chat_with_chatgpt(message):
            messages.append(
                    {"role":"user","content":message},
            )
            
            chat = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",messages = messages,temperature=0.5        
            )
            
            reply = chat.choices[0].message.content
            messages.append({"role":"assistant","content":reply})
            
            return reply


        #SETUP SPEECH
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        activationWord = 'Computer'


        #Ham nhan dien giong noi
        def parseCommand(lan):
            listener = sr.Recognizer()
            
            with sr.Microphone() as source:
                listener.pause_threshold = 2
                input_speech = listener.listen(source)
                
            try:
                #print("listening:...")
                query = listener.recognize_google(input_speech, language=lan)
                PRINTF(query,USER)
                
            except Exception as exception:
                nof = "Tôi không nghe bạn nói gì"
                nof_translate = Language_Translate_Python.translates(nof,"vi",MAIN_LANGUAGES)
                #Speak(nof_translate,lan)
                #PRINTF(nof,AI)
                #PRINTF(Exception,AI)
                return ""
            
            return query

        #TIME
        def get_time(lan):
            now = datetime.datetime.now()
            text = 'Bây giờ là' + str(now.hour) + ' giờ ' +str(now.minute) +' phút ngày ' +str(now.day)+'tháng '+str(now.month)+ ' năm ' +str(now.year)
            text_translate = Language_Translate_Python.translates(text,"vi",MAIN_LANGUAGES)
            PRINTF(text_translate,AI)
            Speak(text,lan)
            
        #Huong dan cach su dung
        def construction(lan):
            text = chat_with_chatgpt(Language_Translate_Python.translates("bạn hãy cung cấp chi tiết khả năng của mình ","vi","en"))
            text_translate = Language_Translate_Python.translates(text,"en",MAIN_LANGUAGES)
            PRINTF(text_translate,AI)
            Speak(text_translate,lan)


        def play():
            play_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@title='Play (k)']")))
            play_btn.click()

        def mute():
            mute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Mute (m)']")))
            mute_btn.click()

        # comment out to test mute_btn, otherwise it happens so fast you don't notice it
        def unmute():
            unmute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Unmute (m)']")))
            unmute_btn.click()

        def exit():
            driver.close()

        #Khởi tạo biến check music
        music = False
        #Khởi tạo biến talking
        talk = False
        #Khởi tạo biến đếm cnt để ra lệnh cho chatbot
        cnt=0
        #khởi tạo biến đang giao tiếp với ci
        speaking = False
        #doc bao
        reading =False
        list_paper = ["thời sự",
                    "du lịch",
                    "thế giới",
                    "kinh doanh",
                    "khoa học",
                    "giải trí",
                    "thể thao",
                    "pháp luật",
                    "giáo dục",
                    "sức khỏe",
                    "đời sống",
                    ]

        translate_listpaper = {
                    "thời sự" : "thoi-su",
                    "du lịch" : "du-lich",
                    "thế giới": "the-gioi",
                    "kinh doanh":"kinh-doanh",
                    "khoa học":"khoa-hoc",
                    "giải trí":"giai-tri",
                    "thể thao":"the-thao",
                    "pháp luật":"phap-luat",
                    "giáo dục":"giao-duc",
                    "sức khỏe":"suc-khoe",
                    "đời sống":"doi-song",
        }

    #----------------------MAIN CODE----------------------
    
        #LAY MAIN_LANGUAGE
        MAIN_LANGUAGES = "vi"
        
        #SETUP
        _ = chat_with_chatgpt(Language_Translate_Python.translates("""Từ nay bạn có tên là Ci nhé.Chào ci, nếu ai đó hỏi bạn có chức năng gì thì xin hãy nói cho họ rằng họ cần nói từ khóa 'hướng dẫn' nhé, 
        và nếu ai đó hỏi bạn có thể làm gì thì bạn hãy trả lời bạn có thể làm gì ra nhé và bạn hãy nói bạn còn có thể hát nhạc cho mọi người nghe chỉ cần nói từ khóa 'nghe nhạc' và nói tên bản nhạc mà học muốn nghe hoặc ca sĩ mà họ yêu thích và bạn hãy trả lời lại là duy nhất cụm từ là tên bài hát, và bạn có thể đọc báo cho mọi người nghe chỉ cần nói từ khóa 'đọc báo' và nói từ khóa bạn muốn đọc ví dụ như đọc báo khoa học,đọc báo thời sự,đọc báo thế giới.Nếu tôi hỏi bạn có thể làm những gì thì trả lời thêm những chức năng ở trên nhé,
        và nếu tôi hỏi cách sử dụng của chức năng nghe nhạc thì hãy nói bạn có thể nói từ khóa tắt nhạc để kết thúc bài hát,
        ""","vi",'en'))
        #print(Language_Translate_Python.translates(_,"en","vi"))
            
        #Thong bao chatbot da san sang
        text_start = chat_with_chatgpt(Language_Translate_Python.translates("Xin chào, bạn tên là gì?","vi",'en'))
        #text_start = chat_with_chatgpt(Language_Translate_Python.translates("nghe nhạc một con vịt","vi",'en'))

        text_start_translate = Language_Translate_Python.translates(text_start,"en",MAIN_LANGUAGES)
            
        PRINTF(text_start_translate,AI)
            
        Speak(text_start_translate,MAIN_LANGUAGES)
        
        #time = 0
        
        #while time<=20:
            
        time+=1
        print(time)
            
        #Lay voice
        query = parseCommand(MAIN_LANGUAGES).lower()                
                
        split_query = query.split()
        if len(query)>0 and query!="":            
            if Language_Translate_Python.translates("giờ","vi",MAIN_LANGUAGES) in split_query or Language_Translate_Python.translates("ngày","vi",MAIN_LANGUAGES) in split_query:
                    
                #time = 0 
                get_time(MAIN_LANGUAGES)
                        
            elif query == Language_Translate_Python.translates("hướng dẫn","vi",MAIN_LANGUAGES):
                    
                #time = 0 
                construction(MAIN_LANGUAGES)
                        
            elif Language_Translate_Python.translates("nghe","vi",MAIN_LANGUAGES) in split_query[0] and Language_Translate_Python.translates("nhạc","vi",MAIN_LANGUAGES) in split_query[1]:
                    
                #time = 0 
                    
                text = query[:]
                text_translate = Language_Translate_Python.translates(text,"vi",MAIN_LANGUAGES)
                            
                PRINTF(text_translate,AI)
                Speak(text_translate,MAIN_LANGUAGES)
                        
                #setup thoi
                music = True
                        
                #Listen_to_music.OpenYtb(query)
                            
                driver = webdriver.Chrome()
                driver.maximize_window()

                wait = WebDriverWait(driver, 3)
                presence = EC.presence_of_element_located
                visible = EC.visibility_of_element_located

                video =query
                    # Navigate to url with video being appended to search_query
                driver.get('https://www.youtube.com/results?search_query={}'.format(str(video)))

                # play the video
                wait.until(visible((By.ID, "video-title")))
                driver.find_element(By.ID, "video-title").click()

                all_iframes = driver.find_elements("name","iframe")  
                        
                playing = True
                mute=True 
                        
                while music:
                            
                    command = parseCommand(MAIN_LANGUAGES).lower()
                            
                    if (command == Language_Translate_Python.translates("tắt nhạc","vi",MAIN_LANGUAGES)):
                                
                        PRINTF(Language_Translate_Python.translates("đang tắt nhạc","vi",MAIN_LANGUAGES),AI)
                        Speak(Language_Translate_Python.translates("đang tắt nhạc","vi",MAIN_LANGUAGES),MAIN_LANGUAGES)
                                
                        driver.close()
                        music=False
                                
            elif Language_Translate_Python.translates("đọc","vi",MAIN_LANGUAGES) in split_query[0] and Language_Translate_Python.translates("báo","vi",MAIN_LANGUAGES) in split_query[1]:
                        
                #time = 0 
                
                text = query[:]
                text_translate = Language_Translate_Python.translates(text,"vi",MAIN_LANGUAGES)
                            
                PRINTF(text_translate,AI)
                Speak(text_translate,MAIN_LANGUAGES)
                        
                text = Language_Translate_Python.translates("Đang tải,bạn vui lòng đợi trong giây lát","vi",MAIN_LANGUAGES)
                        
                PRINTF(text,AI)
                Speak(text,MAIN_LANGUAGES)
                        
                #setup thoi
                reading = True
                        
                topic = text[8:]
                        
                if topic in list_paper:
                    pass
                else:
                    topic = random.choice(list_paper)
                                            
                topic = translate_listpaper[topic]
                        
                #reading paper
                reading_now = True 
                        
                #number of paper now:v
                cnt = 1
                tmp=""
                namepaper = "url_" #url_01.txt
                                    
                if ReadPaper.main_code(topic) :
                                            
                    while reading == True:
                                
                        tmp=""
                        if (cnt<10):tmp = "0"
                        File_Now = open("data/results/"+str(topic)+"/"+namepaper+str(tmp)+str(cnt)+'.txt',encoding='utf-8') #"url_01.txt"
                        content = File_Now.read()
                        PRINTF(content,AI)
                        Speak(content,MAIN_LANGUAGES)
                                
                        File_Now.close()
                        PRINTF(Language_Translate_Python.translates("Bạn có muốn đọc tiếp? Nếu có vui lòng nói từ khóa'đọc tiếp' nếu không vui lòng nói 'không đọc tiếp' ","vi",MAIN_LANGUAGES),AI)
                        Speak(Language_Translate_Python.translates("Bạn có muốn đọc tiếp? Nếu có vui lòng nói từ khóa'đọc tiếp' nếu không vui lòng nói 'không đọc tiếp' ","vi",MAIN_LANGUAGES),MAIN_LANGUAGES)
                            
                        speaking = True 
                        while speaking==True:
                            command = parseCommand(MAIN_LANGUAGES).lower()
                            if (command == Language_Translate_Python.translates("đọc tiếp","vi",MAIN_LANGUAGES)):
                                cnt+=1
                                speaking=False
                            elif (command == Language_Translate_Python.translates("không đọc tiếp","vi",MAIN_LANGUAGES)):
                                reading=False 
                                speaking=False            
            else:
                #Xu ly
                #if (len(query)>0 and query!=""):                    
                        #TRANSLATE TO ENGLISH LANGUAGES
                        text_translate = Language_Translate_Python.translates(query,MAIN_LANGUAGES,"en")
                        print(text_translate)
                        if text_translate:                        
                            Text_Chatbot = chat_with_chatgpt(text_translate)
                                        
                            #TRANSLATE ANSWER TO MAIN LANGUAGE
                            Text_Chatbot_translate = Language_Translate_Python.translates(Text_Chatbot,"en",MAIN_LANGUAGES)
                                        
                            #SPEAK ANSWER
                            PRINTF(Text_Chatbot_translate,AI)
                            
                            #print("CC")
                            
                            Speak(Text_Chatbot_translate,MAIN_LANGUAGES)
                            #time = 0
                             
if __name__=="__main__":
    main_()