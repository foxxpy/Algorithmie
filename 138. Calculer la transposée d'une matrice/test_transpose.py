from transpose import *

#On créé nos matrices de test
A = [[1,2,3], [4,5,6]] # matrice 2x3
B = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]] # matrice 4x5
C = [[1,2], [3,4], [5,6], [7,8], [9,10]] # matrice 5x2

#On teste la méthode tranpose()
print(transpose(A))
print(transpose(B))
print(transpose(C))