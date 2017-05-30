from tkinter import *
import shelve, smtplib

fenetre1 = Tk()
fenetre1.title('Jeux de traductions Morse et Fr/An')

def showScore():
    HScore = shelve.open('score.txt')
    score = HScore['score']

def reportf():
    reportf=Toplevel()
    reportf.configure(width=600, height=300)
    reportf.title('Reporter un bug')
    reportf.resizable(width=False, height=False)

    labelrepor1 = Label(reportf, text='E-mail :', font = 'Helvetica 15 bold')# on crée un label avec une police définie
    labelrepor1.place(x=0, y=0)# coordonnées du label
    emmailbox1 = StringVar()
    emmailbox1.set('@gmail.com')
    email1 = Entry(reportf, textvariable = emmailbox1, width=21, font='Helvetica 15 bold', justify=CENTER)
    email1.place(x=90, y=0)

    labelMDP = Label(reportf, text="Votre mot de passe d'email:", width=21, font='Helvetica 15 bold').place(x=0, y=100)
    motdepasse = StringVar()
    MDP = Entry(reportf, textvariable = motdepasse, width = 21, font='Helevetica 15 bold').place(x=280, y=100)

    labelreport2 = Label(reportf, text= "Indiquez de ce coté l'erreur rencontrée:", font = 'Helvetica 15 bold').place(x=0, y=175)
    sujetext1 = StringVar()
    sujet1 = Entry(reportf, textvariable = sujetext1, width=21, font='Helvetica 15 bold', justify=CENTER)
    sujet1.place(x=200, y=200)

    def ELRport():
                
        fromaddr = emmailbox1.get()
        toaddrs = 'thab3@orange.fr'
        msg = sujetext1.get()
        MDP = motdepasse.get()
                
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr , MDP)

        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        reportf.destroy()

    boutonEnvoi = Button(reportf, text = 'Envoyer le report', command = ELRport).place(x=250, y=250)
        
def créateurs():
    createurs = Toplevel()
    createurs.configure(width = 1666, height = 1666)
    createurs.title('Générique de Fin')
    createurs.resizable(False, False)
    
    labelC1 = Label(createurs, text = 'Ce jeu vous a été présenté par ' + '\n' + 'Tom Habbar, Dylan Essakhi et Oscar Sellier.' + '\n' + "Avec l'aide supplémentaire de Gawein Le Goff et de Erwan Castioni" + '\n' + "A l'occasion du bac d'ISN se déroulant au Lycée Camille Saint-Saens" + '\n' + "En espérant qu'il vous plaise ^^", font='Helvetica 15 bold', justify=CENTER)
    labelC1.pack()

def fenetre():
    pass
##    global fenetre2
##    fenetre2 = Toplevel()

menubarre = Menu(fenetre1)

menu1 = Menu(menubarre, tearoff = 0)
menu1.add_command(label='Scores', command = showScore)
menu1.add_separator()
menu1.add_command(label='Quitter', command = fenetre1.destroy)
menubarre.add_cascade(label='Fichier', menu=menu1)

menu2 = Menu(menubarre, tearoff = 0)
menu2.add_command(label='A propos', command = créateurs)
menu2.add_command(label='Reporter un bug', command=reportf)
menubarre.add_cascade(label='Aide', menu=menu2)

fenetre1.config(menu=menubarre)


fenetre1.resizable(False, False)

Bouton1 = Button(fenetre1, text = 'Jeu de traduction Fr/An', command = fenetre)
Bouton2 = Button(fenetre1, text = 'Jeu de morse', command = fenetre)
Bouton1.pack(side=LEFT, padx=6, pady=6)
Bouton2.pack(side=RIGHT, padx=6, pady=6)

fenetre1.mainloop()
