import os, random, sys, time, threading, shelve, smtplib
from tkinter import *

#os.chdir('C:\Python34')

def SearchPath():                                       #je crée une fonction qui me permet de trouver un dossier dans n'importe quel fichier
    if getattr(sys, 'frozen', False):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.dirname(__file__)
    return datadir

#--------------------------------------------------------------

chemin = SearchPath()

fA = open(os.path.join(chemin, 'VocaAnglais.txt'), 'r')             #je lui demande d'ouvrir le fichier .txt en faisant en sorte qu'il le retrouve avant de le lire
fF = open(os.path.join(chemin, 'VocaFrancais.txt'), 'r')

listfF = [line.split('/n') for line in fF.readlines()]              #je lui demande de créer une liste à chaque fois qu'il y a un saut de ligne dans le fichier .txt
listfA = [line.split('/n') for line in fA.readlines()]

#---------------------------------------------------------------
fenetreJeu = Tk()
fenetreJeu.title('Jeu de traduction')
fenetreJeu['bg'] = 'grey'                   #je crée une fenêtre en lui donnant un nom et un fond
fenetreJeu.geometry('500x500+750+350')      #je place la fenêtre à l'écran et je paramètre sa taille

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
    createurs['bg'] = fenetreJeu['bg']
    
    labelC1 = Label(createurs, text = 'Ce jeu vous a été présenté par ' + '\n' + 'Tom Habbar, Dylan Essakhi et Oscar Sellier.' + '\n' + "Avec l'aide supplémentaire de Gawein Le Goff et de Erwan Castioni" + '\n' + "A l'occasion du bac d'ISN se déroulant au Lycée Camille Saint-Saens" + '\n' + "En espérant qu'il vous plaise ^^", font='Helvetica 15 bold', justify=CENTER)
    labelC1.pack()

#_______________________________________________________________
menubarre = Menu(fenetreJeu)            #On va ici créer le menu du jeu

menu1 = Menu(menubarre, tearoff = 0)
menu1.add_command(label='Scores', command = showScore)
menu1.add_separator()
menu1.add_command(label='Quitter', command = fenetreJeu.quit)
menubarre.add_cascade(label='Fichier', menu=menu1)

menu2 = Menu(menubarre, tearoff = 0)
menu2.add_command(label='A propos', command = créateurs)
menu2.add_command(label='Reporter un bug', command=reportf)
menubarre.add_cascade(label='Aide', menu=menu2)

fenetreJeu.config(menu=menubarre)

#_______________________________________________________________
nbMot = IntVar()
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

def repareMot(mot):
    listeNouvMot = []
    ignoreSuivant = False
    for indLettre in range(len(mot)):
            if ignoreSuivant:
                    ignoreSuivant = False
                    pass
            elif (mot[indLettre] in ("[", "]", "'")):
                    pass
            elif mot[indLettre] == chr(92) and mot[indLettre + 1] == "n":
                    ignoreSuivant = True
                    pass
            else:
                    listeNouvMot.append(mot[indLettre])
    nouveauMot = "".join(listeNouvMot)
    nouveauMot.replace("\n", "")
    if nouveauMot.endswith("\n"):
            vraiMot = nouveauMot[:-1] #On enleve le dernier caractere (= saut de ligne) pour eviter les sauts de lignes inutiles
    else:
            vraiMot = nouveauMot
    return vraiMot

label1 = Label(fenetreJeu, text='Bienvenue dans ce jeu de traduction mon jeune ami.' + '\n' + "Comment t'appelles-tu? ", font='Helvetica 12 bold', justify=CENTER)
label1.pack()

valueName = StringVar()
prenom = Entry(fenetreJeu, textvariable = valueName, font='Helvetica 12 bold', justify=CENTER)
prenom.pack()

def entrer():
    global label1, prenom, bouton1
    prenom.destroy()
    label1.destroy()
    bouton1.destroy()

def nbDeMot(evnt):
    label1 = Label(fenetreJeu, text = 'Très bien ' + valueName.get() + '.', font='Helvetica 12 bold', justify=CENTER)
    label1.pack()
    labelNbrMot = Label(fenetreJeu, text= 'Indiquez le nombre de mots à traduire (Minimum 5).', font='Helvetica 12 bold', justify=CENTER)
    labelNbrMot.pack()
    nbrMot = Entry(fenetreJeu, textvariable = nbMot, font='Helvetica 12 bold', justify=CENTER)
    nbrMot.pack()

    def entrer2():
            global nbMot, label2, boutonFr, boutonAn
            if nbMot.get() >= 5:
                    label1.destroy()
                    labelNbrMot.destroy()
                    nbrMot.destroy()
                    bouton2.destroy()
                    tempMot = nbMot.get()
                    nbMot = int(tempMot)
                    label3 = Label(fenetreJeu, text='Tu vas maintenant avoir ' + str(nbMot) +' mots à traduire.' + '\n' + "Fais attention, il n'y a pas d'accent.", font='Helvetica 12 bold', justify=CENTER)
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
bouton1.bind('<Destroy>', nbDeMot)


def Francais():
    global boutonFr, boutonAn, label2, actFr
    boutonFr.destroy()
    boutonAn.destroy()
    actFr = 1
    label2['text'] ='Il faut les traduire en français'
    labelVide = Label(fenetreJeu, text = '', font='Helvetica 12 bold', justify=CENTER, bg = fenetreJeu['bg'])
    labelVide.pack()
    Game()

def Anglais():
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
    def Accept(event):
        global ReponseJoueur, score, nbrEssai, labelIndic
        labelIndic.destroy()
        if ReponseJoueur.get() != reponse:
            labelIndic = Label(fenetreJeu, text='Il te reste ' + str(nbrEssai) + ' essais.', font = 'Helvetica 12 bold', justify=CENTER)
            labelIndic.pack()
            ReponseJoueur.set('')
            nbrEssai -= 1
        if ReponseJoueur.get() == reponse and nbrEssai > 0:
            score += 1
            labelIndic = Label(fenetreJeu, text= 'Ceci est la bonne réponse!', font = 'Helvetica 12 bold', justify=CENTER)
            labelIndic.pack()
            ReponseJoueur.set('')
            nbrEssai = 4
            time.sleep(0.5)
            labelIndic.destroy()
            Game()
        if nbrEssai == -1 and ReponseJoueur.get() != reponse:
            labelIndic.destroy()
            labelIndic = Label(fenetreJeu, text= "La reponse était '" + str(reponse) + "' .", font='Helvetica 12 bold', justify=CENTER)
            labelIndic.pack()
            ReponseJoueur.set('')
            nbrEssai = 4
            time.sleep(1)
            labelIndic.destroy()
            Game()

    labelIndic.destroy()
    labelMot.destroy()
    EntreeRep.destroy()
    compteurMot += 1
    if actFr == 1 and nbMot!=compteurMot:
        hasard = random.randint(0, len(listfA))
        mot = repareMot(listfA[hasard])
        reponse = repareMot(listfF[hasard])
        reponse.lower()
        labelMot = Label(fenetreJeu, text = mot, font='Helvetica 12 bold', justify=CENTER)
        labelMot.pack()
        EntreeRep = Entry(fenetreJeu, textvariable= ReponseJoueur, font = 'Helvetica 12 bold', justify=CENTER)
        EntreeRep.pack()
        EntreeRep.bind('<KeyPress-Return>', Accept)
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
    if nbMot == compteurMot:
        labelIndic.destroy()
        labelMot.destroy()
        EntreeRep.destroy()
        label2.destroy()
        label3.destroy()
        labelRep = Label(fenetreJeu, text = valueName.get() + ', vous avez un score de ' + str(score) + ' sur ' + str(nbMot), font = 'Helvetica 12 bold', justify=CENTER)
        labelRep.pack()

boutonFr = Button(fenetreJeu, text='Français', font='Helvetica 12 bold', command = Francais)
boutonAn = Button(fenetreJeu, text='Anglais', font='Helvetica 12 bold', command = Anglais)

boutonFr.bind('<Activate>', Game )
boutonAn.bind('<Activate>', Game )

fenetreJeu.mainloop()
fA.close()
fF.close()
