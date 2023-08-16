#Enigme 1 
result=""
fichier = open("text.txt", "r")
for ligne in fichier:
    for mot in ligne.split():
        result = result + chr(int(mot))
print(result)
fichier.close()