import os, random
os.chdir('C:\Python34')

fA = open('VocaAnglais.txt', 'r')
fF = open('VocaFrancais.txt', 'r')

listfF = [line.split('\n') for line in fF.readlines()]
listfA = [line.split('\n') for line in fA.readlines()]

print("Bienvenue dans ce jeu de traduction mon jeune ami. Comment t'appelles-tu? ")
prenom = input("Veuillez le renseigner de ce côté --> ")
print("Très bien mon jeune ", prenom, " .")
print("Tu vas maintenant avoir 15 mots à traduire.")

print(len(listfF))

fA.close()
fF.close()
