from determinant_3 import *

#On créé nos matrices de test
A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[3,0,2], [-1,1,0], [5,2,3]]
C = [[2, 1, 3], [1,0,2], [2,0,-2]]
D = [[1,2,3], [0,4,5], [2,1,9]]
#On teste la méthode determinant_3()
print(determinant_3(A))
print(determinant_3(B))
print(determinant_3(C))
print(determinant_3(D))
