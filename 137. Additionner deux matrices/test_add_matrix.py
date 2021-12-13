from add_matrix import add_matrix, add_matrix_np, add_matrix_basic

#On créé nos matrices pour les tests
a1 = [[1,2,3], [1,2,3]]
a2 = [[3,2,1], [3,2,1]]

b1 = [[1,2,3,4], [-1,-2,-3,-4], [0,1,0,1]]
b2 = [[1,0,1,0], [1,2,3,4], [-1,-2,-3,-4]]

c1 = [[1]]
c2 = [[4]]

#On affiche les résultats pour add_matrix_basic
print("---- add_matrix_basic ----")
print(add_matrix_basic(a1,a2))
print(add_matrix_basic(b1,b2))
print(add_matrix_basic(c1,c2))

#On affiche les résultats pour add_matrix
print("---- add_matrix_ ----")
print(add_matrix(a1,a2))
print(add_matrix(b1,b2))
print(add_matrix(c1,c2))

#On affiche les résultats pour add_matrix_np
print("---- add_matrix_np ----")
print(add_matrix_np(a1,a2))
print(add_matrix_np(b1,b2))
print(add_matrix_np(c1,c2))