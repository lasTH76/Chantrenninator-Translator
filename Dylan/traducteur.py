import os, random, sys, time, threading, shelve, smtplib
from tkinter import *

#os.chdir('C:\Python34')

def SearchPath():                                       #je cree une fonction qui me permet de trouver un dossier dans n'importe quel fichier
    if getattr(sys, 'frozen', False):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.dirname(__file__)
    return datadir

#--------------------------------------------------------------

chemin = SearchPath()

fA = open(os.path.join(chemin, 'VocaAnglais.txt'), 'r')             #je lui demande d'ouvrir le fichier .txt en faisant en sorte qu'il le retrouve avant de le lire
fF = open(os.path.join(chemin, 'VocaFrancais.txt'), 'r')

listfF = [line.split('/n') for line in fF.readlines()]              #je lui demande de creer une liste a chaque fois qu'il y a un saut de ligne dans le fichier .txt
listfA = [line.split('/n') for line in fA.readlines()]

#---------------------------------------------------------------
fenetreJeu = Toplevel()
fenetreJeu.title('Jeu de traduction')
fenetreJeu['bg'] = 'grey'                   #je cree une fenêtre en lui donnant un nom et un fond
fenetreJeu.geometry('500x500+750+350')      #je place la fenêtre a l'ecran et je parametre sa taille

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
    createurs['bg'] = fenetreJeu['bg']
    
    labelC1 = Label(createurs, text = 'Ce jeu vous a ete presente par ' + '\n' + 'Tom Habbar, Dylan Essakhi et Oscar Sellier.' + '\n' + "Avec l'aide supplementaire de Gawein Le Goff et de Erwan Castioni" + '\n' + "A l'occasion du bac d'ISN se deroulant au Lycee Camille Saint-Saens" + '\n' + "En esperant qu'il vous plaise ^^", font='Helvetica 15 bold', justify=CENTER)
    labelC1.pack()

#_______________________________________________________________
menubarre = Menu(fenetreJeu)            #On va ici creer le menu du jeu

menu1 = Menu(menubarre, tearoff = 0)
menu1.add_command(label='Scores', command = showScore)
menu1.add_separator()
menu1.add_command(label='Quitter', command = fenetreJeu.quit)
menubarre.add_cascade(label='Fichier', menu=menu1)

menu2 = Menu(menubarre, tearoff = 0)
menu2.add_command(label='A propos', command = createurs)
menu2.add_command(label='Reporter un bug', command=reportf)
menubarre.add_cascade(label='Aide', menu=menu2)

fenetreJeu.config(menu=menubarre)

#_______________________________________________________________
nbMot = IntVar()                        #ici se trouve toutes les variables dont j'aurais besoin par la suite
score = 1
nbrEssai = 4
ReponseJoueur = StringVar()
actAn = 0
actFr = 0
labelMot = Label(fenetreJeu)
labelIndic = Label(fenetreJeu)
EntreeRep = Entry(fenetreJeu)
BoutonAccRep = Button(fenetreJeu)
compteurMot = 0
label3 = Label(fenetreJeu)
labelVide2 = Label(fenetreJeu)

def repareMot(mot):                     #Cette fonction permet d'extraire le mot de la liste venant des fichiers .txt
    listeNouvMot = []                   #On cree d'abord une liste vide
    ignoreSuivant = False
    for indLettre in range(len(mot)):   #Pour chaque caractere contenu dans un mot, on lui demande:
            if ignoreSuivant:
                    ignoreSuivant = False   #S'il n'y a rien a faire, de passer.
                    pass
            elif (mot[indLettre] in ("[", "]", "'")):   #S'il y a un de ces caracteres, de passer aussi et de ne pas l'inclure dans un mot
                    pass
            elif mot[indLettre] == chr(92) and mot[indLettre + 1] == "n":   #Si le n et le separateur \ sont presents, de passer en ignorant ces deux caracteres combines
                    ignoreSuivant = True
                    pass
            else:                       #Sinon, la fonction applique a la liste vide chaque lettre qu'il va separer par des guillemets quand il y aura un saut de ligne
                    listeNouvMot.append(mot[indLettre])
    nouveauMot = "".join(listeNouvMot)
    nouveauMot.replace("\n", "")
    if nouveauMot.endswith("\n"):
            vraiMot = nouveauMot[:-1] #On enleve le dernier caractere (= saut de ligne) pour eviter les sauts de lignes inutiles
    else:
            vraiMot = nouveauMot
    return vraiMot

label1 = Label(fenetreJeu, text='Bienvenue dans ce jeu de traduction mon jeune ami.' + '\n' + "Comment t'appelles-tu? ", font='Helvetica 12 bold', justify=CENTER) #On cree" un premier label (=texte sous Tkinter) avec une police d'ecriture et un placement defini
label1.pack()       #On place ce premier label

valueName = StringVar()     #On indique que la variable valueName est une zone d'entree de texte
prenom = Entry(fenetreJeu, textvariable = valueName, font='Helvetica 12 bold', justify=CENTER)  #On cree une zone pour ecrire dans la variable valueName
prenom.pack()

def entrer():       #on cree une fonction qui sert juste a supprimer les trois zones de texte, variable ou fixe.
    global label1, prenom, bouton1
    prenom.destroy()
    label1.destroy()
    bouton1.destroy()

def nbDeMot(evnt):          #On cree une seconde fonction qui va changer le texte affiche et demande le nombre de mots a traduire
    label1 = Label(fenetreJeu, text = 'Tres bien ' + valueName.get() + '.', font='Helvetica 12 bold', justify=CENTER)
    label1.pack()
    labelNbrMot = Label(fenetreJeu, text= 'Indiquez le nombre de mots a traduire (Minimum 5).', font='Helvetica 12 bold', justify=CENTER)
    labelNbrMot.pack()
    nbrMot = Entry(fenetreJeu, textvariable = nbMot, font='Helvetica 12 bold', justify=CENTER)
    nbrMot.pack()

    def entrer2():          #On cree une sous-fonction qui va servir a verifier si le nombre choisi est superieur ou non a 5
            global nbMot, label2, boutonFr, boutonAn
            if nbMot.get() >= 5:
                    label1.destroy()
                    labelNbrMot.destroy()
                    nbrMot.destroy()
                    bouton2.destroy()
                    nbMot = nbMot.get()
                    label3 = Label(fenetreJeu, text='Tu vas maintenant avoir ' + str(nbMot) +' mots a traduire.' + '\n' + "Fais attention, il n'y a pas d'accent.", font='Helvetica 12 bold', justify=CENTER)
                    label3.pack()
                    label2 = Label(fenetreJeu, text='Maintenant, dans quelle langue veux-tu jouer?', font='Helvetica 12 bold', justify=CENTER)
                    label2.pack()
                    boutonFr.pack(side=LEFT, expand = True)
                    boutonAn.pack(side=RIGHT, expand = True)
            else:
                    nbMot.set('5')
    bouton2 = Button(fenetreJeu, text='Entrer', command = entrer2, font='Helvetica 12 bold', justify=CENTER)
    bouton2.pack()

bouton1 = Button(fenetreJeu,text = 'Entrer', command = entrer, font='Helvetica 12 bold', justify=CENTER)
bouton1.pack()
bouton1.bind('<Destroy>', nbDeMot)          #Des que le bouton 1 est detruit, on appelle la fonction nbDeMot


def Francais():             #Cette fonction sert a changer le texte du label2 puis de lancer le jeu pour le mode français
    global boutonFr, boutonAn, label2, actFr
    boutonFr.destroy()
    boutonAn.destroy()
    actFr = 1             #Cette variable sert a savoir quel bouton le joueur a presse, en l'occurence le bouton FR. 
    label2['text'] ='Il faut les traduire en français'
    labelVide = Label(fenetreJeu, text = '', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu['bg'])
    labelVide.pack()
    Game()

def Anglais():              #Même chose que pour la fonction au-dessus, mais pour l'anglais
    global boutonFr, boutonAn, label2, actAn
    boutonFr.destroy()
    boutonAn.destroy()
    actAn = 1
    label2['text']='Il faut les traduire en anglais'
    labelVide = Label(fenetreJeu, text = '', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu['bg'])
    labelVide.pack()
    Game()

def Game():
    global nbMot, actAn, actFr, labelMot, EntreeRep, nbMot, valueName, score, compteurMot, label2, label3
    def Accept(event):      #Cette fonction sert a verifier la reponse du joueur et d'agir en consequence
        global ReponseJoueur, score, nbrEssai, labelIndic, labelVide2
        if ReponseJoueur.get() != reponse:          #Si le joueur donne une mauvaise reponse, on lui dit combien d'essai il lui reste.
            labelIndic.destroy()
            labelVide2.destroy()
            labelIndic = Label(fenetreJeu, text='Il te reste ' + str(nbrEssai) + ' essais.', font = 'Helvetica 12 bold', justify=CENTER)
            labelIndic.pack()
            ReponseJoueur.set('')
            nbrEssai -= 1
        if ReponseJoueur.get() == reponse and nbrEssai > 0:         #S'il donne une bonne reponse, on le lui indique et on passe au mot suivant en reinitialisant la zone de reponse.
            labelIndic.destroy()
            labelVide2.destroy()
            score += 1
            labelIndic = Label(fenetreJeu, text= 'Ceci est la bonne reponse!', font = 'Helvetica 12 bold', justify=CENTER)
            labelIndic.pack()
            labelVide2 = Label(fenetreJeu, text = '\n', font = 'Helvetica 12 bold', justify = CENTER, bg = fenetreJeu['bg'])
            labelVide2.pack()
            ReponseJoueur.set('')
            nbrEssai = 4
            Game()
        if nbrEssai == -1 and ReponseJoueur.get() != reponse:       #S'il s'est trompe, on lui indique la bonne reponse et on passe au mot suivant.
            labelIndic.destroy()
            labelVide2.destroy()
            labelIndic = Label(fenetreJeu, text= "La reponse etait '" + str(reponse) + "' .", font='Helvetica 12 bold', justify=CENTER)
            labelIndic.pack()
            labelVide2 = Label(fenetreJeu, text = '\n', font = 'Helvetica 12 bold', justify = CENTER, bg = fenetreJeu['bg'])
            labelVide2.pack()
            ReponseJoueur.set('')
            nbrEssai = 4
            Game()

    labelMot.destroy()
    EntreeRep.destroy()
    compteurMot += 1                #A chaque fois que la fonction est lancee, on ajoute plus 1 au compteur de mot fait.
    if actFr == 1 and nbMot!=compteurMot:           #Tant que le compteur est different du nombre de mot, on lance le jeu.
        hasard = random.randint(0, len(listfA))     #On choisit au hasard un nombre entre 0 et la longueur de la liste du fichier .txt
        mot = repareMot(listfA[hasard])             #On indique quel est le mot a traduire
        reponse = repareMot(listfF[hasard])         #La reponse est le mot repare contenu dans l'autre liste ayant le même nombre que le mot affiche
        reponse.lower()             #On met la reponse en minuscule au cas où
        labelMot = Label(fenetreJeu, text = mot, font='Helvetica 12 bold', justify=CENTER)      #On affiche le mot a traduire
        labelMot.pack()
        EntreeRep = Entry(fenetreJeu, textvariable= ReponseJoueur, font = 'Helvetica 12 bold', justify=CENTER)      #On indique la zone de texte où le joueur pourra repondre
        EntreeRep.pack()
        EntreeRep.bind('<KeyPress-Return>', Accept)     #A chaque fois que le joueur appuie sur le bouton Entree, on lance la fonction Accept
    if actAn == 1 and nbMot!=compteurMot:
        hasard = random.randint(0, len(listfA))
        mot = repareMot(listfF[hasard])
        reponse = repareMot(listfA[hasard])
        reponse.lower()
        labelMot = Label(fenetreJeu, text = mot, font='Helvetica 12 bold', justify=CENTER)
        labelMot.pack()
        EntreeRep = Entry(fenetreJeu, textvariable= ReponseJoueur, font = 'Helvetica 12 bold', justify=CENTER)
        EntreeRep.pack()
        EntreeRep.bind('<KeyPress-Return>', Accept)
    if nbMot == compteurMot:        #Si le compteur de mot est egale au nombre de mot choisi, le jeu efface tous les labels et autre zone de texte pour afficher le score.
        labelIndic.destroy()
        labelMot.destroy()
        EntreeRep.destroy()
        label2.destroy()
        label3.destroy()
        labelRep = Label(fenetreJeu, text = valueName.get() + ', vous avez un score de ' + str(score) + ' sur ' + str(nbMot), font = 'Helvetica 12 bold', justify=CENTER)
        labelRep.pack()

boutonFr = Button(fenetreJeu, text='Français', font='Helvetica 12 bold', command = Francais)
boutonAn = Button(fenetreJeu, text='Anglais', font='Helvetica 12 bold', command = Anglais)

boutonFr.bind('<Activate>', Game )          #Des que l'un des boutons est active, on lance le jeu une premiere fois
boutonAn.bind('<Activate>', Game )

fenetreJeu.mainloop()               #Sert a indiquer que c'est la fenêtre principal pour ce jeu.
fA.close()          #On ferme les differents fichiers .txt pour pouvoir les reutiliser quand on relance le jeu.
fF.close()
