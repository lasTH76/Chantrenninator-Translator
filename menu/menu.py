from tkinter import *
import tkinter as tk
import os
import sys
import time
import smtplib
import subprocess
#----------------------------------------------------
##fenetre de configuration
fenetre = Tk()
fenetre.configure(width=550, height=400)
fenetre.title("Jeux de réflexion et de logique")
fenetre.resizable(width=False, height=False)

textitlemenu=PhotoImage(file="title_menu.png")
canttml = Canvas(fenetre, width=227,height=62)
canttml.create_image(0,0,anchor='nw', image=textitlemenu)
canttml.place(x=165, y=30)

gif_parle=PhotoImage(file="einstein_montre.gif")
can1 = Canvas(fenetre, width=120,height=135)
can1.create_image(0,0,anchor='nw', image=gif_parle)
can1.place(x=10, y=0)

gif_parle2=PhotoImage(file="einstein_montre.gif")
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
#----------------------------------------------------
##
def graphf():
	graphf=Toplevel()
	graphf.configure(width=350,height=200)# on regle la taille de la fenetre
	graphf.title("Graphique")# on donne un nom a notre fenetre
	graphf.resizable(width=False, height=False)# fonction qui évite le redimensionnement

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

#----------------------------------------------------
##menu
menubar = Menu(fenetre)# on creer une barre de menu

menu1 = Menu(menubar, tearoff=0)#on crées un premier boutton pour le menu
menu1.add_command(label="Quitter", command=fenetre.destroy)# on crées un boutton qui ferme le programme
menubar.add_cascade(label="Fichier", menu=menu1)# on crées un nom au premier boutton du menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Graphique", command=graphf)
menubar.add_cascade(label="Progression", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos")# on crées un boutton qui ouvre une fenêtre alerte
menu3.add_command(label="Reporter un bug", command=reportf)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)# on configure la barre de menu

#-----------------------------------------------------
##bouton
def test():
	subprocess.call("start python jeu1.py")


boutonreni=Button(fenetre, text=" ", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=test)
boutonreni.place(x=180, y=180)

fenetre.mainloop()