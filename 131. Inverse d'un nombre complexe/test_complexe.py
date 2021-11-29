#On importe la classe Complexe du module complexe
from complexe import Complexe

#On créé nos nombres complexes
z1 = Complexe(1, 1)
z2 = Complexe(3, 0)
z3 = Complexe(0, -2)
z4 = Complexe(4, 3)
z5 = Complexe(-3, -2)

#On affiche l'inverse des nombres complexes
print(z1.inverse())
print(z2.inverse())
print(z3.inverse())
print(z4.inverse())
print(z5.inverse())