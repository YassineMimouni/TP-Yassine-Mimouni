#!/net/apps/anaconda3/bin/python

def calcul_nb_voisins(Z):
    
    '''Fonction calcul_nb_voisin qui renvoie une matrice de même taille que Z contenant le nombre de voisins de chaque élément de Z '''
    
    
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] -1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] + Z[x-1][y] + 0 + Z[x+1][y] + Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
    return N                     



import numpy as np


def iteration_jeu(Z):
    
    '''Fonction itérative qui renvoie la matrice Z après un tour du jeu de la vie
       Fait appel à la fonction calcul_nb_voisin'''    
    
    
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1, forme[0] -1):
        for y in range(1, forme[1] - 1):
            if Z[x][y] == 1 and (N[x][y]<2 or N[x][y]>3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y]==3:
                Z[x][y] = 1
               
    return Z


import matplotlib as plt    
    