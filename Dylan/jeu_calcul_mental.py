##nous importons les modules qui nous permettrons de créer la fenêtre et d'utiliser le temps.
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from time import time, sleep #sleep permet de mettre en pause le programme (ou une fonction) pendant un certain temps.
from threading import Thread #permet d'éxecuter des tâches multiples en même temps.
import os, sys, random #permet d'utliser les commandes systèmes (comme l'utilisation de fichier exterieur) et le random sert à demander au système de choisir un nombre aléatoire.
#----------------------------------------------------
##fenêtre de configuration
jeu1 = Tk() #Cela permet de créer la fenêtre graphique
jeu1.configure(width=300, height=350) #Cela permet de configure la taille de la fenêtre en pixels.
jeu1.title("Calcul mental") #Cela permet de donner un titre à la fenêtre (dans ce cas là le titre de la fenêtre est "Calcul mental").
jeu1.resizable(width=False, height=False) #Cela permet d'éviter que l'utilisateur redimensionne la fenêtre comme il le souhaîte.

textitle=PhotoImage(file="image/nuage_title-jeu.png") #Cette commande permet d'utiliser une image sur la fenêtre pour l'utiliser comme devanture.
canttl = Canvas(jeu1, width=227,height=62) #Cela permet de redimentionner l'image.
canttl.create_image(0,0,anchor='nw', image=textitle) #Cette commande permet de créer l'image et de l'afficher.
canttl.place(x=45, y=10) #Cette commande permet de placer l'image sur la fenêtre avec un système de coordonnée.

#-----------------------------------------------------
##9000
def aide():
	top1=Toplevel() #Permet de créer une fenêtre au dessus de la principale
	top1.configure(width=350,height=200) #On régle la taille de la fenêtre
	top1.title("Aide") #On donne un nom à notre fenêtre
	top1.resizable(width=False, height=False) #Fonction qui évite le redimensionnement
	labeltop1 = Label(top1, text="Utilisation du jeu", font = "Helvetica 22 bold") #Créer un label avec une police définit
	labeltop1.place(x=45, y=0) #Coordonnées du label

def temps():
	global tmpr, tmp, score1, t #Cela permet d'utiliser une variable qui se trouve en dehors de la fonction
	#--------------------------------------------------------------------------
	##fonction de la fenêtre temps
	def renitial():
		global tmpr, tmp, score1, t #Cela permet d'utiliser des variables exterieur dans la fonction.
		tmp=0 #la variable "tmp" prend la valeur 0 pour permettre d'arrêter le temps.
		tmpr=10 #la variable "tmpr" prend la valeur 10 pour rénitialiser le temps à la valeur par défaut.
		tmp=tmpr #la variable "tmp" prend la valeur de "tmpr".
		score1=0 #le score est rénitialisé.
		t=0 #la variable "t" prend la valeur 0
		labeltop2['text']=str("Temps : ")+str(tmp)+str("s") #le label de la fenêtre de configuration est actualisé.
		temps1['text']=str("Time : ")+str(tmp) #On remplace le contenu du label temps1 par "Time : 'temps par défaut' ".
		reponsa.bind("<Return>", resultat) #On rend visible le bouton pour recommencer.

	def modifitemps():
		global tmpr, tmp, score1, t #Cela permet d'utiliser des variables exterieur dans la fonction.
		tmp=0 #la variable "tmp" prend la valeur 0 pour permettre d'arrêter le temps.
		imnwtime=int(jerenit1.get()) #On transforme la chaine de caractère entré dans la textbox de configuration en nombre entier.
		tmpr=imnwtime #la variable "tmpr" prend la valeur de "imnwtime".
		tmp=tmpr #la variable "tmp" prend la valeur de "tmpr".
		score1=0 #le score est rénitialisé.
		t=0 #la variable "t" prend la valeur 0
		labeltop2['text']=str("Temps : ")+str(tmp)+str("s") #le label de la fenêtre de configuration est actualisé.
		temps1['text']=str("Time : ")+str(tmp) #On remplace le contenu du label temps1 par "Time : 'temps définit par l'utilisateur' ".
		reponsa.bind("<Return>", resultat) #On rend visible le bouton pour recommencer.
	#-------------------------------------------------------------------------
	##Structure de la fenêtre temps
	top2=Toplevel() #Création d'une fenêtre au dessus de la principale.
	top2.configure(width=200,height=200) #On régle la taille de la fenêtre.
	top2.title("Temps") #On donne un nom à notre fenêtre.
	top2.resizable(width=False, height=False) #Fonction qui évite le redimensionnement.
	labeltop2 = Label(top2, text="Temps : "+str(tmp)+"s", font = "Helvetica 22 bold") #Création d'un label avec une police définit.
	labeltop2.place(x=5, y=0) #Coordonnées du label.

	labelnb2 = Label(top2, text="Entrez la durée du quizz :", font="Helvetica 10 bold") #Label pour guider l'utilisateur.
	labelnb2.place(x=20, y=50) #Coordonnées du label.
	jerenit1 = StringVar() #Récupère la valeur du temps définit par l'utilisateur.
	jerenitlabel = Entry(top2, textvariable = jerenit1, width=10, justify=CENTER, font="Helvetica 15 bold") #Création d'une textbox de longueur 30.
	jerenitlabel.place(x=40, y=80) #Coordonnées du textbox.
	b1t2=Button(top2, text="Appliquer", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=modifitemps) #Bouton qui permet d'appliquer la modification en executant la fonction modifitemps.
	b1t2.place(x=110, y=160) #Coordonnées du bouton.
	b2t2=Button(top2, text="Annuler", padx=15, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=top2.destroy) #Bouton qui permet d'annuler la modification en fermant la fenêtre.
	b2t2.place(x=10, y=160) #Coordonnées du bouton.
	b2t2=Button(top2, text="Rénitialiser", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=renitial) #Bouton qui permet de remettre le temps à 10 secondes en executant la fonction renitial.
	b2t2.place(x=50, y=120) #Coordonnées du bouton.

#-----------------------------------------------------
##menu
menubar = Menu(jeu1) #Création de la barre de menu.

menu1 = Menu(menubar, tearoff=0) #Création d'un premier bouton pour le menu.
menu1.add_command(label="Quitter", command=jeu1.destroy) #Création d'un bouton qui ferme le programme et qui se trouve dans le "sous-onglet" de l'onglet Fichier.
menubar.add_cascade(label="Fichier", menu=menu1) #Création du nom du bouton créé du menu.

menu2 = Menu(menubar, tearoff=0) #Création d'un deuxième bouton pour le menu.
menu2.add_command(label="Temps", command=temps) #Création d'un bouton qui ouvre la fenêtre de configuration du temps et qui se trouve dans le "sous-onglet" de l'onglet Configuration.
menubar.add_cascade(label="Configuration", menu=menu2) #Création du nom du bouton créé du menu.

menu3 = Menu(menubar, tearoff=0) #Création d'un troisième bouton pour le menu.
menu3.add_command(label="Aide", command=aide) #Création d'un bouton qui ouvre la fenêtre d'aide et qui se trouve dans le "sous-onglet" de l'onglet A propos.
menubar.add_cascade(label="A propos", menu=menu3) #Création du nom du bouton créé du menu.

jeu1.config(menu=menubar) #On configure la barre de menu.
#-----------------------------------------------------
##Image
validato = PhotoImage(file="image/null.png") #On ajoute une image au programme pour la devanture.
canvas = Canvas(jeu1,width=30, height=30) #On régle la taille alloué pour l'image.
canvas.create_image(0, 0, anchor=NW,image=validato) #On créé l'image.
canvas.place(x=250, y=140) #On place l'image
#-----------------------------------------------------
##Variables
score1=0
part1=0
partdef=10
operateurs=["X", "+", "-"]
t=0
tmp=10
tmpr=10
bestscore=0
#---------------------------------------------------------
##Fonction de calcul
class The_time(Thread): #Classe qui permmet de créer un compte à rebours qui s'execute en même temps que la fonction résultat (d'où le "Thread" entre parenthèses).
	def __init__(self): 
		Thread.__init__(self)
		self.pause=False

	def run(self):
		global temps1, tmp #utiliser variables exterieur à la fonction.
		while self.pause==False:
			while tmp!=0: #Tant que le temps n'est pas écoulé, enlever une seconde à celle-ci (voir ligne 122).
				temps1['text']=str("Time : ")+str(tmp) #Réactualisation du label temps1 pour que l'utilisateur sache combien de temps il lui reste.
				tmp=tmp-1 #enlève une seconde au temps (= à la variable tmp).
				sleep(1) #La boucle se met en pause toute les secondes pour éviter que le temps s'écoule trop vite.
			self.pause=True
				
		reponsa.unbind("<Return>") #évite que la personne ne rentre d'autre réponse alors que le compte à rebours est terminé.
		boutonreni.config(state = NORMAL) #dégriser le bouton pour recommencer le jeu.

	def pause(self):
		self.pause=True
	def resume(self):
		tmp=tmpr
		self.pause=False


def resultat(event): #"event" permet d'utiliser une touche du clavier pour executer la fonction resultat.
	global part1,opera1,a,b,c, reponsa,score1, t, tmp, tmpr, Timone #permet d'utiliser les variables exterieur à la fonction.
	try:
		if t==0: #Permet de savoir si la fonction a été mise en route. Si non, la variable "t" se met à 1 (ligne 143), pour éviter que quand on execute la fonction avec la touche entrez pour répondre au question, le compte à rebours s'execute une 2e fois.
			Timone = The_time() #Cela permmet d'utiliser la classe.
			tmp=tmpr #le temps prend la valeur du temps défini, si l'utilisateur à changé le temps dans le menu configuration.
			Timone.start() #Cela permet d'enclencher le compte à rebours.
			t=1
		else: #Sinon, si t==1 alors faire la suite.
			t=1
		repon1=str(reponse.get()) #la variable repon1 prend la valeur rentré dans la textbox.
		if opera1==0: #Si l'operation est une mutiplication faire la suite.
			tot=a*b
		elif opera1==1: #Sinon, si l'operation est une addition faire la suite.
			tot=a+b
		else: #A l'inverse des deux, l'operation est donc une soustraction, et donc on exécute cette condition.
			tot=a-b
		if str(repon1)==str(tot): #Si la variable rentré est la bonne réponse alors on exécute cette condition.
			validato.config(file="image/valide2.png") #Une image apparaît pour nous dire que notre réponse est la bonne.
			score1+=1 #Donc le score (= variable "score1") augmente de 1 point.
			labscore['text']=str("Point : ")+str(score1) #Le label "labscore" est actualiser.
		else: #Sinon, si la réponse est fausse executer cette condition.
			validato.config(file="image/faux2.png") #Une image pour nous dire que c'est faux.
		tot2['text']=str("Résultat : ")+str(tot) #Le bon résultat est affiché.
	except ValueError: #"try" (ligne 138) et "except ValueError" permettent normalement d'afficher une fenêtre qui dit que la saisie entrée n'est pas un nombre. (Mais au final elle ne sert à rien à part montrer que je connaît cette fonction) 
		showerror("Erreur", "Incorrect")
	part1+=1 
	a=random.randint(0,10) #La variable "a" prend la valeur d'un nombre entier au hasard compris entre 0 et 10.
	b=random.randint(0,10) #La variable "b" prend la valeur d'un nombre entier au hasard compris entre 0 et 10.
	c=random.choice(operateurs) #On demande au programme de faire un choix aléatoire dans la liste "opérateurs"
	opera1=operateurs.index(c) #opera1 prend la valeur de l'indice de l'opérateurs choisi (exemple : "X" = 0, "+" = 1, ...)
	calcul1['text'] = str(a)+str(c)+str(b) #Remplace le label calcul1 par les nouvelles valeurs à calculer.
	reponsa.delete(0, END) #Efface le contenu de la textbox pour éviter que l'utilisateur ne perd de temps à le faire.

	bestscore=score1/tmpr #Quand la partie est terminé, la variable "bestscore" prend la valeur du calcul du score sur le temps entrez par l'utilisateur.
	data=float(dodo) #Comme la variable dodo enregistré dans un fichier point a de grande chance d'être un nombre à virgule, alors on utilise la fonction float pour récuperer un nombre décimal et pouvoir le comparer par la suite avec le nouveau score.
	if bestscore>data: #Si le nouveau score (bestscore) fait par l'utilisateur a dépassé son précédent score enregistré dans un fichier, alors il execute la condition.
		bstsc1=str(bestscore) #Le nouveau meilleur score (bestscore) est enregistré dans la varaible bstsc1 en tant que chaîne de caractère (d'où la fonction str(), pour string).
		fichier2=open("data/table_de_calcul.txt","w") #On ouvre le fichier où l'ancien meilleur score est. Et on ouvre le fichier en "w" (pour write) ce qui permet d'écraser les chaînes de caractère entré.
		fichier2.write(bstsc1) #La fonction write (écrire en anglais) permet d'ajouter le nouveau score.
		fichier2.close() #La fonction ".close()" sert à fermer le fichier en l'enregistrant.
		labelbstsore['text']="Best Score : "+str(bstsc1)+" pts/sec" #Le labelbstscore est actualiser.

def reniti1(): #Cette fonction permet de relancer le jeu.
	global temps1, score1, tmp, tmpr #Ce sont les variables exterieur qui seront utiliser dans la fonction.
	t=1 #On met par précaution que t prend la valeur 1.
	tmp=tmpr #Le temps prend la valeur du temps fixé par l'utilisateur.
	temps1['text']=str("Time : ")+str(tmp) #Le label temps1 est égal au nouveau temps.
	tot2['text']=str("Résultat : ") #Le label tot2 est rénitialisé.
	labscore['text']=str("Point : ")+str(0) #Le label labelscore est rénitialisé.
	score1=0 #Le score (score1) est égal à 0.
	calcul1['text'] = str(a)+str(c)+str(b) #Le label calcul1 affiche un nouveau problème.
	boutonreni.config(state = DISABLED) #Le bouton pour recommencer est griser (et donc inutilisable).
	reponsa.bind("<Return>", resultat) #La touche Entrez pour confirmer les choix est réactivé.
	Timone = The_time()
	Timone.start() #La fonction de la classe est réactivé avec un nouveau temps si l'utilisateur en a fixé un.

#----------------------------------------------------------
#réponder au question avant le temps imparti

tot2=Label(jeu1, text="Résultat : ", font = "Helvetica 20 bold") #On crée le label "tot2" pour afficher les résultats.
tot2.place(x=5, y=220) #Coordonnées du label.

calcul1=Label(jeu1, text="", font = "Helvetica 20 bold") #On crée le label "calcul1" pour afficher les opérations.
calcul1.place(x=120, y=80) #Coordonnées du label.

a=random.randint(0,10) #La variable "a" prennd la valeur d'un nombre entier au hasard entre 0 et 10.
b=random.randint(0,10) #La variable "b" prennd la valeur d'un nombre entier au hasard entre 0 et 10.
c=random.choice(operateurs) #On demande au programme de faire un choix aléatoire dans la liste "opérateurs"
opera1=operateurs.index(c) #opera1 prend la valeur de l'indice de l'opérateurs choisi (exemple : "X" = 0, "+" = 1, ...)
calcul1['text'] = str(a)+str(c)+str(b) #On affiche l'opération.

labscore=Label(jeu1, text="Point : "+str(0), font = "Helvetica 20 bold") #Création du label pour les points.
labscore.place(x=5, y=260) #Coordoonnées du label.

reponse = StringVar() #Récupère et assigne la chaîne de caractère entré dans la textbox à la variable "reponse".
reponsa = Entry(jeu1, textvariable = reponse, width=21, font="Helvetica 15 bold", justify=CENTER) #On crée la textbox "reponsa" et on lui donne comme paramètre le font (= la police), width (= taille de la textbox) et justify (qui permet de mettre le curseur au milieu de la textbox).
reponsa.place(x=10, y=140) #Coordonnées de la textbox.
reponsa.bind("<Return>", resultat) #Cela permet d'executer la fonction "resultat" avec la touche Entrez (= Return).

instru1=Label(jeu1, text="Entrez", font = "Helvetica 15 bold") #On crée un bouton de longueur 200 et largeur 10 avec une ccouleur plus grise quand le bouton est pressé.
instru1.place(x=110, y=180) #Coordonnées du label

boutonreni=Button(jeu1, text="Recommencer", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", state=DISABLED, command=reniti1) #On crée un bouton "recommencer" avec comme paramètres state (pour rendre le bouton grisé, qu'il ne soit pas executable).
boutonreni.place(x=180, y=180) #Coordonnées du bouton.

temps1=Label(jeu1, text="Time : "+str(tmp), font = "Helvetica 15 bold") #Création du label pour afficher le temps.
temps1.place(x=5, y=180) #Coordonnées du label.

fichier = open("data/table_de_calcul.txt", "r") #Ouvrir le fichier en mode "r" (pour read = lire en anglais).
dodo=fichier.read() #La variable dodo prend comme chaîne de caractère la valeur qui est dans le fichier.
labelbstsore=Label(jeu1, text="Best Score : "+str(dodo)+" pts/sec", font="Helvetica 15 bold") #On crée le label "labelbstscore" pour afficher le meilleur score fait par l'utilisateur.
labelbstsore.place(x=5, y=300) #Coordonnées du label
fichier.close() #On ferme le fichier texte.

jeu1.mainloop() #Ceci est la fin de la boucle de la fenêtre.