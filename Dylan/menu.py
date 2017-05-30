from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import time, random, sys, os, smtplib
from time import time, sleep
#--------------------------------------------------------------------------------------------------------------
fenetre = Tk() #Cela permet de créer la fenêtre graphique
fenetre.configure(width=550, height=400) #Cela permet de configure la taille de la fenêtre en pixels.
fenetre.title("Jeux de réflexion et de logique") #Cela permet de donner un titre à la fenêtre (dans ce cas là le titre de la fenêtre est "Jeux de réflexion et de logique").
fenetre.resizable(width=False, height=False) #Cela permet d'éviter que l'utilisateur redimensionne la fenêtre comme il le souhaîte.

#--------------------------------------------------------------------------------------------------------------
##image menu
textitlemenu=PhotoImage(file="image/nuage_title-menu.png") #Cette commande permet d'utiliser une image sur la fenêtre pour l'utiliser comme devanture.
canttml = Canvas(fenetre, width=500,height=145) #Cela permet de redimentionner l'image.
canttml.create_image(0,0,anchor='nw', image=textitlemenu) #Cette commande permet de créer l'image et de l'afficher.
canttml.place(x=115, y=20) #Cette commande permet de placer l'image sur la fenêtre avec un système de coordonnée.

gif_parle=PhotoImage(file="image/einstein_montre.gif")
can1 = Canvas(fenetre, width=120,height=135) #Cela permet de redimentionner le gif.
can1.create_image(0,0,anchor='nw', image=gif_parle) #Cette commande permet de créer le gif et de l'afficher.
can1.place(x=10, y=0) #Coordonnées du gif.

gif_parle2=PhotoImage(file="image/einstein_montre.gif")
can2 = Canvas(fenetre, width=120,height=135) #Cela permet de redimentionner le gif.
can2.create_image(0,0,anchor='nw', image=gif_parle2) #Cette commande permet de créer le gif et de l'afficher.
can2.place(x=450, y=0) #Coordonnées du gif.

ind = -1 #La variable ind prend la valeur -1
def update(delay=200): #Fonction qui permet d'animer les gifs en affichant chaques images entre un intervalle de temps.
    global ind #Cela permet d'utiliser une variable exterieur dans la fonction.
    ind += 1 #Permet d'incrémenter de 1 la variable ind
    if ind == 8: ind = 0 #Si le gif atteint la 8e image (qui est la dernière), il recommence à 0.
    gif_parle.configure(format="gif -index " + str(ind)) #Permet d'afficher une image spécifique avec -index X (étant entre 0 et 8) se trouvant dans la compilation d'image qui est le gif.
    gif_parle2.configure(format="gif -index " + str(ind)) #Permet d'afficher une image spécifique avec -index X (étant entre 0 et 8) se trouvant dans la compilation d'image qui est le gif.
    fenetre.after(delay, update)
update() #execute le fonction "update"
#--------------------------------------------------------------------------------------------------------------
##fonction menu
def menu_graphf():
	menu_graphf=Toplevel() #Permet de créer une fenêtre au dessus de la principale
	menu_graphf.configure(width=350,height=200) #On régle la taille de la fenêtre
	menu_graphf.title("Graphique") #On donne un nom a notre fenêtre
	menu_graphf.resizable(width=False, height=False) #Fonction qui évite le redimensionnement

def reportf():
	reportf=Toplevel() #Permet de créer une fenêtre au dessus de la principale
	reportf.configure(width=600, height=300) #On régle la taille de la fenêtre
	reportf.title("Reporter un bug") #On donne un nom a notre fenêtre
	reportf.resizable(width=False, height=False) #Fonction qui évite le redimensionnement

	labelrepor1 = Label(reportf, text="E-mail :", font = "Helvetica 15 bold") #Création d'un label avec une police définit
	labelrepor1.place(x=0, y=0) #Coordonnées du label
	emmailbox1 = StringVar()
	emmailbox1.set("@gmail.com")
	email1 = Entry(reportf, textvariable = emmailbox1, width=21, font="Helvetica 15 bold", justify=CENTER)
	email1.place(x=90, y=0) #Coordonnées du label

	labelMDP = Label(reportf, text="Votre mot de passe d'email:", width=21, font="Helvetica 15 bold") #Création d'un label avec une police définit
	labelMDP.place(x=0, y=100) #Coordonnées du label
	motdepasse = StringVar()
	MDP = Entry(reportf, textvariable = motdepasse, width = 21, font="Helevetica 15 bold", justify=CENTER)
	MDP.place(x=280, y=100) #Coordonnées du label

	labelreport2 = Label(reportf, text= "Indiquez de ce coté l'erreur rencontrée:", font = "Helvetica 15 bold") #Création d'un label avec une police définit
	labelreport2.place(x=0, y=175) #Coordonnées du label
	sujetext1 = StringVar()
	sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font="Helvetica 15 bold", justify=CENTER)
	sujet1.place(x=200, y=200) #Coordonnées du label

	def ELRport():
                
		fromaddr = emmailbox1.get()
		toaddrs = 'dylan.e@hotmail.fr'
		msg = sujetext1.get()
		MDP = motdepasse.get()
                
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
	os.chdir("C:\\Users\\Anonymed\\Desktop\\BAC") #Changer le répertoire.
	os.popen("jeu_calcul_mental.py") #Ouvrir le programme "jeu_calcul_mental" en laissant la main au programme principale.


#--------------------------------------------------------------------------------------------------------------
##bouton menu
imageb1calc= PhotoImage(file="image/nuage_title-jeu.png") #Importe d'une image dans une variable
boutonreni=Button(fenetre, text="", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#0076BB", image=imageb1calc, bg="#00a2ff", command=batjeu1)
boutonreni.place(x=10, y=180) #Coordonnées du bouton

fenetre.mainloop()