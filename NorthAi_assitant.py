import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


music={
   "winning":"https://youtu.be/vsWxs1tuwDk?si=wZm2jEzOZitN6U-K",
   "allah": "https://youtu.be/ri3NctAmkWE?si=E7XsMi0McoRqHIul",
   "soni":"https://youtu.be/GFljvZMZI0U?si=pZ3Dt6C5pco8ufAX",
   "aao":"https://youtu.be/Mo5tQDcs__g?si=QC6BWCkSOJGURxyf",
   "gangland":"https://youtu.be/QgHbp2c66FI?si=1ry-lbkKZdNej_It",
   "let's": "https://youtu.be/GeiBOC1Wc5U?si=lmJaoO26rmPMsoBo"
}
#speaking
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
#wishme functn
def wishMe():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour <=12:
    print("Good Morning")
    speak("Good Morning")
  elif hour>=12 and hour<=17:
    print("Good Afternoon")
    speak("Good Afternoon")
  else:
    print("Good Evening")
    speak("Good Evening")
  print("Hello! I am North an advanced AI robot designed to assist and engage with you in various ways.")     
  speak("Hello! I am  North an advanced AI robot designed to assist and engage with you in various ways.") 
  #speechrecognition functn 
def takeCommand():
#   It takes microphone input fromm user and returnstring output
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold=1
       audio=r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query  




if __name__=="__main__":
  wishMe()
  while True:
    query=takeCommand().lower()

    #Logic for executing tasks based on query
    if 'wikipedia' in query:
       speak('Searching Wikipedia....')
       query=query.replace("wikipedia","")
       results=wikipedia.summary(query,sentences=2)
       speak("According to Wikipedia")
       print(results)
       speak(results)
    #opening yt
    elif 'open youtube' in query:
       print("opening opening...")
       speak("opening youtube")
       webbrowser.open("youtube.com")
    elif 'open instagram' in query: #opening insta
       print("opening Instagram...")
       speak("opening Instagram")
       webbrowser.open("instagram.com")
    elif 'open google' in query: 
       print("opening google")#opening google
       speak("opening google")
       webbrowser.open("google.com")
    elif 'the time' in query:
       strTime=datetime.datetime.now().strftime("%H:%H:%S")
       print(strTime)
       speak(f"The time is {strTime}")#time
    
    elif 'open code' in query:#opening vs code
       
       codepath ="C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
       os.startfile(codepath)
    elif 'shut up' in query:#quiting
       print("hope i have helped you")
       speak("hope i have helped you")
       quit()
    elif'play'in query:
       song=query.lower().split(" ")[2]
       link=music[song]
       webbrowser.open(link)
    else:
       print("I am very sorry.... I am unable to hear u or this feature is not available in this version")
       speak("I am very sorry....I am unable to hear u or this feature is not available in this version")