from produit_kronecker import *
import numpy as np

#On créé nos matrices de test
A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,2], [3,4]]
C = [[-1, -2, -3]]


#On teste la méthode produit_kronecker()
print(produit_kronecker(A,B))
print(np.kron(np.array(A), np.array(B)))
print("------------")

print(produit_kronecker(B,A))
print(np.kron(np.array(B), np.array(A)))
print("------------")

print(produit_kronecker(C,A))
print(np.kron(np.array(C), np.array(A)))
print("------------")