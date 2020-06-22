import speech_recognition as sr


def recognize_language(audio):
    """
    Cette fonction a pour but de reconnaître la langue utilisée et de mettre Voicee en mode écoute.
    """

    # On instancie sr.Recognizer
    r = sr.Recognizer()

    if 'Salut Google' in r.recognize_google(audio, language="fr-FR"):
        language = "fr-FR"
        message = "Que puis-je faire pour vous ?"
    elif 'Hey Google' in r.recognize_google(audio, language="en-US"):
        language = "en-US"
        message = "What can I do for you ?"
    else:
        return print("The language has not been detected")

    return language, message


def record_audio(audio, language):
    """
    Cette fonction a pour but d'enregistrer un message vocal
    """

    # On instancie sr.Recognizer
    r = sr.Recognizer()

    voice_data = ''
    message = ''

    if language == "fr-FR":
        try:
            voice_data = r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            message = "Je n'ai pas compris votre demande"
        except sr.RequestError:
            message = "Votre demande est erronée"

    elif language == "en-US":
        try:
            voice_data = r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            message = "I didn't understand your request"
        except sr.RequestError:
            message = "Your request is incorrect"

    text = voice_data.lower()

    return text, message
