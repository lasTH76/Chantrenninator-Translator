import os
os.chdir('C:\Python34')
# -*- coding: Unicode -*-
fA = open('VocaAnglais.txt', 'r')
fF = open('VocaFrancais.txt', 'r')

lstA = fA.readlines()
lstF = fF.readlines()

print(lstA)

fA.close()
fF.close()
