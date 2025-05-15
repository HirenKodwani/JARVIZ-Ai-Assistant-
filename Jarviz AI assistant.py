#Jarviz Project AI Chatbot

import speech_recognition as sr#Liabrary for Speech Recognition from audio input
import webbrowser
import pyttsx3#for giving output as an Audio
import requests
from openai import OpenAI


recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):#Function to Invoke Speaking Liabrary
   ttsx.say(text)
   ttsx.runAndWait()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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"
)

def aiProcess(command):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are Jarvis, an intelligent assistant."},
                {"role": "user", "content": command}
            ]
        )
        reply = response.choices[0].message.content
        print(reply)
        speak(reply)
        return reply
    except Exception as e:
        speak("Sorry sir, there was an error while processing your request.")
        print("Error:", e)
        return "Error: " + str(e)
   
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Of course Sir Here You GO...") 
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Of course Sir Here You GO...") 
    elif "open music"in c.lower():
        webbrowser.open("https://open.spotify.com/track/3YZUdbRzjjSn4i8ADgCObA?si=da1968ed882f4e8b")
        speak("Of course Sir Here You GO...") 
    elif "open youtube" in c.lower() or "entertain me" in c.lower(): 
        webbrowser.open("https://youtube.com")
        speak("Of course Sir Here You GO...") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Of course Sir Here You GO...") 
    elif"what is going on in US market"in c.lower(): 
        webbrowser.open("https://finviz.com/")
        speak("Lets go Trading...")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={"7da57610a08d442b8e3531a4f5dbce61"}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    elif "open camera"in c.lower():
        webbrowser.open("https://webcammictest.com/")
        speak("Opening Web Cam")
        
    elif"who made you"in c.lower() or "tell me about yourself" in c.lower(): 
        speak("I am an artificial Intelegence , I was made by mr. Hee rain Koodwani.  sir made me by througholy wrighting my code base ")
    else:
        aiProcess(c)  #  fallback to AI processing if no command matched
    
         
print("Hello Hee rain Sir, I am Your Artificial Intelegence... ")
      
speak("Hello Hee rain Sir, I am Your Artificial Intelegence... ")


while True:#Invoking Wake word which will start listining the commands
    r=sr.Recognizer()
    
    
    print("Recognising...")
    try:
        with sr.Microphone() as source:
           print("Listning sir...")
           audio = r.listen(source,timeout=5,phrase_time_limit=4)
        word = r.recognize_google(audio)
        print(word)
        if (word.lower()=="jarvis"):
            speak("Yes Sir...How may I Help You") #Giving back answer
            #Listinig Main Command
            with sr.Microphone() as source:
                speak("Active Sir")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                
                processCommand(command)
                
    except sr.UnknownValueError:
        print("Could not Understand Audio")
        speak("Could not Understand sir, Can you please repeat")
      
    except sr.RequestError as e:
        print("Error ;{0}".format(e))
        
