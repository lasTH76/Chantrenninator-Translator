from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import os
import sys
from time import time, sleep
import random
from threading import Thread
#----------------------------------------------------
##fenetre de configuration
jeu1 = Tk()
jeu1.configure(width=300, height=300)
jeu1.title("Calcul mental")
jeu1.resizable(width=False, height=False)
#-----------------------------------------------------
##9000
def nombre():
	global nbmin, nbmax
	top1=Toplevel()
	top1.configure(width=450,height=200)# on regle la taille de la fenetre
	top1.title("Nombres")# on donne un nom a notre fenetre
	top1.resizable(width=False, height=False)# fonction qui évite le redimensionnement
	labeltop1 = Label(top1, text="Nombres", font = "Helvetica 22 bold")# créer un label avec une police définit
	labeltop1.place(x=45, y=0)# coordonnées du label

	labelnb1 = Label(top1, text="Borne minimale", font="Helvetica 15 bold")
	labelnb1.place(x=20, y=50)
	var_textop1 = StringVar()# récupère valeur des dents du plateau
	ligne_textop1 = Entry(top1, textvariable = var_textop1, width=10)# créer une textbox de longueur 30
	ligne_textop1.place(x=20, y=80)# coordonnées du textbox
#-----------------------------------------------------
##menu
menubar = Menu(jeu1)# on creer une barre de menu

menu1 = Menu(menubar, tearoff=0)#on crées un premier boutton pour le menu
menu1.add_command(label="Quitter", command=jeu1.destroy)# on crées un boutton qui ferme le programme
menubar.add_cascade(label="Fichier", menu=menu1)# on crées un nom au premier boutton du menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Nombres", command=nombre)
menu2.add_command(label="Temps")
menubar.add_cascade(label="Configuration", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Help")
menu3.add_cascade(label="A propos", menu=menu3)

jeu1.config(menu=menubar)# on configure la barre de menu
#-----------------------------------------------------
##Image
validato = PhotoImage(file="null.png")# on ajoute une photo au programme pour la devanture
canvas = Canvas(jeu1,width=30, height=30)# on régle la taille alloué pour l'image
canvas.create_image(0, 0, anchor=NW,image=validato)
canvas.place(x=180, y=180)
#-----------------------------------------------------
score1=0
part1=0
partdef=10
operateurs=["X", "+", "-"]
t=0
touche=
#---------------------------------------------------------
##calcul
class The_time(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		global temps1, bouton1, tmp
		tmp=30
		while tmp!=0:
			temps1['text']=str("Time : ")+str(tmp)
			tmp=tmp-1
			sleep(1)
		bouton1["state"]="disabled"

def resultat():
	global part1,opera1,a,b,c,reponsa,score1, t
	try:
		if t==0:
			Timone = The_time()
			Timone.start()
			t=1
		else:
			t=1
		repon1=str(reponse.get())
		if opera1==0:
			tot=a*b
		elif opera1==1:
			tot=a+b
		else:
			tot=a-b
		if str(repon1)==str(tot):
			validato.config(file="valide2.png")
			score1+=1
			labscore['text']=str("Point : ")+str(score1)
		else:
			validato.config(file="faux2.png")
		tot2['text']=str("Résultat : ")+str(tot)
	except ValueError:
		showerror("Erreur", "Incorrect")
	part1+=1
	a=random.randint(0,10)
	b=random.randint(0,10)
	c=random.choice(operateurs)
	opera1=operateurs.index(c)
	calcul1['text'] = str(a)+str(c)+str(b)
	reponsa.delete(0, END)
#----------------------------------------------------------
labelt1=Label(jeu1, text="Répondre le plus vite possible", font = "Helvetica 15 bold")
labelt1.place(x=5, y=0)

tot2=Label(jeu1, text="Résultat : ", font = "Helvetica 20 bold")
tot2.place(x=20, y=220)

calcul1=Label(jeu1, text="", font = "Helvetica 20 bold")
calcul1.place(x=120, y=80)

a=random.randint(0,10)
b=random.randint(0,10)
c=random.choice(operateurs)
opera1=operateurs.index(c)
calcul1['text'] = str(a)+str(c)+str(b)

labscore=Label(jeu1, text="Point : ", font = "Helvetica 20 bold")
labscore.place(x=20, y=260)

reponse = StringVar()
reponsa = Entry(jeu1, textvariable = reponse, width=21, font="Helvetica 15 bold", justify=CENTER)
reponsa.place(x=30, y=140)
reponsa.bind("<Return>", resultat)

bouton1=Button(jeu1, text="Entrer", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=resultat)# créer un boutton de longueur 200 et largeur 10 avec une ccouleur plus grise quand le bouton est pressé
bouton1.place(x=120, y=180)

temps1=Label(jeu1, text="Time : ", font = "Helvetica 15 bold")
temps1.place(x=5, y=180)

jeu1.mainloop()