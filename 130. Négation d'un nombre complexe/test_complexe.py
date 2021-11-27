from complexe import Complexe

#On créé des nombres complexes
z1 = Complexe(1, 2)
z2 = Complexe(-5, -7)
z3 = Complexe(6, 0)
z4 = Complexe(0, -8)

#On teste si la négation fonctionne
print(z1.negation())
print(z2.negation())
print(z3.negation())
print(z4.negation())