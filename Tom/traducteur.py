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
CheminAbsolu = os.path.join(chemin, "Chantrenninator-Translator")

fA = open(os.path.join(chemin, 'VocaAnglais.txt'), 'r')
fF = open(os.path.join(chemin, 'VocaFrancais.txt'), 'r')

listfF = [line.split("/n") for line in fF.readlines()]
listfA = [line.split("/n") for line in fA.readlines()]

score = 0
nbrEssai = 5
choix = "Vide"
ReponseJoueur = "mouais"
nbMot = 0

#---------------------------------------------------------------
fenetreJeu = Tk()
fenetreJeu.title("Jeu de traduction")
fenetreJeu["bg"] = 'blue'
fenetreJeu.geometry("500x400+350+666")

#_______________________________________________________________
def showScore():
        HScore = shelve.open('score.txt')
        score = HScore['score']
	        
def reportf():
	reportf=Toplevel()
	reportf.configure(width=600, height=300)
	reportf.title("Reporter un bug")
	reportf.resizable(width=False, height=False)

	labelrepor1 = Label(reportf, text="E-mail :", font = "Helvetica 15 bold")# créer un label avec une police définit
	labelrepor1.place(x=0, y=0)# coordonnées du label
	emmailbox1 = StringVar()
	emmailbox1.set("@gmail.com")
	email1 = Entry(reportf, textvariable = emmailbox1, width=21, font="Helvetica 15 bold", justify=CENTER)
	email1.place(x=90, y=0)

	labelMDP = Label(reportf, text="Votre mot de passe d'email:", width=21, font="Helvetica 15 bold").place(x=0, y=100)
	motdepasse = StringVar()
	MDP = Entry(reportf, textvariable = motdepasse, width = 21, font="Helevetica 15 bold").place(x=280, y=100)

	labelreport2 = Label(reportf, text= "Indiquez de ce coté l'erreur rencontrée:", font = "Helvetica 15 bold").place(x=0, y=175)
	sujetext1 = StringVar()
	sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font="Helvetica 15 bold", justify=CENTER)
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

	boutonEnvoi = Button(reportf, text = "Envoyer le report", command = ELRport).place(x=250, y=250)
        
def créateurs():
        createurs = Toplevel()
        createurs.configure(width = 1666, height = 1666)
        createurs.title("Générique de Fin")
        createurs.resizable(False, False)
        createurs["bg"] = fenetreJeu["bg"]
        
        labelC1 = Label(createurs, text = "Ce jeu vous a été présenté par " + '\n' + "Tom Habbar, Dylan Essakhi et Oscar Sellier." + '\n' + "Avec l'aide supplémentaire de Gawein Le Goff et de Erwan Castioni" + '\n' + "A l'occasion du bac d'ISN se déroulant au Lycée Camille Saint-Saens" + '\n' + "En espérant qu'il vous plaise ^^").pack()

#_______________________________________________________________
menubarre = Menu(fenetreJeu)

menu1 = Menu(menubarre, tearoff = 0)
menu1.add_command(label='Scores', command = showScore)
menu1.add_separator()
menu1.add_command(label='Quitter', command = fenetreJeu.quit)
menubarre.add_cascade(label='Fichier', menu=menu1)

menu2 = Menu(menubarre, tearoff = 0)
menu2.add_command(label="A propos", command = créateurs)# on crées un boutton qui ouvre une fenêtre alerte
menu2.add_command(label="Reporter un bug", command=reportf)
menubarre.add_cascade(label="Aide", menu=menu2)

fenetreJeu.config(menu=menubarre)

#_______________________________________________________________
##class Destructeur(threading.Thread):
##        def __init__(self):
##                threading.Thread.__init__(self)
##        def run(self):
##                time.sleep(5)
##                label1.destroy()

label1 = Label(fenetreJeu, text="Bienvenue dans ce jeu de traduction mon jeune ami. Comment t'appelles-tu? ").pack()

##conan = Destructeur()
##conan.start()

valueName = StringVar()
prenom = Entry(fenetreJeu, textvariable = valueName).pack()

def entrer():
        label1 = Label(fenetreJeu, text = "Très bien mon jeune " + prenom.get() + ".").pack()

bouton1 = Button(fenetreJeu,text = 'Accepter', command = entrer).pack()

##while nbMot <= 4:
##        nbMot = int(input("Indiquer le nombre de mots que vous voulez traduire -->   "))
##        if nbMot > 0 and nbMot < 5:
##                print("Petit Joueur.", end='\n')
##
##print("Tu vas maintenant avoir", nbMot, "mots à traduire.")
##print("Fais attention il n'y a pas d'accent.")
##print("Maintenant, dans quelle langue veux-tu jouer?")
##
##def repareMot(mot):
##        listeNouvMot = []
##        ignoreSuivant = False
##        for indLettre in range(len(mot)):
##                if ignoreSuivant:
##                        ignoreSuivant = False
##                        pass
##                elif (mot[indLettre] in ("[", "]", "'")):
##                        pass
##                elif mot[indLettre] == chr(92) and mot[indLettre + 1] == "n":
##                        ignoreSuivant = True
##                        pass
##                else:
##                        listeNouvMot.append(mot[indLettre])
##        nouveauMot = "".join(listeNouvMot)
##        nouveauMot.replace("\n", "")
##        if nouveauMot.endswith("\n"):
##                vraiMot = nouveauMot[:-1] #On enleve le dernier caractere (= saut de ligne) pour eviter les sauts de lignes inutiles
##        else:
##                vraiMot = nouveauMot
##        return vraiMot
##
##while not choix in ("Francais", "Anglais"):
##        choix = input("Francais ou Anglais?    ")
##        if choix == "Francais":
##                print("Il faut les traduire en anglais")
##                for loop in range(nbMot):
##                        hasard = random.randint(0, len(listfF))
##                        mot = repareMot(listfF[hasard])
##                        reponse = repareMot(listfA[hasard])
##                        reponse.lower()
##                        print(mot, end='\n')
##                        while ReponseJoueur != reponse and nbrEssai > 0:
##                                ReponseJoueur = input()
##                                if ReponseJoueur != reponse:
##                                        nbrEssai += -1
##                                        print("Il vous reste", nbrEssai, "essais.", end= '\n')
##                                        print("")
##                                if ReponseJoueur == reponse and nbrEssai >= 0:
##                                        score += 1
##                                        print("")
##                                        break
##                        if nbrEssai == 0 and ReponseJoueur != reponse:
##                                print("La reponse était", reponse,".")
##                                print()
##                        nbrEssai = 5
##
##
##        if choix == "Anglais":
##                print("Il faut les traduire en francais")
##                for loop in range(nbMot):
##                        hasard = random.randint(0, len(listfA))
##                        mot = repareMot(listfA[hasard])
##                        reponse = repareMot(listfF[hasard])
##                        reponse.lower()
##                        print(mot, end='\n')
##                        while ReponseJoueur != reponse and nbrEssai > 0:
##                                ReponseJoueur = input()
##                                if ReponseJoueur != reponse:
##                                        nbrEssai += -1
##                                        print("Il vous reste", nbrEssai, "essais.", end= '\n')
##                                        print("")
##                                if ReponseJoueur == reponse and nbrEssai >= 0:
##                                        score += 1
##                                        print("")
##                                        break
##                        if nbrEssai == 0 and ReponseJoueur != reponse:
##                                print("La reponse était", reponse,".")
##                                print()
##                        nbrEssai = 5
##
##print(prenom, ",vous avez un score de",score,"sur",nbMot)

fenetreJeu.mainloop()
fA.close()
fF.close()
time.sleep(1)

if __name__ == '__main__':
        trad()
