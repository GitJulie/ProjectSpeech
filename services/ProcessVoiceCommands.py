from services.AudioFunctions import *
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
            i = 0
        elif check_commands("réseau").name in r.recognize_google(audio2, language=language):
            open_url(check_commands("réseau").command_url)
            vocal_message = "Voici votre site"
            i = 0
        elif check_commands("vidéo").name in r.recognize_google(audio2, language=language):
            open_url(check_commands("vidéo").command_url)
            vocal_message = "Voici votre site"
            i = 0
        elif "recherche" in r.recognize_google(audio2, language=language):
            text, message = transform_audio(audio2, language)
            vocal_message = search(language,text)
            i = 0
        elif "heure" in r.recognize_google(audio2, language=language):
             vocal_message = give_time()
             i = 0
        elif "écris" in r.recognize_google(audio2, language=language):
             text, message = transform_audio(audio2, language)
             print(message)
             speak(message)
             vocal_message = write_doc(text, language)
             i = 0
        elif "au revoir" in r.recognize_google(audio2, language=language):
             vocal_message = "Au revoir"
             i = 1
        else:
             vocal_message = "Je n'ai pas compris votre demande"
             i = 0
    else:
        if "youtube" in r.recognize_google(audio2, language=language):
            open_url("https://www.youtube.com/")
            vocal_message = "Here's the website"
            i = 0
        elif "amazon" in r.recognize_google(audio2, language=language):
            open_url("https://www.amazon.fr/")
            vocal_message = "Here's the website"
            i = 0
        elif "facebook" in r.recognize_google(audio2, language=language):
            open_url("https://www.facebook.com/")
            vocal_message = "Here's the website"
            i = 0
        elif "search" in r.recognize_google(audio2, language=language):
            vocal_message = search(language,audio2)
            i = 0
        elif "time" in r.recognize_google(audio2, language=language):
            vocal_message = give_time()
            i = 0
        elif "write" in r.recognize_google(audio2, language=language):
            text, written_message = transform_audio(audio2, language)
            print(written_message)
            speak(written_message)
            vocal_message = write_doc(text, language)
            i = 0
        elif "bye" in r.recognize_google(audio2, language=language):
            vocal_message = "Bye"
            i = 1
        else:
            vocal_message = "I didn't understand your request"
            i = 0
    return vocal_message, i
