from services.ProcessVoiceCommands import *
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
    language, activation_message = recognize_language(audio1)
    print(activation_message)
    speak(activation_message)

    # On enregistre notre requête
    with sr.Microphone() as source:
        audio2 = r.listen(source)
    request_message = proccess_voice_commands(language, audio2, r)
    print(request_message)
    speak(request_message)

main()


