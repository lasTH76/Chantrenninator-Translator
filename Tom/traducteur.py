import os, random, sys, time, threading, shelve, smtplib
from tkinter import *

#os.chdir('C:\Python34')

def SearchPath():
    if getattr(sys, 'frozen', False):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.dirname(__file__)
    return datadir

#--------------------------------------------------------------

chemin = SearchPath()
CheminAbsolu = os.path.join(chemin, 'Chantrenninator-Translator')

fA = open(os.path.join(chemin, 'VocaAnglais.txt'), 'r')
fF = open(os.path.join(chemin, 'VocaFrancais.txt'), 'r')

listfF = [line.split('/n') for line in fF.readlines()]
listfA = [line.split('/n') for line in fA.readlines()]

#---------------------------------------------------------------
fenetreJeu = Tk()
fenetreJeu.title('Jeu de traduction')
fenetreJeu['bg'] = 'blue'
fenetreJeu.geometry('500x500+750+350')

#_______________________________________________________________
def showScore():
        HScore = shelve.open('score.txt')
        score = HScore['score']
            
def reportf():
    reportf=Toplevel()
    reportf.configure(width=600, height=300)
    reportf.title('Reporter un bug')
    reportf.resizable(width=False, height=False)

    labelrepor1 = Label(reportf, text='E-mail :', font = 'Helvetica 15 bold')# créer un label avec une police définit
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
menubarre = Menu(fenetreJeu)

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
score = 0
nbrEssai = 5
ReponseJoueur = StringVar()

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

label1 = Label(fenetreJeu, text='Bienvenue dans ce jeu de traduction mon jeune ami.' + '\n' + "Comment t'appelles-tu? ", font='Helvetica 10 bold', justify=CENTER)
label1.pack()

valueName = StringVar()
prenom = Entry(fenetreJeu, textvariable = valueName, font='Helvetica 10 bold', justify=CENTER)
prenom.pack()

def entrer():
        global label1, prenom, bouton1
        prenom.destroy()
        label1.destroy()
        bouton1.destroy()

def nbDeMot(evnt):
        label1 = Label(fenetreJeu, text = 'Très bien ' + valueName.get() + '.', font='Helvetica 10 bold', justify=CENTER)
        label1.pack()
        labelNbrMot = Label(fenetreJeu, text= 'Indiquez le nombre de mots à traduire (Minimum 5).', font='Helvetica 10 bold', justify=CENTER)
        labelNbrMot.pack()
        nbrMot = Entry(fenetreJeu, textvariable = nbMot, font='Helvetica 10 bold', justify=CENTER)
        nbrMot.pack()

        def entrer2():
                global nbMot, label2, boutonFr, boutonAn
                if nbMot.get() >= 5:
                        label1.destroy()
                        labelNbrMot.destroy()
                        nbrMot.destroy()
                        bouton2.destroy()
                        nbMot = nbMot.get()
                        label3 = Label(fenetreJeu, text='Tu vas maintenant avoir ' + str(nbMot) +' mots à traduire.' + '\n' + "Fais attention, il n'y a pas d'accent.", font='Helvetica 10 bold', justify=CENTER)
                        label3.pack()
                        label2.pack()
                        boutonFr.pack(side=LEFT, expand = True)
                        boutonAn.pack(side=RIGHT, expand = True)
                else:
                        nbMot.set('5')
        bouton2 = Button(fenetreJeu, text='Entrer', command = entrer2, font='Helvetica 10 bold', justify=CENTER)
        bouton2.pack()

bouton1 = Button(fenetreJeu,text = 'Entrer', command = entrer, font='Helvetica 10 bold', justify=CENTER)
bouton1.pack()
bouton1.bind('<Destroy>', nbDeMot)
label2 = Label(fenetreJeu, text='Maintenant, dans quelle langue veux-tu jouer?', font='Helvetica 10 bold', justify=CENTER)

def Francais():
        global boutonFr, boutonAn, label2
        boutonFr.destroy()
        boutonAn.destroy()
        label2['text'] ='Il faut les traduire en français'

def NouveauMot_Fr():
        global ReponseJoueur, labelInd, labelIndic, boutonFr, boutonAn, BoutonAccRep
	boutonAn.destroy()
	boutonFr.destroy()
        labelInd.destroy()
        labelIndic.destroy()
        hasard = random.randint(0, len(listfA))
        mot = repareMot(listfA[hasard])
        reponse = repareMot(listfF[hasard])
        reponse.lower()
        labelMot = Label(fenetreJeu, text = mot, font='Helvetica 10 bold', justify=CENTER)
        labelMot.pack()
        EntreeRep = Entry(fenetreJeu, textvariable= ReponseJoueur, font = 'Helvetica 10 bold', justify=CENTER)
        EntreeRep.pack()
	BoutonAccRep.pack()

def NouveauMot_An():
        global ReponseJoueur, labelInd, labelIndic, boutonFr, boutonAn, BoutonAccRep
	boutonAn.destroy()
	boutonFr.destroy()
        labelInd.destroy()
        labelIndic.destroy()
        hasard = random.randint(0, len(listfA))
        mot = repareMot(listfF[hasard])
        reponse = repareMot(listfA[hasard])
        reponse.lower()
        labelMot = Label(fenetreJeu, text = mot, font='Helvetica 10 bold', justify=CENTER)
        labelMot.pack()
        EntreeRep = Entry(fenetreJeu, textvariable= ReponseJoueur, font = 'Helvetica 10 bold', justify=CENTER)
        EntreeRep.pack()
	BoutonAccRep.pack()

def Verif_Accept():
        global ReponseJoueur, score, nbrEssai, valueName, reponse, EntreeRep, boutonFr, boutonAn
        ActAn = boutonAn.bind('<Activate>', ActAn = 1)
        ActFr = boutonFr.bind('<Activate>', ActFr = 1)
        if nbMot == 0:
                labelInd.destroy()
                labelIndic.destroy()
                labelInd.destroy()
                EntreeRep.destroy()
                labelRep = Label(fenetreJeu, text = valueName.get() + ',vous avez un score de' + score + 'sur' + nbMot, font = 'Helvetica 10 bold', justify=CENTER)
                labelRep.pack()
        else:
                while ReponseJoueur.get() != reponse and nbrEssai > 0:
                        if ReponseJoueur.get() != reponse:
                                nbrEssai += -1
                                labelIndic = Label(fenetreJeu, text='Il te reste' + nbrEssai + 'essais.', font = 'Helvetica 10 bold', justify=CENTER)
                                labelIndic.pack()
                        if ReponseJoueur.get() == reponse and nbrEssai >= 0:
                                score += 1
                                labelIndic = Label(fenetreJeu, text= 'Ceci est la bonne réponse!', font = 'Helvetica 10 bold', justify=CENTER)
                                labelIndic.pack()
                                if ActAn == 1:
                                    NouveauMot_An()
                                elif ActFr == 1:
                                    NouveauMot_Fr()
                        if nbrEssai == 0 and ReponseJoueur.get() != reponse:
                                labelInd = Label(fenetreJeu, text= 'La reponse était '"'"+ reponse +"' .", font='Helvetica 10 bold', justify=CENTER)
                                labelInd.pack()
                                if ActAn == 1:
                                    NouveauMot_An()
                                elif ActFr == 1:
                                    NouveauMot_Fr()
                nbrEssai = 5
                nbMot += -1


def Anglais():
        global boutonFr, boutonAn, label2
        boutonFr.destroy()
        boutonAn.destroy()
        label2['text']='Il faut les traduire en anglais'


boutonFr = Button(fenetreJeu, text='Français', font='Helvetica 10 bold', command = Francais)
boutonAn = Button(fenetreJeu, text='Anglais', font='Helvetica 10 bold', command = Anglais)
BoutonAccRep = Button(fenetreJeu , text = "Valider?", command = Verif_Accept, font='Helvetica 10 bold', justify=CENTER)

if label2.pack() == True:
	boutonFr.pack()
	boutonAn.pack()

boutonFr.bind('<Activate>', NouveauMot_Fr() )
boutonAn.bind('<Activate>', NouveauMot_An() )

fenetreJeu.mainloop()
fA.close()
fF.close()
time.sleep(1)

if __name__ == '__main__':
        trad()
