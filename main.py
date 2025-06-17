import speech_recognition as sr
import webbrowser
import pyttsx3 #help for text to speech
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

#pip install pocketsphinx

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="your_api_key_here"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    

def speak(text):
    tts=gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def aiProcess(command):
    client=OpenAI(api_key="your_api_key_here",)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
    {"role": "user", "content": command}
  ]
)

    return completion.choices[0].message.content
    
def processCommand(c):
    if c.lower()=="open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startwith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
        
    else:
        output=aiProcess(c)
        speak(output)
        
        
    

if __name__=="__main__":
    # speak("Hey sir how may I help you")
    speak("Initializing Jarvis....")
    while True:
            #Listen for the wake word "Jarvis"
            #obtain audio from the microphone
            r=sr.Recognizer()

                
          

            print("recognizing")
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio=r.listen(source,timeout=2, phrase_time_limit=1)
                word=r.recognize_google(audio)

                
                
                if(word.lower()=="Jarvis"):
                    speak("Ya")
                    #Listen for command
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio=r.listen(source)
                        command=r.recognize_google(audio)
                        
                        processCommand(command)
                       
                    
            except Exception as e:
                print("Error; {0}".format(e))    
    


# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# # Check microphone list (for debugging)
# print(sr.Microphone.list_microphone_names())

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "your_api_key_hereA"

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
#     pygame.mixer.init()
#     pygame.mixer.music.load('temp.mp3')
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")

# def aiProcess(command):
#     client = OpenAI(api_key="your_api_key_hereA")
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#             {"role": "user", "content": command}
#         ]
#     )
#     return completion.choices[0].message.content

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music.get(song)
#         if link:
#             webbrowser.open(link)
#         else:
#             speak("Sorry, I couldn't find that song.")
#     elif "news" in c.lower():
#         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
#         if r.status_code == 200:
#             data = r.json()
#             articles = data.get('articles', [])
#             for article in articles[:5]:  # read only top 5 headlines
#                 speak(article['title'])
#     else:
#         output = aiProcess(c)
#         speak(output)

# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         try:
#             print("recognizing...")
#             with sr.Microphone(device_index=5) as source:  # change index if needed
#                 recognizer.adjust_for_ambient_noise(source, duration=1)
#                 print("Listening...")
#                 audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

#             word = recognizer.recognize_google(audio)
#             if word.lower() == "jarvis":
#                 speak("Ya")
#                 with sr.Microphone(device_index=5) as source:
#                     recognizer.adjust_for_ambient_noise(source, duration=1)
#                     print("Jarvis Active...")
#                     audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#                     command = recognizer.recognize_google(audio)
#                     processCommand(command)

#         except Exception as e:
#             print(f"Error: {e}")
