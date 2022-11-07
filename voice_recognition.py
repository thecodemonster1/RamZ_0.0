import speech_recognition as sr
import pyttsx3 as pyttsx

speech_engine = pyttsx.init()  # 'sapi5' see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)


def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()


recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_sphinx(audio)
        # speak("I am running now")
        # or: return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Recog Error; {0}".format(e))

    return "Hello"


speak("I heard you say " + listen())
