#!/net/apps/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np



def calcul_nb_voisins(Z):
    
    '''Fonction calcul_nb_voisin qui renvoie une matrice de même taille que Z contenant le nombre de voisins de chaque élément de Z '''
    
    
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] -1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] + Z[x-1][y] + 0 + Z[x+1][y] + Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
    return N                     



###


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


###


def calcul_nb_voisins_np(Y):
    
    """Fonction prenant en entrée un numpy array Y
       Calcul la matrice contenant le nombre de voisins de chaque élément de Y
       Utilise les méthodes de slicing"""
    
    nbv = np.zeros(Y.shape)
    nbv[1:-1, 1:-1] = Y[:-2, :-2] + Y[1:-1, :-2] + Y[2:, :-2] \
       + Y[:-2, 1:-1] + 0 + Y[2:, 1:-1] \
       + Y[:-2, 2:] + Y[1:-1, 2:] + Y[2:, 2:]
    
    return (nbv)



###


def iteration_jeu_np(Y):
    
    """Fonction similaire à iteration_jeu qui prend en entrée des numpy array"""
    
   
    forme = Y.shape
    N = calcul_nb_voisins_np(Y)
    for x in range(1, forme[0] -1):
        for y in range(1, forme[1] - 1):
            if Y[x][y] == 1 and (N[x][y]<2 or N[x][y]>3):
                Y[x][y] = 0
            elif Y[x][y] == 0 and N[x][y]==3:
                Y[x][y] = 1
               
    return (Y)
    
###


def jeu_np(Z_ini, nb_iter):
    
    """Fonction admettant en entrée un numpy array Z_in et en sortie la matrice Z après nb_iter itérations du jeu de la vie"""
    
    if (nb_iter==0):
        return(plt.imshow(Z_ini), plt.title("".join("Itération " + str(nb_iter))), plt.axis('off'))
    
    else:
        for i in range(nb_iter-1):
            iteration_jeu_np(Z_ini)
        
    plt.imshow(iteration_jeu(Z_ini))
    plt.title("".join("Itération " + str(nb_iter) + " du jeu de la vie"))
    plt.axis('off')
        
###


def iteration_10(Z):
    
    """Affiche les 10 premières itérations du jeu de la vie pour une matrice Z"""

    fig, axs = plt.subplots(2, 5, figsize=(12,12))
    Y=np.array(Z)

    for i in range(2):
        for j in range(5):
        
            axs[i,j].imshow(Y)
            axs[i,j].set_title("".join("Itération " + str(5*i+j))) # Numero de l'itération
            axs[i,j].axis('off')                                   # Suppression des axes
        
            Y = iteration_jeu(Y)
            
###





 
    