import pyttsx3
import speech_recognition as sr
import wikipedia 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def ask(audio):
        engine.say(audio)
        engine.runAndWait()
def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                ask("listening...")
                audio = r.listen(source)
        try:
                q = r.recognize_google(audio,language='en-in')    
        except:
                ask("say again")      
                return "None"
        return q

while True:
        query = takecommand().lower()
        
        if "hello" in query:
                ask("Hello")    
            
        elif query in query:
                
                result2 = wikipedia.summary(query,sentences = 4)  
                print(result2)
                ask(result2) 
       