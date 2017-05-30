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
        global ValeurPrenom, prenom, EntreePrenom
        ValPrenom = ValeurPrenom.get()
        prenom.destroy()
        EntreePrenom.destroy()

EntreePrenom.bind('<KeyPress-Return>', Accepter)

##        print("You'll have to translate a random letter, number or ponctuation mark into Morse code")
##        number = int(input("Now select the number of characters you want to translate -->	    "))
##        print("It's time to start!")
##        print("")
##
##        for loop in range(number):
##                letter = random.randint(33,90)
##                while (letter > 34 and letter < 39) or (letter > 41 and letter < 44) or (letter > 46 and letter < 48) or (letter > 59 and letter < 63) or (letter > 63 and letter < 65):
##                        letter = random.randint(33,90)
##                goodanswer = Morse[chr(letter).upper()]
##                Try = 3
##                
##                print(chr(letter))
##                
##                while answer != goodanswer and Try > 0:
##                        answer = input()
##                        if answer != goodanswer:
##                                Try += -1
##                                print(Try, "attempt left.")
##                if answer == goodanswer:
##                        result += 1
##                        print("Good answer")
##                        print("")
##                if Try == 0 and answer != goodanswer:
##                        print("The answer was", goodanswer, ".")
##                        print("")
##
##        print(prenom, "has", result, "over", number, ".")

if __name__ == '__main__':
        morse()
