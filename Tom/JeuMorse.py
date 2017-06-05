import random, sys, time, threading, shelve, smtplib
from tkinter import *

#_______________________________________________________________
fenetreJeu2 = Tk()
fenetreJeu2.title('Le Morse')
fenetreJeu2['bg'] = 'grey'                   #je cree une fenêtre en lui donnant un nom et un fond
fenetreJeu2.geometry('800x300+650+350')      #je place la fenêtre a l'ecran et je parametre sa taille
#_______________________________________________________________
def showScore():            #Fonction a venir qui permettra de voir les precedants scores
    pass

def reportf():              #Fonction qui permet d'envoyer le probleme qu'un utilisateur peut rencontrer vers une adresse mail de l'equipe de programmation
    reportf=Toplevel()
    reportf.configure(width=600, height=300)
    reportf.title('Reporter un bug')
    reportf.resizable(width=False, height=False)

    labelrepor1 = Label(reportf, text='E-mail :', font = 'Helvetica 15 bold')# on cree un label avec une police definie
    labelrepor1.place(x=0, y=0)# coordonnees du label
    emmailbox1 = StringVar()
    emmailbox1.set('@gmail.com')
    email1 = Entry(reportf, textvariable = emmailbox1, width=21, font='Helvetica 15 bold', justify=CENTER)
    email1.place(x=90, y=0)

    labelMDP = Label(reportf, text="Votre mot de passe d'email:", width=21, font='Helvetica 15 bold').place(x=0, y=100)
    motdepasse = StringVar()
    MDP = Entry(reportf, textvariable = motdepasse, width = 21, font='Helevetica 15 bold').place(x=280, y=100)

    labelreport2 = Label(reportf, text= "Indiquez de ce cote l'erreur rencontree:", font = 'Helvetica 15 bold').place(x=0, y=175)
    sujetext1 = StringVar()
    sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font='Helvetica 15 bold', justify=CENTER)
    sujet1.place(x=200, y=200)

    def ELRport():          #Sous-Fonction qui prend le texte, l'adresse mail et le mot de passe pour envoyer le probleme
                
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
        
def createurs():            #Ni plus ni moins que les credits du programme
    createurs = Toplevel()
    createurs.configure(width = 1666, height = 1666)
    createurs.title('Generique de Fin')
    createurs.resizable(False, False)
    createurs['bg'] = fenetreJeu2['bg']
    
    labelC1 = Label(createurs, text = 'Ce jeu vous a ete presente par ' + '\n' + 'Tom Habbar, Dylan Essakhi et Oscar Sellier.' + '\n' + "Avec l'aide supplementaire de Gawein Le Goff et de Erwan Castioni" + '\n' + "A l'occasion du bac d'ISN se deroulant au Lycee Camille Saint-Saens" + '\n' + "En esperant qu'il vous plaise ^^", font='Helvetica 15 bold', justify=CENTER)
    labelC1.pack()

#_______________________________________________________________
menubarre = Menu(fenetreJeu2)            #On va ici creer le menu du jeu

menu1 = Menu(menubarre, tearoff = 0)    #On cree un premier sous-menu qui ne se detache pas
menu1.add_command(label='Scores', command = showScore)
menu1.add_separator()                   #On ajoute un separateur
menu1.add_command(label='Quitter', command = fenetreJeu2.quit)
menubarre.add_cascade(label='Fichier', menu=menu1)      #On donne un nom au sous-menu cree

menu2 = Menu(menubarre, tearoff = 0)
menu2.add_command(label='A propos', command = createurs)
menu2.add_command(label='Reporter un bug', command=reportf)
menubarre.add_cascade(label='Aide', menu=menu2)

fenetreJeu2.config(menu=menubarre)

#_______________________________________________________________
Morse = {'A': '.-', 'B': '-...', 'C':'-.-.', 'D': '-..',                #On cree un tuple qui donne pour chaque caractere son equivalent en morse normal
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
Indication = Label(fenetreJeu2)
BonneRep = Label(fenetreJeu2)
MauvaiseRep = Label(fenetreJeu2)                #Ici se trouve toutes les variables qui vont être modifiees dans le programme 
compteurMot = 0
goodanswer = ''
Try = 3
zoneRep = Entry(fenetreJeu2)

labelMot = Label(fenetreJeu2)
zoneRep = Entry(fenetreJeu2)
labelVide2 = Label(fenetreJeu2)

prenom = Label(fenetreJeu2, text = "Indiquez votre nom ici", font='Helvetica 12 bold', justify=CENTER)
prenom.pack()
ValeurPrenom = StringVar()
EntreePrenom = Entry(fenetreJeu2, textvariable = ValeurPrenom, font='Helvetica 12 bold', justify=CENTER)    #On donne une zone de texte au joueur pour entrer son prenom
EntreePrenom.pack()

def AccepterRep(event):             #On cree une fonction qui va verifier la reponse du joueur
    global Indication, MauvaiseRep, BonneRep, zoneRep, labelMot, goodanswer, compteurMot, result, Try, answer, boutonSuivant, labelVide2
    if answer.get() != goodanswer and Try > 0:      #Si la reponse est incorrect mais qu'il reste encore plusieurs essais
        Indication.destroy()
        Try -= 1                    #On enleve 1 a la variable essai
        Indication = Label(fenetreJeu2, text = str(Try) + " essai(s) restant(s).", font='Helvetica 12 bold', justify=CENTER)    #On lui indique combien il lui en reste
        Indication.pack()
        answer.set('')              #On reinitialise sa reponse
    if answer.get() == goodanswer:  #Si la reponse est correcte
        Indication.destroy()        #On detruit les eventuelles indications qui seraient presentes
        result += 1                 #On ajoute 1 a son score
        BonneRep = Label(fenetreJeu2, text ="Bonne reponse!", font='Helvetica 12 bold', justify=CENTER)
        BonneRep.pack()
        labelVide2 = Label(fenetreJeu2, text = '\n', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu2['bg'])
        labelVide2.pack()
        labelMot.destroy()
        zoneRep.destroy()
        answer.set('')
        Try = 3             #On reinitialise le nombre d'essai apres avoir fini les essais ou d'avoir obtenu la bonne reponse
        boutonSuivant.pack()        #On place le bouton qui va passer au caractere suivant
    if Try == 0 and answer.get() != goodanswer:         #Si il n'y a plus d'essai possible et que la reponse est incorrecte
        Indication.destroy()
        MauvaiseRep = Label(fenetreJeu2, text = "La reponse etait " + goodanswer + "." + '\n', font='Helvetica 12 bold', justify=CENTER)  #On lui donne la bonne reponse
        MauvaiseRep.pack()
        labelVide2 = Label(fenetreJeu2, text = '\n', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu2['bg'])
        labelVide2.pack()
        labelMot.destroy()
        zoneRep.destroy()
        Try = 3             #On reinitialise le nombre d'essai apres avoir fini les essais ou d'avoir obtenu la bonne reponse
        answer.set('')
        boutonSuivant.pack()        #On place le bouton qui va passer au caractere suivant

def Game():             #On cree la fonction qui va lancer le jeu en question
    global compteurMot, goodanswer, BonneRep, MauvaiseRep, Indication, zoneRep, labelMot, number, boutonSuivant, labelVide2, label3, Morse

    if compteurMot != number.get():     #Avec une variable qu'on appelle compteurMot, on verifie qu'elle n'est pas egale au nombre choisi par le joueur pour lancer le jeu
        labelVide2.destroy()
        boutonSuivant.pack_forget()
        labelMot.destroy()
        zoneRep.destroy()
        Indication.destroy()
        MauvaiseRep.destroy()
        BonneRep.destroy()              #On supprime tous les labels et autres widgets pour ne pas avoir de redondances au niveau de l'affichage

        letter = random.randint(33,90)  #On lance le choix au hasard par l'ordinateur
        while (letter > 34 and letter < 39) or (letter > 41 and letter < 44) or (letter > 46 and letter < 48) or (letter > 59 and letter < 63) or (letter > 63 and letter < 65):
                letter = random.randint(33,90)      #On fait en sorte que, tant que le choix ne correspond pas a un des caracteres presents dans le tupple, il rechoisisse au hasard
                
        goodanswer = Morse[chr(letter).upper()]     #On indique que la bonne reponse est la valeur de la lettre dans le tupple
        compteurMot += 1    #On rajoute plus 1 au compteur de mot
        
        labelMot = Label(fenetreJeu2, text = chr(letter), font='Helvetica 12 bold', justify=CENTER)
        labelMot.pack()
        zoneRep = Entry(fenetreJeu2, textvariable = answer, font ='Helvetica 12 bold', justify=CENTER)
        zoneRep.pack()
        zoneRep.bind('<KeyPress-Return>', AccepterRep)  #Des que le joueur appuie sur Entree pour valider sa reponse, ça lance le programme de verification de la reponse

    elif compteurMot == number. get():      #Si le compteur de mot est egal au nombre choisi, le jeu s'arrête, tout s'efface et on affiche le score
        boutonSuivant.destroy()
        Indication.destroy()
        MauvaiseRep.destroy()
        BonneRep.destroy()
        labelMot.destroy()
        zoneRep.destroy()
        label3['text'] = "C'est fini!"
        labelFinal = Label(fenetreJeu2, text = ValeurPrenom.get() + ", vous avez "+ str(result) + " sur " + str(number.get()) + ".", font='Helvetica 12 bold', justify=CENTER)
        labelFinal.pack()

def Accepter(evnt):             #On cree une fonction qui va supprimer les textes inutiles et passer a la suite
        global prenom, EntreePrenom, label1, label2, EntreeNbr
        prenom.destroy()
        EntreePrenom.destroy()
        label1.pack()
        label2.pack()
        EntreeNbr.pack()

EntreePrenom.bind('<KeyPress-Return>', Accepter)        #Des que le joueur appuie sur Entree (Return pour le noma de la touche) tom

label1 = Label(fenetreJeu2, text ="Vous devez traduire une lettre, un chiffre ou un signe de ponctuation choisi au hasard en code Morse.", font='Helvetica 12 bold', justify=CENTER)
number = IntVar()
label2 = Label(fenetreJeu2, text ="Maintenant, selectionnez le nombre de caracteres a traduire", font='Helvetica 12 bold', justify=CENTER)      #On indique au joueur ce qu'il va devoir faire et on lui demande un nombre de carcteres a traduire
EntreeNbr = Entry(fenetreJeu2, textvariable = number, font='Helvetica 12 bold', justify=CENTER)

def Accepter_2(evnt):       #On cree une fonction qui verifie le nombre choisi en plaçant un minimum a 2
    global label1, label2, label3, EntreeNbr, labelVide
    if number.get() >= 2:
        label1.destroy()
        label2.destroy()
        EntreeNbr.destroy()
        label3.pack()
        labelVide.pack()
        Game()
    else:
        number.set('2')

label3 = Label(fenetreJeu2, text = "It's time to start!", font='Helvetica 12 bold', justify=CENTER)
labelVide = Label(fenetreJeu2, text = '\n', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu2['bg'])
EntreeNbr.bind('<KeyPress-Return>', Accepter_2)         #Des que le joueur valide avec Entree le nombre, cela lance la fonction qui verifie ce nombre

boutonSuivant = Button(fenetreJeu2, text = 'Suivant', command = Game, font='Helvetica 12 bold', justify=CENTER)         #Bouton qui va permettre de passer au mot suivant

fenetreJeu2.mainloop()
