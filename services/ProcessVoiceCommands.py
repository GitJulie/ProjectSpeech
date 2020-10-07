from services.AudioFunctions import *
from services.BasicFunctions import *
from services.TextFunctions import *
from utils.db_access import *

def check_commands(command):
    records = db_access.get_records()
    for record in records:
        if record.name == command:
            return record


def proccess_voice_commands(language, audio2, r):
    """
    Cette fonction traite notre requête orale et retourne le message vocal correspondant
    """

    if language == "fr-FR":
        if check_commands("acheter").name in r.recognize_google(audio2, language=language):
            open_url(check_commands("acheter").command_url)
            vocal_message = "Voici votre site"
        elif check_commands("reseau").name in r.recognize_google(audio2, language=language):
            open_url(check_commands("reseau").command_url)
            vocal_message = "Voici votre site"
        elif check_commands("video").name in r.recognize_google(audio2, language=language):
            open_url(check_commands("video").command_url)
            vocal_message = "Voici votre site"
        elif "recherche" in r.recognize_google(audio2, language=language):
            text, message = transform_audio(audio2, language)
            vocal_message = search(language,text)
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
            open_url("https://www.youtube.com/")
            vocal_message = "Here's the website"
        elif "amazon" in r.recognize_google(audio2, language=language):
            open_url("https://www.amazon.fr/")
            vocal_message = "Here's the website"
        elif "facebook" in r.recognize_google(audio2, language=language):
            open_url("https://www.facebook.com/")
            vocal_message = "Here's the website"
        elif "search" in r.recognize_google(audio2, language=language):
            vocal_message = search(language,audio2)
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
