chaine = input("Entrez la phrase à binariser : ")

for car in chaine:
    binaire = bin(ord(car))
    print(binaire[2:], end= " ")
