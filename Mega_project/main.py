import speech_recognition as sr
import webbrowser
import pyttsx3

#pip install pocketsphinx

recognizer= sr.Recognizer()
ttsx= pyttsx3
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("initializing jarvis.......")
    while True:
        r = sr.Recognizer()
        # with sr.Microphone() as source:
        #  print("Say something!")
        #  audio = r.listen(source,timeout=2 , phrase_time_limit=1)
        print("recognizing......")
        try:
            with sr.Microphone() as source:
               print("Say something!")
               audio = r.listen(source,timeout=2 , phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yeah")
                # listen for command
                with sr.Microphone() as source:
                  print("Say something!")
                  audio = r.listen(source)
                  command=r.recognize_google(audio)
                 
                 

            #  print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        #  except sr.UnknownValueError:
        #   print("Sphinx could not understand audio")
        except Exception as e:
            print("Sphinx error; {0}".format(e))


