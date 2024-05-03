import pywin32_testutil
import datetime
import speechRecognition as sr


engine=pywin32_testutil.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hey!! akanksha .please tell me how can i help you") 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listining")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing..")
        query=r.recognize_google(audio,Language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        #print(e)
        print("say that again please")
        return"none"    
if __name__=="__main__":
    wishMe()
    




       



