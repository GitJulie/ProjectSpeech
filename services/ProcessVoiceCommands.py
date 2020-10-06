from services.AudioFunctions import *
from services.BasicFunctions import *
from services.TextFunctions import *



def proccess_voice_commands(language, audio2, r):
    """
    Cette fonction traite notre requête orale et retourne le message vocal correspondant
    """
    if language == "fr-FR":
        if "vidéo" in r.recognize_google(audio2, language=language):
            open_url("youtube")
            vocal_message = "Voici votre site"
        elif "recherche" in r.recognize_google(audio2, language=language):
            text, message = transform_audio(audio2, language)
            vocal_message = search(language,text)
        elif "acheter" in r.recognize_google(audio2, language=language):
            open_url("amazon")
            vocal_message = "Voici votre site"
        elif "réseau" in r.recognize_google(audio2, language=language):
            open_url("facebook")
            vocal_message = "Voici votre site"
        elif "heure" in r.recognize_google(audio2, language=language):
            vocal_message = give_time()
        elif "écris" in r.recognize_google(audio2, language=language):
            text, message = transform_audio(audio2, language)
            print(message)
            speak(message)
            vocal_message = write_doc(text, language)
        else:
            vocal_message = "Je n'ai pas compris votre demande"
    else:
        if "youtube" in r.recognize_google(audio2, language=language):
            open_url("youtube")
            vocal_message = "Here's the website"
        elif "search" in r.recognize_google(audio2, language=language):
            vocal_message = search(language,audio2)
        elif "amazon" in r.recognize_google(audio2, language=language):
            open_url("amazon")
            vocal_message = "Here's the website"
        elif "facebook" in r.recognize_google(audio2, language=language):
            open_url("facebook")
            vocal_message = "Here's the website"
        elif "time" in r.recognize_google(audio2, language=language):
            vocal_message = give_time()
        elif "write" in r.recognize_google(audio2, language=language):
            text, written_message = transform_audio(audio2, language)
            print(written_message)
            speak(written_message)
            vocal_message = write_doc(text, language)
        else:
            vocal_message = "I didn't understand your request"
    return vocal_message
