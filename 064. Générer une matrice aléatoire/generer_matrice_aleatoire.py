from random import randint

def afficher_matrice(matrice):
    """Affiche la matrice dans la console"""
    
    for line in matrice:
        print(line)

        

def generer_matrice_aleatoire(M, N, inf=1, sup=100):
    """Génère une matrice avec des nombres aléatoire"""

    matrix = []

    for i in range(M):
        line = []
        for j in range(N):
            line.append(randint(inf, sup))
        matrix.append(line)

    return matrix
