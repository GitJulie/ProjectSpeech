import speech_recognition as sr
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


def recognize_language(audio):
    """
    Cette fonction a pour but de reconnaître la langue utilisée et de mettre Voicee en mode écoute.
    :param audio: data_audio
    :return: language, message
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


def speak(message):
    """
    Cette fonction a pour but de lire à voix haute un message écrit
    :param message: text
    :return: oral text
    """

    #On instancie SpeechConfig, AudioOutputConfig et SpeechSynthesizer
    speech_config = SpeechConfig(subscription="e380a1ef788a4b6d9d614c213728ffbc", region="francecentral")
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    return synthesizer.speak_text_async(message)



