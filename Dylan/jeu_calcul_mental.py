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
jeu1.configure(width=300, height=350)
jeu1.title("Calcul mental")
jeu1.resizable(width=False, height=False)

textitle=PhotoImage(file="image/nuage_title-jeu.png")
canttl = Canvas(jeu1, width=227,height=62)
canttl.create_image(0,0,anchor='nw', image=textitle)
canttl.place(x=45, y=10)

#-----------------------------------------------------
##9000
def aide():
	top1=Toplevel()
	top1.configure(width=350,height=200)# on regle la taille de la fenetre
	top1.title("Aide")# on donne un nom a notre fenetre
	top1.resizable(width=False, height=False)# fonction qui évite le redimensionnement
	labeltop1 = Label(top1, text="Utilisation du jeu", font = "Helvetica 22 bold")# créer un label avec une police définit
	labeltop1.place(x=45, y=0)# coordonnées du label

def temps():
	global tmpr, score1, t
	#--------------------------------------------------------------------------
	##fonction de la fenetre temps
	def renitial():
		global tmpr, tmp, score1, t
		tmp=0
		tmpr=10
		tmp=tmpr
		score1=0
		t=0
		labeltop2['text']=str("Temps : ")+str(tmp)+str("s")
		temps1['text']=str("Time : ")+str(tmp)
		reponsa.bind("<Return>", resultat)

	def modifitemps():
		global tmpr, tmp, score1, t
		tmp=0
		imnwtime=int(jerenit1.get())
		tmpr=imnwtime
		tmp=tmpr
		score1=0
		t=0
		labeltop2['text']=str("Temps : ")+str(tmp)+str("s")
		temps1['text']=str("Time : ")+str(tmp)
		reponsa.bind("<Return>", resultat)
	#-------------------------------------------------------------------------
	##structure de la fenetre temps
	top2=Toplevel()
	top2.configure(width=200,height=200)# on regle la taille de la fenetre
	top2.title("Temps")# on donne un nom a notre fenetre
	top2.resizable(width=False, height=False)# fonction qui évite le redimensionnement
	labeltop2 = Label(top2, text="Temps : "+str(tmp)+"s", font = "Helvetica 22 bold")# créer un label avec une police définit
	labeltop2.place(x=5, y=0)# coordonnées du label

	labelnb2 = Label(top2, text="Entrez la durée du quizz :", font="Helvetica 10 bold")
	labelnb2.place(x=20, y=50)
	jerenit1 = StringVar()# récupère valeur des dents du plateau
	jerenitlabel = Entry(top2, textvariable = jerenit1, width=10, justify=CENTER, font="Helvetica 15 bold")# créer une textbox de longueur 30
	jerenitlabel.place(x=40, y=80)# coordonnées du textbox
	b1t2=Button(top2, text="Appliquer", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=modifitemps)
	b1t2.place(x=110, y=160)
	b2t2=Button(top2, text="Annuler", padx=15, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=top2.destroy)
	b2t2.place(x=10, y=160)
	b2t2=Button(top2, text="Rénitialiser", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command=renitial)
	b2t2.place(x=50, y=120)

#-----------------------------------------------------
##menu
menubar = Menu(jeu1)# on creer une barre de menu

menu1 = Menu(menubar, tearoff=0)#on crées un premier boutton pour le menu
menu1.add_command(label="Quitter", command=jeu1.destroy)# on crées un boutton qui ferme le programme
menubar.add_cascade(label="Fichier", menu=menu1)# on crées un nom au premier boutton du menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Temps", command=temps)
menubar.add_cascade(label="Configuration", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Aide", command=aide)
menubar.add_cascade(label="A propos", menu=menu3)

jeu1.config(menu=menubar)# on configure la barre de menu
#-----------------------------------------------------
##Image
validato = PhotoImage(file="image/null.png")# on ajoute une photo au programme pour la devanture
canvas = Canvas(jeu1,width=30, height=30)# on régle la taille alloué pour l'image
canvas.create_image(0, 0, anchor=NW,image=validato)
canvas.place(x=250, y=140)
#-----------------------------------------------------
score1=0
part1=0
partdef=10
operateurs=["X", "+", "-"]
t=0
tmp=10
tmpr=10
brack=0
#---------------------------------------------------------
##calcul
class The_time(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.pause=False

	def run(self):
		global temps1, tmp
		while self.pause==False:
			while tmp!=0:
				temps1['text']=str("Time : ")+str(tmp)
				tmp=tmp-1
				sleep(1)
			self.pause=True
				
		reponsa.unbind("<Return>")
		boutonreni.config(state = NORMAL)

	def pause(self):
		self.pause=True
	def resume(self):
		tmp=tmpr
		self.pause=False


def resultat(event):
	global part1,opera1,a,b,c, reponsa,score1, t, tmp, tmpr, Timone
	try:
		if t==0:
			Timone = The_time()
			tmp=tmpr
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
			validato.config(file="image/valide2.png")
			score1+=1
			labscore['text']=str("Point : ")+str(score1)
		else:
			validato.config(file="image/faux2.png")
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

def reniti1():
	global temps1, score1, tmp, tmpr
	t=1
	tmp=tmpr
	temps1['text']=str("Time : ")+str(tmp)
	tot2['text']=str("Résultat : ")
	labscore['text']=str("Point : ")+str(0)
	score1=0
	calcul1['text'] = str(a)+str(c)+str(b)
	boutonreni.config(state = DISABLED)
	reponsa.bind("<Return>", resultat)
	Timone = The_time()
	Timone.start()

#----------------------------------------------------------
#réponder au question avant le temps imparti

tot2=Label(jeu1, text="Résultat : ", font = "Helvetica 20 bold")
tot2.place(x=20, y=220)

calcul1=Label(jeu1, text="", font = "Helvetica 20 bold")
calcul1.place(x=120, y=80)

a=random.randint(0,10)
b=random.randint(0,10)
c=random.choice(operateurs)
opera1=operateurs.index(c)
calcul1['text'] = str(a)+str(c)+str(b)

labscore=Label(jeu1, text="Point : "+str(0), font = "Helvetica 20 bold")
labscore.place(x=20, y=260)

reponse = StringVar()
reponsa = Entry(jeu1, textvariable = reponse, width=21, font="Helvetica 15 bold", justify=CENTER)
reponsa.place(x=10, y=140)
reponsa.bind("<Return>", resultat)

instru1=Label(jeu1, text="Entrez", font = "Helvetica 15 bold")# créer un boutton de longueur 200 et largeur 10 avec une ccouleur plus grise quand le bouton est pressé
instru1.place(x=110, y=180)

boutonreni=Button(jeu1, text="Recommencer", padx=5, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", state=DISABLED, command=reniti1)
boutonreni.place(x=180, y=180)

temps1=Label(jeu1, text="Time : "+str(tmp), font = "Helvetica 15 bold")
temps1.place(x=5, y=180)

labelbstsore=Label(jeu1, text="Votre meilleur score :", font="Helvetica 15 bold")
labelbstsore.place(x=30, y=290)

labelbstsore1=Label(jeu1, text="", font="Helvetica 15 bold")
labelbstsore1.place(x=50, y=315)

jeu1.mainloop()