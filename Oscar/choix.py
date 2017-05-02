from tkinter import *
import tkinter as tk
import random
#-------------------------------------------

windo = Tk()
windo.configure(width=600, height=375)
windo.title("trouve la capitale")
windo.resizable(width=False, height=False)
#------------------------------------------
def France():
    global paysEurope, capitaleEurope 
    
def Europe():
    global paysEurope, capitaleEurope, nombre, RP,compteur_essai, correct, choix, reponse
    for loop in range(nombre):
        RP=randint(0,26-loop)
        correct=False
        compteur_essai = 0
        while correct==False and compteur_essai != 3:
            print("Quelle est la capitale de ce pays : ",paysEurope[RP])
            choix=reponse
            if choix ==capitaleEurope[RP]:
                print("tu as donné la bonne réponse!")
                correct=True
                compteur_essai = 3
                Nbreussite=Nbreussite+1
            elif choix != copie_capitale[RP] and compteur_essai < 3 :
                print("C'est faux")
                correct=False
                compteur_essai = compteur_essai + 1
        copie_pays.remove(copie_pays[RP])
        copie_capitale.remove(copie_capitale[RP])


        
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
menu1.add_command(label="France")
menu1.add_command(label="Europe")
menubar.add_cascade(label="Choi de la Region",menu=menu1)

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

nombre=5
RP=""
correct=False
#-----------------------------------------
#on fait l'interface graphic

reponse = StringVar()
reponsa = Entry(windo, textvariable = reponse, width=21, font="Helvetica 15 bold", justify=CENTER)
reponsa.place(x=205, y=160)

boutonreni=Button(windo, text="Valider", padx=8, pady=3, font = "Helvetica 10 bold", relief=GROOVE, activebackground="#A4A4A4")
boutonreni.place(x=270, y=200)

tot2=Label(windo, text="", font = "Helvetica 20 bold")
tot2.place(x=250, y=120)

tot3=Label(windo, text="", font = "Helvetica 20 bold")
tot3.place(x=250, y=90)

nbreponce=Label(windo, text="il te restse 3 essais", font = "Helvetica 20 bold")
nbreponce.place(x=250, y=120)
#-----fin
windo.mainloop()
