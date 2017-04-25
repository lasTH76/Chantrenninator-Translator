import os, random, sys, time

#os.chdir('C:\Python34')

def SearchPath():
	if getattr(sys, 'frozen', False):
		datadir = os.path.dirname(sys.executable)
	else:
		datadir = os.path.dirname(__file__)
	return datadir


chemin = SearchPath()
CheminAbsolu = os.path.join(chemin, "Chantrenninator-Translator")

fA = open(os.path.join(chemin, 'VocaAnglais.txt'), 'r')
fF = open(os.path.join(chemin, 'VocaFrancais.txt'), 'r')

listfF = [line.split("/n") for line in fF.readlines()]
listfA = [line.split("/n") for line in fA.readlines()]

score = 0
nbrEssai = 5
choix = "Vide"
ReponseJoueur = "mouais"
nbMot = 0

print("Bienvenue dans ce jeu de traduction mon jeune ami. Comment t'appelles-tu? ")
prenom = input("Veuillez le renseigner de ce côté -->   ")
print("Très bien mon jeune", prenom, ".")

while nbMot <= 4:
	nbMot = int(input("Indiquer le nombre de mots que vous voulez traduire -->   "))
	if nbMot > 0 and nbMot < 5:
		print("Petit Joueur.", end='\n')

print("Tu vas maintenant avoir", nbMot, "mots à traduire.")
print("Fais attention il n'y a pas d'accent.")
print("Maintenant, dans quelle langue veux-tu jouer?")


def repareMot(mot):
	listeNouvMot = []
	ignoreSuivant = False
	for indLettre in range(len(mot)):
		if ignoreSuivant:
			ignoreSuivant = False
			pass
		elif (mot[indLettre] in ("[", "]", "'")):
			pass
		elif mot[indLettre] == chr(92) and mot[indLettre + 1] == "n":
			ignoreSuivant = True
			pass
		else:
			listeNouvMot.append(mot[indLettre])
	nouveauMot = "".join(listeNouvMot)
	nouveauMot.replace("\n", "")
	if nouveauMot.endswith("\n"):
		vraiMot = nouveauMot[:-1] #On enleve le dernier caractere (= saut de ligne) pour eviter les sauts de lignes inutiles
	else:
		vraiMot = nouveauMot
	return vraiMot

while not choix in ("Francais", "Anglais"):
	choix = input("Francais ou Anglais?    ")
	if choix == "Francais":
		print("Il faut les traduire en anglais")
		for loop in range(nbMot):
			hasard = random.randint(0, len(listfF))
			mot = repareMot(listfF[hasard])
			reponse = repareMot(listfA[hasard])
			reponse.lower()
			print(mot, end='\n')
			while ReponseJoueur != reponse and nbrEssai > 0:
				ReponseJoueur = input()
				if ReponseJoueur != reponse:
					nbrEssai += -1
					print("Il vous reste", nbrEssai, "essais.", end= '\n')
					print("")
				if ReponseJoueur == reponse and nbrEssai >= 0:
					score += 1
					print("")
					break
			if nbrEssai == 0 and ReponseJoueur != reponse:
				print("La reponse était", reponse,".")
				print()
			nbrEssai = 5


	if choix == "Anglais":
		print("Il faut les traduire en francais")
		for loop in range(nbMot):
			hasard = random.randint(0, len(listfA))
			mot = repareMot(listfA[hasard])
			reponse = repareMot(listfF[hasard])
			reponse.lower()
			print(mot, end='\n')
			while ReponseJoueur != reponse and nbrEssai > 0:
				ReponseJoueur = input()
				if ReponseJoueur != reponse:
					nbrEssai += -1
					print("Il vous reste", nbrEssai, "essais.", end= '\n')
					print("")
				if ReponseJoueur == reponse and nbrEssai >= 0:
					score += 1
					print("")
					break
			if nbrEssai == 0 and ReponseJoueur != reponse:
				print("La reponse était", reponse,".")
				print()
			nbrEssai = 5

print(prenom, ",vous avez un score de",score,"sur",nbMot)


fA.close()
fF.close()
time.sleep(1)
