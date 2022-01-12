from flatten import *

#On créé nos listes
a = [1,2,3,4,5,6,7,8,9,10]
b = [1, [2,3], [4, [5,6, [7,8,9]]], 10]
c = [[[[[[[[1,2,3,4], [5,[6,7,8]]]]]]]], 9, 10]
d = [[], [1,2,3], [[]], 4,5,6,[[[7,8]]], 9, [10]]

#Test des méthodes
print(flatten_recursif(a))
print(flatten_recursif_short(a))
print(flatten_recursif(b))
print(flatten_recursif_short(b))
print(flatten_recursif(c))
print(flatten_recursif_short(c))
print(flatten_recursif(d))
print(flatten_recursif_short(d))

#Test de flatten
e = [[1,2,3], [4,5,6], [7,8,9,10]]
f = [[1,2],[3,4],[5,6], [7,8], [9,10]]
print(flatten(e))
print(flatten(f))