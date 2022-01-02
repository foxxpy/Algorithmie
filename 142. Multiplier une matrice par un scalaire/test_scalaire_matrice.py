from scalaire_matrice import *

#On créé nos vecteurs et matrices
v1 = [1,2,3,4,5]
A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,2], [-1, -2]]

#On teste la méthode multiplier_scalaire
print(multiplier_scalaire(v1, 2))
print(multiplier_scalaire(A, -1))
print(multiplier_scalaire(B, 0))