from datetime import datetime


def write_doc(text):
    """
    Cette fonction a pour but d'écrire un texte dans un fichier .txt
    """
    fichier = open("Your_audio.txt", "w")
    voice_fichier = text
    fichier.write(voice_fichier)
    fichier.close()


def give_time():
    """
    Cette fonction a pour but de retourner l'heure actuelle
    """
    message = str(datetime.now())
    return message
