from tkinter import *
import traducteur as trad
import JeuMorse as morse

fenetre1 = Tk()
fenetre1.title('Jeux de traductions Morse et Fr/An')

def fenetre():
    global fenetre2
    fenetre2 = Toplevel()

Bouton1 = Button(fenetre1, text = 'Jeu de traduction Fr/An', command = fenetre)
Bouton2 = Button(fenetre1, text = 'Jeu de morse', command = fenetre)
Bouton1.pack()
Bouton2.pack()

fenetre1.mainloop()
