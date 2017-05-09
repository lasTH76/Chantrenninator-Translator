from tkinter import *
import tkinter as tk
import random
import copy
#-------------------------------------------

windo = Tk()
windo.configure(width=600, height=375)
windo.title("trouve la capitale")

#------------------------------------------

modeJeu = "Europe"

def changeMode(nouvMode):
    global modeJeu
    modejeu = nouvMode

def France():
    global paysEurope, capitaleEurope

def Monde():
    pass
    
def Europe():
    global paysEurope, capitaleEurope, nombre, RP, compteur_essai, correct, choix, Nbreussite, Capitale, Region
    Capitale=copy.copy(capitaleEurope)
    Region=copy.copy(paysEurope)
    for loop in range(nombre):
        RP=random.randint(0,26-loop)
        correct=False
        compteur_essai = 0
        while not correct and compteur_essai < 3:
            tot3.config(text = "Quelle est la capitale de ce pays : {}".format(Region[RP]))
            choix= reponse.get()
            if choix ==Capitale[RP]:
                tot2.config(text ="tu as donné la bonne réponse!")
                correct=True
                compteur_essai = 3
                Nbreussite=Nbreussite+1
            elif choix != Capitale[RP]:
                tot2.config(text = "C'est faux")
                correct=False
                compteur_essai = compteur_essai + 1
                nbreponce=Label(windo, text="il te reste {} essais".format(compteur_essai), font = "Helvetica 20 bold")
                nbreponce.place(x=210, y=120)
                nbreponce.config(text ="il te reste {} essais".format(compteur_essai))
        Region.remove(Region[RP])
        Capitale.remove(Capitale[RP])

def Valide():
    if modeJeu == "Europe":
        Europe()
    elif modeJeu == "France":
        France()
    elif modeJeu == "Monde":
        Monde()
    else:
        raise ValueError("Mauvaise valeur pour modeJeu")


        
def nbquestion1():
    global nombre
    nombre=5
def nbquestion2():
    global nombre
    nombre=10
def nbquestion3():
    global nombre
    nombre=15
def nbquestion4():
    global nombre
    nombre=20
#-----------------------------------------
menubar = Menu(windo)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="France", command = lambda : changeMode("France"))
menu1.add_command(label="Europe", command = lambda : changeMode("Europe"))
menu1.add_command(label = "Monde", command = lambda: changeMode("Monde"))
menubar.add_cascade(label="Choix de la Region",menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="5",command=nbquestion1)
menu2.add_command(label="10",command=nbquestion2)
menu2.add_command(label="15",command=nbquestion3)
menu2.add_command(label="20",command=nbquestion4)
menubar.add_cascade(label="nombre de question",menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="régle du jeu")
menubar.add_cascade(label="aides",menu=menu3)

windo.config(menu=menubar)
#-----------------------------------------
#variable liste
paysEurope=["Allemagne", "Autriche" ,"Belgique","Bulgarie","Chypre","Danemark","Espagne","Estonie","Finlande","France","Grèce","Hongrie","Irlande","Italie","Lettonie","Lituanie","Luxembourg","Malte","Pays-Bas","Pologne","Portugal","République-tchèque","Roumanie","Royaume-Uni","Slovaquie","Slovénie","Suède"]
capitaleEurope=["Berlin","Vienne","Bruxelles","Sofia","Nicosie","Copenhague","Madrid","Tallinn","Helsinki","Paris","Athènes","Budapest","Dublin","Rome","Riga","Vilnius","Luxembourg","La-Valette","Amsterdam","Varsovie","Lisbonne","Prague","Bucarest","Londres","Bratislava","Ljubljana","Stockholm"]

regionFrance=["Auvergne-Rhône-Alpes","Bourgogne-Franche-Comté ","Bretagne","Centre-Val-de-Loire","Corse","Grand_Est","Hauts-De-France", "île-de-France","Normandie","Nouvelle-Aquitaine","Occitane","pays_de_la_Loire","Provence-Alpes-Côtes_d’Azur","Guadeloupe","Guyane","Martinique","Reunion","Mayotte"]
capitaleFrance=["Lyon","Dijon","Brest","Orléans","Ajaccio","Strasbourg","Lille","Paris","Rouen","Bordeaux","Toulouse","Nantes","Marseille","Basse-Terre","Fort-de-France","cayenne","Saint-Denis","Dzaoudzi"]

Region=[]
Capitale=[]

nombre=5
RP=""
correct=False
Nbreussite=0
compteur_essai=0

#-----------------------------------------
#on fait l'interface graphic

reponse = StringVar()
reponse = Entry(windo, textvariable = reponse, width=21, font="Helvetica 15 bold", justify=CENTER)
reponse.place(x=205, y=160)

boutonreni=Button(windo, text="Valider", padx=8, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command = Valide)
boutonreni.place(x=270, y=300)

tot2=Label(windo, text="", font = "Helvetica 20 bold")
tot2.place(x=250, y=200)

tot3=Label(windo, text="", font = "Helvetica 20 bold")
tot3.place(x=150, y=90)

#nbreponce=Label(windo, text="il te reste " + str(compteur_essai)+ " essais", font = "Helvetica 20 bold")
#nbreponce.place(x=210, y=120)
#-----fin
windo.mainloop()
