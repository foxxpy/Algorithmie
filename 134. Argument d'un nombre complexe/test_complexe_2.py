from complexe_2 import *
import cmath, math

#On créé nos nombres complexes
z1 = (1,1)
z2 = (0, 1)
z3 = (-1, -1)
z4 = (-1, 0)

#On calcule l'argument des nombres complexes précédents
print(argument_complexe(z1))
print(math.degrees(cmath.phase(1+1j)))
print("-----")

print(argument_complexe(z2))
print(math.degrees(cmath.phase(1j)))
print("-----")

print(argument_complexe(z3))
print(math.degrees(cmath.phase(-1-1j)))
print("-----")

print(argument_complexe(z4))
print(math.degrees(cmath.phase(-1-0j)))