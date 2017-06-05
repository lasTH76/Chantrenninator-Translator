import random, sys, time, threading, shelve, smtplib
from tkinter import *

#_______________________________________________________________
fenetreJeu2 = Tk()
fenetreJeu2.title('Le Morse')
fenetreJeu2['bg'] = 'grey'                   #je crée une fenêtre en lui donnant un nom et un fond
fenetreJeu2.geometry('800x300+650+350')      #je place la fenêtre à l'écran et je paramètre sa taille
#_______________________________________________________________
def showScore():            #Fonction à venir qui permettra de voir les precédants scores
    pass

def reportf():              #Fonction qui permet d'envoyer le problème qu'un utilisateur peut rencontrer vers une adresse mail de l'équipe de programmation
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

    def ELRport():          #Sous-Fonction qui prend le texte, l'adresse mail et le mot de passe pour envoyer le problème
                
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
        
def créateurs():            #Ni plus ni moins que les crédits du programme
    createurs = Toplevel()
    createurs.configure(width = 1666, height = 1666)
    createurs.title('Générique de Fin')
    createurs.resizable(False, False)
    createurs['bg'] = fenetreJeu2['bg']
    
    labelC1 = Label(createurs, text = 'Ce jeu vous a été présenté par ' + '\n' + 'Tom Habbar, Dylan Essakhi et Oscar Sellier.' + '\n' + "Avec l'aide supplémentaire de Gawein Le Goff et de Erwan Castioni" + '\n' + "A l'occasion du bac d'ISN se déroulant au Lycée Camille Saint-Saens" + '\n' + "En espérant qu'il vous plaise ^^", font='Helvetica 15 bold', justify=CENTER)
    labelC1.pack()

#_______________________________________________________________
menubarre = Menu(fenetreJeu2)            #On va ici créer le menu du jeu

menu1 = Menu(menubarre, tearoff = 0)    #On crée un premier sous-menu qui ne se détache pas
menu1.add_command(label='Scores', command = showScore)
menu1.add_separator()                   #On ajoute un séparateur
menu1.add_command(label='Quitter', command = fenetreJeu2.quit)
menubarre.add_cascade(label='Fichier', menu=menu1)      #On donne un nom au sous-menu créé

menu2 = Menu(menubarre, tearoff = 0)
menu2.add_command(label='A propos', command = créateurs)
menu2.add_command(label='Reporter un bug', command=reportf)
menubarre.add_cascade(label='Aide', menu=menu2)

fenetreJeu2.config(menu=menubarre)

#_______________________________________________________________
Morse = {'A': '.-', 'B': '-...', 'C':'-.-.', 'D': '-..',                #On crée un tuple qui donne pour chaque caractère son équivalent en morse normal
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
MauvaiseRep = Label(fenetreJeu2)                #Ici se trouve toutes les variables qui vont être modifiées dans le programme 
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
EntreePrenom = Entry(fenetreJeu2, textvariable = ValeurPrenom, font='Helvetica 12 bold', justify=CENTER)    #On donne une zone de texte au joueur pour entrer son prénom
EntreePrenom.pack()

def Accepter(evnt):             #On crée une fonction qui va supprimer les textes inutiles et passer à la suite
        global prenom, EntreePrenom, label1, label2, EntreeNbr
        prenom.destroy()
        EntreePrenom.destroy()
        label1.pack()
        label2.pack()
        EntreeNbr.pack()

EntreePrenom.bind('<KeyPress-Return>', Accepter)        #Dès que le joueur appuie sur Entrée (Return pour le nom de la touche) tom

label1 = Label(fenetreJeu2, text ="Vous devez traduire une lettre, un chiffre ou un signe de ponctuation choisi au hasard en code Morse.", font='Helvetica 12 bold', justify=CENTER)
number = IntVar()
label2 = Label(fenetreJeu2, text ="Maintenant, sélectionnez le nombre de caractères à traduire", font='Helvetica 12 bold', justify=CENTER)      #On indique au joueur ce qu'il va devoir faire et on lui demande un nombre de carctères à traduire
EntreeNbr = Entry(fenetreJeu2, textvariable = number, font='Helvetica 12 bold', justify=CENTER)

def Accepter_2(evnt):       #On crée une fonction qui vérifie le nombre choisi en plaçant un minimum à 2
    global label1, label2, label3, EntreeNbr
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
EntreeNbr.bind('<KeyPress-Return>', Accepter_2)         #Dès que le joueur valide avec Entrée le nombre, cela lance la fonction qui vérifie ce nombre

def AccepterRep(event):             #On crée une fonction qui va vérifier la réponse du joueur
    global Indication, MauvaiseRep, BonneRep, zoneRep, labelMot, goodanswer, compteurMot, result, Try, answer, boutonSuivant, labelVide2
    if answer.get() != goodanswer and Try > 0:      #Si la réponse est incorrect mais qu'il reste encore plusieurs essais
        Indication.destroy()
        Try -= 1                    #On enlève 1 à la variable essai
        Indication = Label(fenetreJeu2, text = str(Try) + " essai(s) restant(s).", font='Helvetica 12 bold', justify=CENTER)    #On lui indique combien il lui en reste
        Indication.pack()
        answer.set('')              #On réinitialise sa réponse
    if answer.get() == goodanswer:  #Si la réponse est correcte
        Indication.destroy()        #On détruit les éventuelles indications qui seraient présentes
        result += 1                 #On ajoute 1 à son score
        BonneRep = Label(fenetreJeu2, text ="Bonne réponse!", font='Helvetica 12 bold', justify=CENTER)
        BonneRep.pack()
        labelVide2 = Label(fenetreJeu2, text = '\n', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu2['bg'])
        labelVide2.pack()
        labelMot.destroy()
        zoneRep.destroy()
        answer.set('')
        Try = 3             #On réinitialise le nombre d'essai après avoir fini les essais ou d'avoir obtenu la bonne réponse
        boutonSuivant.pack()        #On place le bouton qui va passer au caractère suivant
    if Try == 0 and answer.get() != goodanswer:         #Si il n'y a plus d'essai possible et que la réponse est incorrecte
        Indication.destroy()
        MauvaiseRep = Label(fenetreJeu2, text = "La réponse était " + goodanswer + "." + '\n', font='Helvetica 12 bold', justify=CENTER)  #On lui donne la bonne réponse
        MauvaiseRep.pack()
        labelVide2 = Label(fenetreJeu2, text = '\n', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu2['bg'])
        labelVide2.pack()
        labelMot.destroy()
        zoneRep.destroy()
        Try = 3             #On réinitialise le nombre d'essai après avoir fini les essais ou d'avoir obtenu la bonne réponse
        answer.set('')
        boutonSuivant.pack()        #On place le bouton qui va passer au caractère suivant

def Game():             #On crée la fonction qui va lancer le jeu en question
    global compteurMot, goodanswer, BonneRep, MauvaiseRep, Indication, zoneRep, labelMot, number, boutonSuivant, labelVide2, label3

    if compteurMot != number.get():     #Avec une variable qu'on appelle compteurMot, on vérifie qu'elle n'est pas égale au nombre choisi par le joueur pour lancer le jeu
        labelVide2.destroy()
        boutonSuivant.pack_forget()
        labelMot.destroy()
        zoneRep.destroy()
        Indication.destroy()
        MauvaiseRep.destroy()
        BonneRep.destroy()              #On supprime tous les labels et autres widgets pour ne pas avoir de redondances au niveau de l'affichage

        letter = random.randint(33,90)  #On lance le choix au hasard par l'ordinateur
        while (letter > 34 and letter < 39) or (letter > 41 and letter < 44) or (letter > 46 and letter < 48) or (letter > 59 and letter < 63) or (letter > 63 and letter < 65):
                letter = random.randint(33,90)      #On fait en sorte que, tant que le choix ne correspond pas à un des caractères présents dans le tupple, il rechoisisse au hasard
                
        goodanswer = Morse[chr(letter).upper()]     #On indique que la bonne réponse est la valeur de la lettre dans le tupple
        compteurMot += 1    #On rajoute plus 1 au compteur de mot
        
        labelMot = Label(fenetreJeu2, text = chr(letter), font='Helvetica 12 bold', justify=CENTER)
        labelMot.pack()
        zoneRep = Entry(fenetreJeu2, textvariable = answer, font ='Helvetica 12 bold', justify=CENTER)
        zoneRep.pack()
        zoneRep.bind('<KeyPress-Return>', AccepterRep)  #Dès que le joueur appuie sur Entrée pour valider sa réponse, ça lance le programme de vérification de la réponse

    elif compteurMot == number. get():      #Si le compteur de mot est égal au nombre choisi, le jeu s'arrête, tout s'efface et on affiche le score
        boutonSuivant.destroy()
        Indication.destroy()
        MauvaiseRep.destroy()
        BonneRep.destroy()
        labelMot.destroy()
        zoneRep.destroy()
        label3['text'] = "C'est fini!"
        labelFinal = Label(fenetreJeu2, text = ValeurPrenom.get() + ", vous avez "+ str(result) + " sur " + str(number.get()) + ".", font='Helvetica 12 bold', justify=CENTER)
        labelFinal.pack()

boutonSuivant = Button(fenetreJeu2, text = 'Suivant', command = Game, font='Helvetica 12 bold', justify=CENTER)         #Bouton qui va permettre de passer au mot suivant

fenetreJeu2.mainloop()
