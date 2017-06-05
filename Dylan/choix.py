from tkinter import *
import tkinter as tk
import random
import copy, time
#-------------------------------------------

windo = Toplevel()
windo.configure(width=800, height=375)
windo.title("Trouve la capitale")

#------------------------------------------

modeJeu = "Europe"
aClique = False

def reinitialise():
    global Capitale
    global Region
    Capitale=copy.copy(capitaleEurope)
    Region=copy.copy(paysEurope)

def changeMode(nouvMode):
    global modeJeu
    modejeu = nouvMode

def France():
    global paysEurope, capitaleEurope

def Monde():
    pass
    
def Europe():
    global paysEurope, capitaleEurope, nombre, RP, compteur_essai, correct, choix, Nbreussite, Capitale, Region, nbreponce
    Capitale=copy.copy(capitaleEurope)
    Region=copy.copy(paysEurope)
    try:
        nbreponce.destroy()
    except:
        pass
        
    for loop in range(nombre):
        RP=random.randint(0,26-loop)
        correct=False
        compteur_essai = 3
        if not correct and compteur_essai > 0:
            tot3.config(text = "Quelle est la capitale de ce pays : {}".format(Region[RP]))
            choix= reponse.get()
            if choix == Capitale[RP]:
                tot2.config(text ="tu as donné la bonne réponse!")
                correct=True
                compteur_essai = 3
                Nbreussite=Nbreussite+1
            elif choix != Capitale[RP]:
                tot2.config(text = "C'est faux")
                correct=False
                compteur_essai -= 1
                nbreponce=Label(windo, text="il te reste {} essais".format(compteur_essai), font = "Helvetica 20 bold")
                nbreponce.place(x=210, y=120)
                nbreponce.config(text ="il te reste {} essais".format(compteur_essai))
        
        
def demandePays():
    global paysEurope, capitaleEurope, nombre, RP, compteur_essai, correct, choix, Nbreussite, Capitale, Region, nbreponce
    try:
        nbreponce.destroy()
    except:
        pass
    RP=random.randint(0,len(Capitale))
    correct=False
    compteur_essai = 3
    tot3.config(text = "Quelle est la capitale de ce pays : {} ?".format(Region[RP]))
    nbreponce=Label(windo, text="Il te reste {} essais".format(compteur_essai), font = "Helvetica 20 bold")
    nbreponce.place(x=210, y=120)
    nbreponce.config(text ="Il te reste {} essais".format(compteur_essai))


def Valide():
    global compteur_essai, Nbreussite

    if compteur_essai == 0:
        demandePays()
    else:
        choix= reponse.get()
        if choix == Capitale[RP]:
            tot2.config(text ="Tu as donné la bonne réponse!")
            correct=True
            compteur_essai = 3
            Nbreussite=Nbreussite+1
            time.sleep(0.1)
        else:
            tot2.config(text = "C'est faux")
            correct=False
            compteur_essai -= 1
            nbreponce=Label(windo, text="Il te reste {} essais".format(compteur_essai), font = "Helvetica 20 bold")
            nbreponce.place(x=210, y=120)
            nbreponce.config(text ="Il te reste {} essais".format(compteur_essai))
        if choix == Capitale[RP] or compteur_essai == 0:
            Region.remove(Region[RP])
            Capitale.remove(Capitale[RP])
            demandePays()
            
'''
    global aClique
    aClique = True
'''
    
'''
    if modeJeu == "Europe":
        Europe()
    elif modeJeu == "France":
        France()
    elif modeJeu == "Monde":
        Monde()
    else:
        raise ValueError("Mauvaise valeur pour modeJeu")
'''


        
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
menubar.add_cascade(label="Nombre de questions",menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Règles du jeu")
menubar.add_cascade(label="Aide",menu=menu3)

windo.config(menu=menubar)
#-----------------------------------------
#Variable liste
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
#On fait l'interface graphique

reponse = StringVar()
reponse = Entry(windo, textvariable = reponse, width=21, font="Helvetica 15 bold", justify=CENTER)
reponse.place(x=205, y=160)

boutonreni=Button(windo, text="Valider", padx=8, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4", command = Valide)
boutonreni.place(x=270, y=300)

tot2=Label(windo, text="", font = "Helvetica 20 bold")
tot2.place(x=250, y=200)

tot3=Label(windo, text="", font = "Helvetica 20 bold")
tot3.place(x=150, y=90)

reinitialise()
demandePays()

#nbreponce=Label(windo, text="il te reste " + str(compteur_essai)+ " essais", font = "Helvetica 20 bold")
#nbreponce.place(x=210, y=120)
#-----fin
windo.mainloop()
