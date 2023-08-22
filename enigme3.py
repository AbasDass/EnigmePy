# on passe en parametre la liste et le plus grand indice
def maximum(liste, k):

    # récuperation de l'indice le plus grand jusqu'à la fin de la liste
    maximum = liste[k]

    #on stock k dans j pour réaliser autrechose
    j = k

    # on choisie le plus grand indice et le reste de la liste, et on le stock dans i
    for i in range(k,len(liste)):
        if liste[i] > maximum :
            maximum = liste[i]
            j = i

    return j



def retourne(liste, x):
    longueur = len(liste)
    for i in range((longueur-x)//2) :
        temp = liste[x+i]
        liste[x+i] = liste [longueur-1-i]
        liste[longueur-1-i] = temp


def tri_crepe(liste):
    for i in range(len(liste)):
        j = maximum(liste,i)
        retourne(liste, j)
        retourne(liste, i)

pile = [7,6,1,3,2,8,9,5,4,]
print(pile)
tri_crepe(pile)
print(pile)
