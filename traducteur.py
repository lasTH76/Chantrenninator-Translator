import os, random, sys
os.chdir('C:\Python34')

def SearchPath():
   if getattr(sys, 'frozen', False):
      datadir = os.path.dirname(sys.executable)
   else:
      datadir = os.path.dirname(__file__)
   return datadir


chemin = SearchPath()
CheminAbsolu = os.path.join(chemin, "Chantrenninator-Translator")

fA = open('VocaAnglais.txt', 'r')
fF = open('VocaFrancais.txt', 'r')

listfF = [line.split('\n') for line in fF.readlines()]
listfA = [line.split('\n') for line in fA.readlines()]

print("Bienvenue dans ce jeu de traduction mon jeune ami. Comment t'appelles-tu? ")
prenom = input("Veuillez le renseigner de ce côté --> ")
print("Très bien mon jeune ", prenom, " .")
print("Tu vas maintenant avoir 15 mots à traduire.")

lstA = [line.split('/n') for line in fA.readlines()]
lstF = [line.split('/n') for line in fF.readlines()]

print(len(listfF), len(listfA))

fA.close()
fF.close()
