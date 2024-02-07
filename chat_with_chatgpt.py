#INTELLIGENT CHATBOT
import openai

openai.api_key = "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"
messages = [{"role":"system","content":"You are a itelligent assistant."}]

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
