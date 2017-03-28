#majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # de 65 à 90 #
#minuscules = 'abcdefghijklmnopqrstuvwxyz' # de 97 à 122 #
#ponctuations = (.!? ) avec un code ASCII de 46, 33, 63 et 32 #



chaine = input("Entrez la phrase à coder : ")
décalage = int(input("Décalage du message : "))

while décalage > 26:
    décalage = décalage - 26

for car in chaine:
    if ord(car) > 64 and ord(car) < 91:
        césar = ord(car) + décalage
        if césar > 90:
            césar = césar - 26
    elif ord(car)>96 and ord(car)< 123:
        césar = ord(car) + décalage
        if césar > 122:
            césar = césar - 26
    else:
        césar = ord(car)
    print( chr(césar), end = "")
