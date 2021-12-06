from complexe import Complexe
import cmath, math
#On créé nos nombres complexes
z1 = Complexe(1,1)
z2 = Complexe(0, 1)
z3 = Complexe(-1, -1)
z4 = Complexe(-1, 0)

# On calcule l'argument de nos nombres complexes précédents
print(z1.argument())
print(math.degrees(cmath.phase(1+1j)))
print("-----")

print(z2.argument())
print(math.degrees(cmath.phase(1j)))
print("-----")

print(z3.argument())
print(math.degrees(cmath.phase(-1-1j)))
print("-----")

print(z4.argument())
print(math.degrees(cmath.phase(-1-0j)))