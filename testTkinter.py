from tkinter import *

fenetre = Tk()

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.pack()

champ_label = Label(fenetre, text= "Bien le bonjour.")
champ_label.pack()
fenetre.mainloop()

