from random import*
pays=["Allemagne", "Autriche" ,"Belgique","Bulgarie","Chypre","Danemark","Espagne","Estonie","Finlande","France","Grèce","Hongrie","Irlande","Italie","Lettonie","Lituanie","Luxembourg","Malte","Pays-Bas","Pologne","Portugal","République-tchèque","Roumanie","Royaume-Uni","Slovaquie","Slovénie","Suède"]
capitale=["Berlin","Vienne","Bruxelles","Sofia","Nicosie","Copenhague","Madrid","Tallinn","Helsinki","Paris","Athènes","Budapest","Dublin","Rome","Riga","Vilnius","Luxembourg","La-Valette","Amsterdam","Varsovie","Lisbonne","Prague","Bucarest","Londres","Bratislava","Ljubljana","Stockholm"]
#print(len(pays))
    
# il ne faut que le même pays tombe deux fois

Nbreussite=0
copie_pays=pays
copie_capitale=capitale

prenom=input("Bonjour ! Quel est ton prénom ?")
print("Dans ce jeu tu devras donner les capitales des pays ou régions demandées.")
print(prenom,"n'oublie pas la majuscule au début de la ville")
print("Tu as trois essais pour chaque question")
nombre=int(input("Entre le nombre de pays à deviner : "))
             
for loop in range(nombre):
    RP=randint(0,26-loop)
    correct=False
    compteur_essai = 0
    while correct==False and compteur_essai != 3:
        print("Quelle est la capitale de ce pays : ",copie_pays[RP])
        choix=input()
        if choix ==copie_capitale[RP]:
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
    
    
print("Tu as au final ",Nbreussite,"bonnes reponses sur", nombre)

#["Auvergne-Rhône-Alpes","Bourgogne-Franche-Comté ","Bretagne","Centre-Val- de-Loire","Corse","Grand_Est","Hauts-De-France », »île-de-France","Normandie", »Nouvelle-Aquitaine","Occitane","pays_de_la_Loire","Provence-Alpes-Côtes_d’Azur","Guadeloupe","Guyane","Martinique","Reunion", »Mayotte »]
#["Lyon", »Dijon,Brest,Orléans,Ajaccio,Strasbourg,Lille,Paris,Rouen,Bordeaux,Toulouse,Nantes,Marseille,Basse-Terre,Fort-de-France,cayenne,Saint-Denis,Dzaoudzi]
