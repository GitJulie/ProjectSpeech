from services.WebsitesManagement import WebsitesManagement

from services.AudioFunctions import *
from services.BasicFunctions import *
from services.TextFunctions import *

import speech_recognition as sr


def main():
    # On instancie sr.Recognizer
    r = sr.Recognizer()

    # On indique le microphone comme source de notre audio
    with sr.Microphone() as source:
        print('Welcome to our ProjetSpeech, you can speak now')
        speak('Welcome to our ProjetSpeech, you can speak now')
        audio1 = r.listen(source)

    # On récupère la langue détectée dans language et on lit le message signifiant la mise à l'écoute
    language, message1 = recognize_language(audio1)
    print(message1)
    speak(message1)

    # On enregistre notre requête
    audio2 = r.listen(source)

    # On va détecter des mots-clés dans l'audio et agir en fonction
    if language == "fr-FR":
        if "youtube" in audio2:
            WebsitesManagement("youtube")
            message2 = "Voici votre site"
        elif "amazon" in audio2:
            WebsitesManagement("amazon")
            message2 = "Voici votre site"
        elif "facebook" in audio2:
            WebsitesManagement("facebook")
            message2 = "Voici votre site"
        elif "heure" in audio2:
            message2 = give_time()
        elif "écris" in audio2:
            text = transform_audio(audio2, language)
            message2 = write_doc(text, language)
        else:
            message2 = "Je n'ai pas compris votre demande"

    else:
        if "youtube" in audio2:
            WebsitesManagement("youtube")
            message2 = "Here's the website"
        elif "amazon" in audio2:
            WebsitesManagement("amazon")
            message2 = "Here's the website"
        elif "facebook" in audio2:
            WebsitesManagement("facebook")
            message2 = "Here's the website"
        elif "time" in audio2:
            message2 = give_time()
        elif "write" in audio2:
            text = transform_audio(audio2, language)
            message2 = write_doc(text, language)
        else:
            message2 = "I didn't understand your request"

    print(message2)
    speak(message2)


main()
