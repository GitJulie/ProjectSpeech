import webbrowser as wb
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


def open_url(name):
    return wb.get().open_new(format(name))

def search(langage, text):
    if langage == "fr-FR":
        search_term = text.split("recherche")[-1]
        url = f"https://google.com/search?q={search_term}"
        wb.get().open(url)
        message = "Voici votre recherche"
    else :
        search_term = text.split("search")[-1]
        url= f"https://google.com/search?q={search_term}"
        wb.get().open(url)
        message = "Here's your search"
    return message

def speak(message):
    """
    Cette fonction a pour but de lire à voix haute un message écrit
    """

    #On instancie SpeechConfig, AudioOutputConfig et SpeechSynthesizer
    speech_config = SpeechConfig(subscription="9427f08d0d5a47079d66f3459efe7e0f", region="francecentral")
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    return synthesizer.speak_text_async(message)



