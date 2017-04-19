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

listfF = [line.split("/n") for line in fF.readlines()]
listfA = [line.split("/n") for line in fA.readlines()]

score = 0
nbrEssai = 0

print("Bienvenue dans ce jeu de traduction mon jeune ami. Comment t'appelles-tu? ")
prenom = input("Veuillez le renseigner de ce côté --> ")
print("Très bien mon jeune", prenom, ".")
print("Tu vas maintenant avoir 15 mots à traduire.")
print("Fais attention aux accents.")
print("Maintenant, dans quelle langue veux-tu jouer?")
choix = input("Français ou Anglais?    ")

if choix == "Français":
   print("Il faut les traduire en anglais")
   
   for loop in range(15):
      hasard = random.randint(0, len(listfF))
      mot = listfF[hasard]
      print(str(mot))

if choix == "Anglais":
   print("Il faut les traduire en français")
   

else:
   while not("Français") or not("Anglais"):
      choix

fA.close()
fF.close()
