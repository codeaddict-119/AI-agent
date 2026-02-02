import speech_recognition as sr
import os
import webbrowser
import datetime
from openai import OpenAI
import pyttsx3
import sys


from config import apikey # create a config.py and add you api key there

client = OpenAI(api_key=apikey)

# Text to Speech 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 for male 1 for female

def say(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=256
        )
        reply = response.choices[0].message.content
        
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        
        safe_name = "".join(x for x in prompt[:20] if x.isalnum())
        with open(f"Openai/{safe_name}.txt", "w") as f:
            f.write(f"Prompt: {prompt}\n\n{reply}")
        return reply
    except Exception as e:
        return "I am having trouble connecting to my servers."

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-US')
            print(f"user said: {query}")
            return query.lower()
        except Exception:
            return "none"

if __name__ == "__main__":
    say("System online")
    while True:
        query = takecommand()
        if query == "none":
            continue

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.org"],
            ["google", "https://www.google.com"],
            ["github", "https://www.github.com"],
            ["stack overflow", "https://stackoverflow.com"]
        ]

        matched_site = False
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                matched_site = True
                break
        
        if matched_site:
            continue

        if "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The time is {strTime}")

        # window app path here:
        elif "open camera" in query:
            os.system("start microsoft.windows.camera:")

        elif "open calculator" in query:
            os.system("calc")

        elif "open notepad" in query:
            os.system("notepad")


        elif "stop" in query or "exit" in query:
            say("Goodbye")
            sys.exit()

        else:
            response = ai(prompt=query)
            say(response)