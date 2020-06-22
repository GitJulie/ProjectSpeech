import webbrowser as wb
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


def open_url(name):
    return wb.get().open_new("https://www.{}.com \n".format(name))


def speak(message):
    """
    Cette fonction a pour but de lire à voix haute un message écrit
    """

    #On instancie SpeechConfig, AudioOutputConfig et SpeechSynthesizer
    speech_config = SpeechConfig(subscription="e380a1ef788a4b6d9d614c213728ffbc", region="francecentral")
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    return synthesizer.speak_text_async(message)



