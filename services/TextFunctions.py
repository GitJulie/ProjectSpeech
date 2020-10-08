from datetime import *
from tkinter.filedialog import *
from tkinter import *
import speech_recognition as sr
from services.BasicFunctions import *


def modifier():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        audio3 = r1.listen(source)
    text = r1.recognize_google(audio3, language='fr-FR, en-EN')
    write_doc(text, language='fr-FR,en-EN')
    message="Votre texte a été modifié"
    print(message)
    speak(message)



def write_doc(text, language):
    """
    Cette fonction a pour but d'écrire un texte dans un fichier .txt
    """

    if language == "fr-FR" :
        text_split = text.split("écris")[-1]
    else :
        text_split = text.split("write")[-1]

    fichier = open("Your_audio.txt", "w")
    fichier.write(text_split)
    fichier.close()

    fenetre = Tk()
    fenetre.title("MON TEXTE")
    fenetre.geometry("480x260")

    bouton1 = Button(fenetre, text="quitter", bg="red", fg="black", command=fenetre.destroy, width=15, height=3)
    bouton2 = Button(fenetre, text="modifier", bg="blue", fg="white", command=modifier, width=15, height=3)
    bouton1.place(relx=.8, rely=.5, anchor="c")
    bouton2.place(relx=.8, rely=.2, anchor="c")

    canvas = Canvas(fenetre, width=250, height=420, background='grey')

    filename = askopenfilename(title="Ouvrir votre document", filetypes=[('txt files', '.txt'), ('all files', '.*')])
    fichier = open(filename, "r")
    content = fichier.read()
    fichier.close()

    Label(canvas, text=content).pack(padx=10, pady=10)

    canvas.pack(side=LEFT, padx=10, pady=10)

    fenetre.mainloop()

    if language == "fr-FR":
        message = "Votre message a bien été écrit et enregistré"
    else:
        message = "Your message was written and registered successfully"
    return message


def give_time():
    """
    Cette fonction a pour but de retourner l'heure actuelle
    """
    message = "Voici le jour et l'heure : " + str(datetime.now())
    return message
