import pyttsx3 as pyttsx

speech_engine = pyttsx.init()  # 'sapi5' see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 175)


def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()


speak("Say something!, Amhar")
# speak("I am running now")
# speak("I have an error")
speak("I heard you say...  Assalaamu alaikkum, Amhar azwar")
