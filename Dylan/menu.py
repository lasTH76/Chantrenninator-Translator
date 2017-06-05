from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import time, random, sys, os, smtplib #permet d'utliser les commandes systèmes (comme l'utilisation de fichier exterieur) et le random sert à demander au système de choisir un nombre aléatoirement.
from time import time, sleep #sleep permet de mettre en pause le programme (ou une fonction) pendant un certain temps.

#--------------------------------------------------------------------------------------------------------------
fenetre = Tk() #Cela permet de créer la fenêtre graphique
fenetre.configure(width=550, height=350) #Cela permet de configurer la taille de la fenêtre en pixels.
fenetre.title("Jeux de réflexion et de logique") #Cela permet de donner un titre à la fenêtre (dans ce cas là le titre de la fenêtre est "Jeux de réflexion et de logique").
fenetre.resizable(width=False, height=False) #Cela permet d'éviter que l'utilisateur redimensionne la fenêtre comme il le souhaite.

#--------------------------------------------------------------------------------------------------------------
##image menu
textitlemenu=PhotoImage(file="image/nuage_title-menu.png") #Cette commande permet d'utiliser une image sur la fenêtre pour l'utiliser comme devanture.
canttml = Canvas(fenetre, width=500,height=145) #Cela permet de redimensionner l'image.
canttml.create_image(0,0,anchor='nw', image=textitlemenu) #Cette commande permet de créer l'image et de l'afficher.
canttml.place(x=115, y=20) #Cette commande permet de placer l'image sur la fenêtre avec un système de coordonnée.

gif_parle=PhotoImage(file="image/einstein_montre.gif")
can1 = Canvas(fenetre, width=120,height=135) #Cela permet de redimensionner le gif.
can1.create_image(0,0,anchor='nw', image=gif_parle) #Cette commande permet de créer le gif et de l'afficher.
can1.place(x=10, y=0) #Coordonnées du gif.

gif_parle2=PhotoImage(file="image/einstein_montre.gif")
can2 = Canvas(fenetre, width=120,height=135) #Cela permet de redimensionner le gif.
can2.create_image(0,0,anchor='nw', image=gif_parle2) #Cette commande permet de créer le gif et de l'afficher.
can2.place(x=450, y=0) #Coordonnées du gif.

ind = -1 #La variable ind prend la valeur -1
def update(delay=200): #Fonction qui permet d'animer les gifs en affichant chaque image entre un intervalle de temps.
    global ind #Cela permet d'utiliser une variable exterieur dans la fonction.
    ind += 1 #Permet d'incrémenter de 1 la variable ind
    if ind == 8: ind = 0 #Si le gif atteint la 8e image (qui est la dernière), il recommence à 0.
    gif_parle.configure(format="gif -index " + str(ind)) #Permet d'afficher une image spécifique avec -index X (étant entre 0 et 8) se trouvant dans la compilation d'image qui est le gif.
    gif_parle2.configure(format="gif -index " + str(ind)) #Permet d'afficher une image spécifique avec -index X (étant entre 0 et 8) se trouvant dans la compilation d'image qui est le gif.
    fenetre.after(delay, update)
update() #execute la fonction "update"
#--------------------------------------------------------------------------------------------------------------
##fonction menu

def reportf():
	reportf=Toplevel() #Permet de créer une fenêtre au dessus de la principale
	reportf.configure(width=600, height=300) #On règle la taille de la fenêtre
	reportf.title("Reporter un bug") #On donne un nom à notre fenêtre
	reportf.resizable(width=False, height=False) #Fonction qui évite le redimensionnement

	labelrepor1 = Label(reportf, text="E-mail :", font = "Helvetica 15 bold") #Création d'un label avec une police définie
	labelrepor1.place(x=0, y=0) #Coordonnées du label
	emmailbox1 = StringVar()
	emmailbox1.set("@gmail.com")
	email1 = Entry(reportf, textvariable = emmailbox1, width=21, font="Helvetica 15 bold", justify=CENTER)
	email1.place(x=90, y=0) #Coordonnées du label

	labelMDP = Label(reportf, text="Votre mot de passe d'email:", width=21, font="Helvetica 15 bold") #Création d'un label avec une police définie
	labelMDP.place(x=0, y=100) #Coordonnées du label
	motdepasse = StringVar()
	MDP = Entry(reportf, textvariable = motdepasse, width = 21, font="Helevetica 15 bold", justify=CENTER)
	MDP.place(x=280, y=100) #Coordonnées du label

	labelreport2 = Label(reportf, text= "Indiquez de ce coté l'erreur rencontrée:", font = "Helvetica 15 bold") #Création d'un label avec une police définie
	labelreport2.place(x=0, y=175) #Coordonnées du label
	sujetext1 = StringVar()
	sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font="Helvetica 15 bold", justify=CENTER)
	sujet1.place(x=200, y=200) #Coordonnées du label

	def ELRport():
                
		fromaddr = emmailbox1.get() #Récuperer la valeur entrée
		toaddrs = 'dylan.e@hotmail.fr' #Addresse électronique de l'un des créateurs

		msg = sujetext1.get() #Récuperer la valeur entrée
		MDP = motdepasse.get() #Récuperer la valeur entrée
                
		server = smtplib.SMTP('smtp.gmail.com', 235) 
		server.ehlo()
		server.starttls()
		server.login(fromaddr , MDP)

		server.sendmail(fromaddr, toaddrs, msg)
		server.close()
		reportf.destroy()

	boutonEnvoi = Button(reportf, text = "Envoyer le report", command = ELRport)
	boutonEnvoi.place(x=250, y=250)

#--------------------------------------------------------------------------------------------------------------
##menubar menu
menubar = Menu(fenetre) #Création d'une barre de menu.

menu1 = Menu(menubar, tearoff=0) #Création d'un premier bouton pour le menu.
menu1.add_command(label="Quitter", command=fenetre.destroy) #Création d'un bouton qui ferme le programme.
menubar.add_cascade(label="Fichier", menu=menu1) #Création d'un nom au premier bouton du menu.

menu2 = Menu(menubar, tearoff=0) #Création d'un deuxième bouton pour le menu.
menu2.add_command(label="A propos") #Création d'un bouton qui ouvre une fenêtre A propos.
menu2.add_command(label="Reporter un bug", command=reportf) #Création d'un bouton qui ouvre une fenêtre report bug.
menubar.add_cascade(label="Aide", menu=menu2)

fenetre.config(menu=menubar) #On configure la barre de menu.
#--------------------------------------------------------------------------------------------------------------
##fonction ouverture
def batjeu1():
	exec(open("./jeu_calcul_mental.py").read()) #Ouvrir le programme "jeu_calcul_mental" en laissant la main au programme principale.

def batjeu2():
	exec(open("./JeuMorse.py").read()) #Ouvrir le programme "jeu du morse" en laissant la main au programme principale.

def batjeu3():
	exec(open("./choix.py").read()) #Ouvrir le programme "jeu des capitales" en laissant la main au programme principale.

def batjeu4():
	exec(open("./traducteur.py").read()) #Ouvrir le programme "jeu de traduction Ang/Fr" en laissant la main au programme principale.

#--------------------------------------------------------------------------------------------------------------
##bouton menu
imageb1calc= PhotoImage(file="image/nuage_menu_title-jeu1.png") #Importe d'une image dans une variable
boutonreni=Button(fenetre, text="", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#0076BB", image=imageb1calc, bg="#00a2ff", command=batjeu1) #Création d'un bouton avec une image en fond.
boutonreni.place(x=70, y=180) #Coordonnées du bouton

imageb2calc= PhotoImage(file="image/nuage_menu_title-morse2.png") #Importe d'une image dans une variable
boutonreni2=Button(fenetre, text="", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#c50404", image=imageb2calc, bg="#f50000", command=batjeu2) #Création d'un bouton avec une image en fond.
boutonreni2.place(x=300, y=180) #Coordonnées du bouton

imageb3calc= PhotoImage(file="image/nuage_menu_title-capitale.png") #Importe d'une image dans une variable
boutonreni3=Button(fenetre, text="", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#009904", image=imageb3calc, bg="#00d205", command=batjeu3) #Création d'un bouton avec une image en fond.
boutonreni3.place(x=70, y=250) #Coordonnées du bouton

imageb4calc= PhotoImage(file="image/nuage_menu_title-trad.png") #Importe d'une image dans une variable
boutonreni3=Button(fenetre, text="", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#ca4700", image=imageb4calc, bg="#ff5a00", command=batjeu4) #Création d'un bouton avec une image en fond.
boutonreni3.place(x=300, y=250) #Coordonnées du bouton

fenetre.mainloop()
