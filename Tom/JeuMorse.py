import random, sys, time, threading, shelve, smtplib
from tkinter import *

#_______________________________________________________________
fenetreJeu2 = Tk()
fenetreJeu2.title('Le Morse')
fenetreJeu2['bg'] = 'grey'
fenetreJeu2.geometry('500x500+750+350')
#_______________________________________________________________
def reportf():
    reportf=Toplevel()
    reportf.configure(width=600, height=300)
    reportf.title('Reporter un bug')
    reportf.resizable(width=False, height=False)

    labelrepor1 = Label(reportf, text='E-mail :', font = 'Helvetica 15 bold')# on crée un label avec une police définie
    labelrepor1.place(x=0, y=0)# coordonnées du label
    emmailbox1 = StringVar()
    emmailbox1.set('@gmail.com')
    email1 = Entry(reportf, textvariable = emmailbox1, width=21, font='Helvetica 15 bold', justify=CENTER)
    email1.place(x=90, y=0)

    labelMDP = Label(reportf, text="Votre mot de passe d'email:", width=21, font='Helvetica 15 bold').place(x=0, y=100)
    motdepasse = StringVar()
    MDP = Entry(reportf, textvariable = motdepasse, width = 21, font='Helevetica 15 bold').place(x=280, y=100)

    labelreport2 = Label(reportf, text= "Indiquez de ce coté l'erreur rencontrée:", font = 'Helvetica 15 bold').place(x=0, y=175)
    sujetext1 = StringVar()
    sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font='Helvetica 15 bold', justify=CENTER)
    sujet1.place(x=200, y=200)

    def ELRport():
                
        fromaddr = emmailbox1.get()
        toaddrs = 'thab3@orange.fr'
        msg = sujetext1.get()
        MDP = motdepasse.get()
                
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr , MDP)

        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        reportf.destroy()

    boutonEnvoi = Button(reportf, text = 'Envoyer le report', command = ELRport).place(x=250, y=250)
        
def créateurs():
    createurs = Toplevel()
    createurs.configure(width = 1666, height = 1666)
    createurs.title('Générique de Fin')
    createurs.resizable(False, False)
    createurs['bg'] = fenetreJeu['bg']
    
    labelC1 = Label(createurs, text = 'Ce jeu vous a été présenté par ' + '\n' + 'Tom Habbar, Dylan Essakhi et Oscar Sellier.' + '\n' + "Avec l'aide supplémentaire de Gawein Le Goff et de Erwan Castioni" + '\n' + "A l'occasion du bac d'ISN se déroulant au Lycée Camille Saint-Saens" + '\n' + "En espérant qu'il vous plaise ^^", font='Helvetica 15 bold', justify=CENTER)
    labelC1.pack()

#_______________________________________________________________
menubarre = Menu(fenetreJeu2)

menu1 = Menu(menubarre, tearoff = 0)
##        menu1.add_command(label='Scores', command = showScore)
menu1.add_separator()
menu1.add_command(label='Quitter', command = fenetreJeu2.quit)
menubarre.add_cascade(label='Fichier', menu=menu1)

menu2 = Menu(menubarre, tearoff = 0)
menu2.add_command(label='A propos', command = créateurs)
menu2.add_command(label='Reporter un bug', command=reportf)
menubarre.add_cascade(label='Aide', menu=menu2)

fenetreJeu2.config(menu=menubarre)

#_______________________________________________________________
Morse = {'A': '.-', 'B': '-...', 'C':'-.-.', 'D': '-..',
         'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..',
        
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
         
         '?': '..--..', '!': '-.-.--', '.': '.-.-.-',
         ';': '-.-.-.', ':': '---...', ',': '--..--',
         "'": '.----.', '-': '-....-', '(': '-.--.',
         ')': '-.--.-', '"': '.-..-.'
        }

answer = StringVar()
result = 0

prenom = Label(fenetreJeu2, text = "Indiquez votre nom ici", font='Helvetica 12 bold', justify=CENTER)
prenom.pack()
ValeurPrenom = StringVar()
EntreePrenom = Entry(fenetreJeu2, textvariable = ValeurPrenom, font='Helvetica 12 bold', justify=CENTER)
EntreePrenom.pack()

def Accepter(evnt):
        global ValeurPrenom, prenom, EntreePrenom, label1, label2, EntreeNbr
        ValPrenom = ValeurPrenom.get()
        prenom.destroy()
        EntreePrenom.destroy()
        label1.pack()
        label2.pack()
        EntreeNbr.pack()

EntreePrenom.bind('<KeyPress-Return>', Accepter)

label1 = Label(fenetreJeu2, text ="Vous devez traduire une lettre, un chiffre ou un signe de ponctuation choisi au hasard en code Morse.", font='Helvetica 12 bold', justify=CENTER)
number = IntVar()
label2 = Label(fenetreJeu2, text ="Maintenant, sélectionnez le nombre de caractères à traduire", font='Helvetica 12 bold', justify=CENTER)
EntreeNbr = Entry(fenetreJeu2, textvariable = number, font='Helvetica 12 bold', justify=CENTER)

def Accepter_2(evnt):
    global label1, label2, label3, EntreeNbr
    label1.destroy()
    label2.destroy()
    EntreeNbr.destroy()
    label3.pack()

label3 = Label(fenetreJeu2, text = "It's time to start!" + '\n', font='Helvetica 12 bold', justify=CENTER)
label3.bind('<KeyPress-Return>', Accepter_2)
nombre = number.get()

for loop in range(nombre):
        letter = random.randint(33,90)
        while (letter > 34 and letter < 39) or (letter > 41 and letter < 44) or (letter > 46 and letter < 48) or (letter > 59 and letter < 63) or (letter > 63 and letter < 65):
                letter = random.randint(33,90)
        goodanswer = Morse[chr(letter).upper()]
        Try = 3
        
        labelMot = Label(fenetreJeu2, text = chr(letter), font='Helvetica 12 bold', justify=CENTER)
        labelMot.pack()

        def AccpterRep(event):
            if answer != goodanswer and Try > 0:
                Indication.destroy()
                Try += -1
                Indication = Label(fenetreJeu2, text = Try + " essai(s) restant(s).", font='Helvetica 12 bold', justify=CENTER)
                Indication.pack()
            if answer.get() == goodanswer:
                    result += 1
                    BonneRep = Label(fenetreJeu2, text ="Bonne réponse!", font='Helvetica 12 bold', justify=CENTER)
                    BonneRep.pack()
            if Try == 0 and answer.get() != goodanswer:
                    MauvaiseRep = Label(fenetreJeu2, text = "La réponse était " + goodanswer + ".", font='Helvetica 12 bold', justify=CENTER)
                    MauvaiseRep.pack()
##        print(prenom, "has", result, "over", number, ".")
##
##if __name__ == '__main__':
##        morse()
