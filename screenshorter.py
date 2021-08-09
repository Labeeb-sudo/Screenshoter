import pyttsx3
import speech_recognition as sr
import pyautogui

voice_engine = pyttsx3.init('sapi5')

voices = voice_engine.getProperty('voices') #getting details of current voice
# print(voices[1].id)
voice_engine.setProperty('voice', voices[0].id)

def speak(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query    
if __name__=="__main__":

    query = takeCommand().lower()

    if 'screenshot' in query:
        screenshot = pyautogui.screenshot()
        speak("ScreenShot captured sir")
        speak("Name sir")
        a = takeCommand()
        screenshot.save("C:\\Users\\Labeeb\\Desktop\\HTML\\" + a + '.jpg')
        speak("Screenshot has been saved to The HTML folder named" + a )
