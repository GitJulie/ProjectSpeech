from services.AudioFunctions import *
from services.BasicFunctions import *
from services.TextFunctions import *

import speech_recognition as sr


def main():
    # On instancie sr.Recognizer
    r = sr.Recognizer()

    # On enregistre notre première demande
    with sr.Microphone() as source:
        print('Welcome to our ProjectSpeech, you can speak now')
        speak('Welcome to our ProjectSpeech, you can speak now')
        audio1 = r.listen(source)

    # On récupère la langue détectée dans language et on lit le message signifiant la mise à l'écoute
    language, message1 = recognize_language(audio1)
    print(message1)
    speak(message1)

    # On enregistre notre requête
    with sr.Microphone() as source:
        audio2 = r.listen(source)

    # On va détecter des mots-clés dans l'audio et agir en fonction
    if language == "fr-FR":
        if "patate" in r.recognize_google(audio2, language=language):
            open_url("youtube")
            message2 = "Voici votre site"
        elif "amazon" in r.recognize_google(audio2, language=language):
            open_url("amazon")
            message2 = "Voici votre site"
        elif "facebook" in r.recognize_google(audio2, language=language):
            open_url("facebook")
            message2 = "Voici votre site"
        elif "heure" in r.recognize_google(audio2, language=language):
            message2 = give_time()
        elif "écris" in r.recognize_google(audio2, language=language):
            text, message = transform_audio(audio2, language)
            print(message)
            speak(message)
            message2 = write_doc(text, language)
        else:
            message2 = "Je n'ai pas compris votre demande"
    else:
        if "youtube" in r.recognize_google(audio2, language=language):
            open_url("youtube")
            message2 = "Here's the website"
        elif "amazon" in r.recognize_google(audio2, language=language):
            open_url("amazon")
            message2 = "Here's the website"
        elif "facebook" in r.recognize_google(audio2, language=language):
            open_url("facebook")
            message2 = "Here's the website"
        elif "time" in r.recognize_google(audio2, language=language):
            message2 = give_time()
        elif "write" in r.recognize_google(audio2, language=language):
            text, message = transform_audio(audio2, language)
            print(message1)
            speak(message1)
            message2 = write_doc(text, language)
        else:
            message2 = "I didn't understand your request"

    print(message2)
    speak(message2)


main()
