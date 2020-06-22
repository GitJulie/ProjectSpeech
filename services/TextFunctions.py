from datetime import datetime


def write_doc(text):
    fichier = open("Your_audio.txt", "w")
    voice_fichier = text
    fichier.write(voice_fichier)
    fichier.close()


def give_time():
    message = str(datetime.now())
    return message
