from services.WebsitesManagement import WebsitesManagement

from services.AudioFunctions import *
from services.BasicFunctions import *
from services.TextFunctions import *

import speech_recognition as sr


def main():
    #On instancie sr.Recognizer
    r = sr.Recognizer()

    #On indique le microphone comme source de notre audio
    with sr.Microphone() as source:
        print('Welcome to our ProjetSpeech, you can speak now')
        speak('Welcome to our ProjetSpeech, you can speak now')
        audio = r.listen(source)

    #On récupère la langue détectée dans language et on lit le message signifiant la mise à l'écoute
    language, message = recognize_language(audio)
    speak(message)



main()