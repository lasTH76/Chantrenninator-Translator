import os,sys

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

lstA = [line.split('/n') for line in fA.readlines()]
lstF = [line.split('/n') for line in fF.readlines()]

print(lstA)

fA.close()
fF.close()
