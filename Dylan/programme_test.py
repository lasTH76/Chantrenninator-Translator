<<<<<<< Updated upstream
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import os
import sys
import time
from time import time, sleep
import random, smtplib
from threading import Thread
#--------------------------------------------------------------------------------------------------------------
fenetre = Tk()
fenetre.configure(width=550, height=400)
fenetre.title("Jeux de réflexion et de logique")
fenetre.resizable(width=False, height=False)

#--------------------------------------------------------------------------------------------------------------
##image menu
textitlemenu=PhotoImage(file="image/nuage_title-menu.png")
canttml = Canvas(fenetre, width=500,height=145)
canttml.create_image(0,0,anchor='nw', image=textitlemenu)
canttml.place(x=115, y=20)

gif_parle=PhotoImage(file="image/einstein_montre.gif")
can1 = Canvas(fenetre, width=120,height=135)
can1.create_image(0,0,anchor='nw', image=gif_parle)
can1.place(x=10, y=0)

gif_parle2=PhotoImage(file="image/einstein_montre.gif")
can2 = Canvas(fenetre, width=120,height=135)
can2.create_image(0,0,anchor='nw', image=gif_parle2)
can2.place(x=450, y=0)

ind = -1
def update(delay=200):
    global ind
    ind += 1
    if ind == 8: ind = 0
    gif_parle.configure(format="gif -index " + str(ind))
    gif_parle2.configure(format="gif -index " + str(ind))
    fenetre.after(delay, update)
update()
#--------------------------------------------------------------------------------------------------------------
##fonction menu
def menu_graphf():
	menu_graphf=Toplevel()
	menu_graphf.configure(width=350,height=200)# on regle la taille de la fenetre
	menu_graphf.title("Graphique")# on donne un nom a notre fenetre
	menu_graphf.resizable(width=False, height=False)# fonction qui évite le redimensionnement

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

	labelMDP = Label(reportf, text="Votre mot de passe d'email:", width=21, font="Helvetica 15 bold")
	labelMDP.place(x=0, y=100)
	motdepasse = StringVar()
	MDP = Entry(reportf, textvariable = motdepasse, width = 21, font="Helevetica 15 bold", justify=CENTER)
	MDP.place(x=280, y=100)

	labelreport2 = Label(reportf, text= "Indiquez de ce coté l'erreur rencontrée:", font = "Helvetica 15 bold")
	labelreport2.place(x=0, y=175)
	sujetext1 = StringVar()
	sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font="Helvetica 15 bold", justify=CENTER)
	sujet1.place(x=200, y=200)

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
menubar = Menu(fenetre)# on creer une barre de menu

menu1 = Menu(menubar, tearoff=0)#on crées un premier boutton pour le menu
menu1.add_command(label="Quitter", command=fenetre.destroy)# on crées un boutton qui ferme le programme
menubar.add_cascade(label="Fichier", menu=menu1)# on crées un nom au premier boutton du menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Graphique", command=menu_graphf)
menubar.add_cascade(label="Progression", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos")# on crées un boutton qui ouvre une fenêtre alerte
menu3.add_command(label="Reporter un bug", command=reportf)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)# on configure la barre de menu
#--------------------------------------------------------------------------------------------------------------
##fonction ouverture
def batjeu1():
	os.chdir("C:\\Users\\Anonymed\\Desktop\\BAC")
	os.system("jeu_calcul_mental.py")

#--------------------------------------------------------------------------------------------------------------
##bouton menu
imageb1calc= PhotoImage(file="image/nuage_title-jeu.png")
boutonreni=Button(fenetre, text="", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#0076BB", image=imageb1calc, bg="#00a2ff", command=batjeu1)
boutonreni.place(x=10, y=180)

=======
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import os
import sys
import time
from time import time, sleep
import random
from threading import Thread
#--------------------------------------------------------------------------------------------------------------
fenetre = Tk()
fenetre.configure(width=550, height=400)
fenetre.title("Jeux de réflexion et de logique")
fenetre.resizable(width=False, height=False)

#--------------------------------------------------------------------------------------------------------------
##image menu
textitlemenu=PhotoImage(file="image/nuage_title-menu.png")
canttml = Canvas(fenetre, width=500,height=145)
canttml.create_image(0,0,anchor='nw', image=textitlemenu)
canttml.place(x=115, y=20)

gif_parle=PhotoImage(file="image/einstein_montre.gif")
can1 = Canvas(fenetre, width=120,height=135)
can1.create_image(0,0,anchor='nw', image=gif_parle)
can1.place(x=10, y=0)

gif_parle2=PhotoImage(file="image/einstein_montre.gif")
can2 = Canvas(fenetre, width=120,height=135)
can2.create_image(0,0,anchor='nw', image=gif_parle2)
can2.place(x=450, y=0)

ind = -1
def update(delay=200):
    global ind
    ind += 1
    if ind == 8: ind = 0
    gif_parle.configure(format="gif -index " + str(ind))
    gif_parle2.configure(format="gif -index " + str(ind))
    fenetre.after(delay, update)
update()
#--------------------------------------------------------------------------------------------------------------
##fonction menu
def menu_graphf():
	menu_graphf=Toplevel()
	menu_graphf.configure(width=350,height=200)# on regle la taille de la fenetre
	menu_graphf.title("Graphique")# on donne un nom a notre fenetre
	menu_graphf.resizable(width=False, height=False)# fonction qui évite le redimensionnement

def reportf():
	reportf=Toplevel()
	reportf.configure(width=350, height=200)
	reportf.title("Reporter un bug")
	reportf.resizable(width=False, height=False)

	labelrepor1 = Label(reportf, text="E-mail :", font = "Helvetica 15 bold")# créer un label avec une police définit
	labelrepor1.place(x=5, y=60)# coordonnées du label
	emmailbox1 = StringVar()
	emmail1 = Entry(reportf, textvariable = emmailbox1, width=21, font="Helvetica 15 bold", justify=CENTER)
	emmail1.place(x=90, y=60)

	sujetext1 = StringVar()
	sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font="Helvetica 15 bold", justify=CENTER)
	sujet1.place(x=5, y=100)

	fromaddr = emmailbox1
	toaddrs  = 'dylan.wolverine@gmail.com'
	msg = sujetext1

#--------------------------------------------------------------------------------------------------------------
##menubar menu
menubar = Menu(fenetre)# on creer une barre de menu

menu1 = Menu(menubar, tearoff=0)#on crées un premier boutton pour le menu
menu1.add_command(label="Quitter", command=fenetre.destroy)# on crées un boutton qui ferme le programme
menubar.add_cascade(label="Fichier", menu=menu1)# on crées un nom au premier boutton du menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Graphique", command=menu_graphf)
menubar.add_cascade(label="Progression", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos")# on crées un boutton qui ouvre une fenêtre alerte
menu3.add_command(label="Reporter un bug", command=reportf)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)# on configure la barre de menu
#--------------------------------------------------------------------------------------------------------------
##fonction ouverture
def batjeu1():
	os.chdir("C:\\Users\\Anonymed\\Desktop\\BAC")
	os.system("jeu_calcul_mental.py")

#--------------------------------------------------------------------------------------------------------------
##bouton menu
imageb1calc= PhotoImage(file="image/nuage_title-jeu.png")
boutonreni=Button(fenetre, text="", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#0076BB", image=imageb1calc, bg="#00a2ff", command=batjeu1)
boutonreni.place(x=10, y=180)

>>>>>>> Stashed changes
fenetre.mainloop()