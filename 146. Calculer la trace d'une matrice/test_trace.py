from trace_matrice import trace
import numpy as np

#On créé nos matrices de test
A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[0,1], [2,3]]
I = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
C = [[1,2,3], [4,5,6]]
D = [[0,1], [4,6], [10,11]]
E = [[1,2], [3,4], [5,6]]

#On teste notre méthode trace()
print("Trace de A :", trace(A))
print("Trace de A :", np.trace(np.array(A)))
print("Trace de B :", trace(B))
print("Trace de B :", np.trace(np.array(B)))
print("Trace de I :", trace(I))
print("Trace de I :", np.trace(np.array(I)))
print("Trace de C :", trace(C))
print("Trace de C :", np.trace(np.array(C)))
print("Trace de D :", trace(D))
print("Trace de D :", np.trace(np.array(D)))
print("Trace de E :", trace(E))
print("Trace de E :", np.trace(np.array(E)))