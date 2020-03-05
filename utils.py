#!/net/apps/anaconda3/bin/python


## Définition de la fonction qui renvoie une matrice de même taille que Z contenant le nombre de voisins de chaque élément


def calcul_nb_voisins(Z):
    forme= len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]  # Créé une matrice N de 0 de taille forme[0] * forme[1]
    for x in range(1, forme[0] -1):                    # Calcul du nombre de voisins
        for y in range(1, forme[1] - 1):               # Le " + 0 " est nécessaire si tous les voisins sont morts
            N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] + Z[x-1][y] + 0 + Z[x+1][y] + Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
    return N                     

import numpy as np


Z =[[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
Z 


N = calcul_nb_voisins(Z)
N