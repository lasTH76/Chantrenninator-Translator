from tkinter import *
from tkinter.messagebox import *
import traducteur as trad
import JeuMorse as morse

fenetre1 = Tk()
fenetre1.title('Jeux de traductions Morse et Fr/An')

def fenetre():
    global fenetre2
    fenetre2 = Toplevel()

def alert():
    showinfo("alerte", "Bravo")

def parametre():
    pass

menubarre = Menu(fenetre1)

menu1 = Menu(menubarre, tearoff=0)
menu1.add_command(label="Paramètres", command = parametre)
menu1.add_command(label='Scores', command = alert)
menu1.add_separator()
menu1.add_command(label='Quitter', command = fenetre1.quit)
menubarre.add_cascade(label='Fichier', menu=menu1)

fenetre1.config(menu=menubarre)

fenetre1.resizable(False, False)

Bouton1 = Button(fenetre1, text = 'Jeu de traduction Fr/An', command = fenetre)
Bouton2 = Button(fenetre1, text = 'Jeu de morse', command = fenetre)
Bouton1.pack(side=LEFT, padx=6, pady=6)
Bouton2.pack(side=RIGHT, padx=6, pady=6)

fenetre1.mainloop()

if fenetre1.quit :
    fenetre1.destroy()
