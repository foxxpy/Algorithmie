from complexe import Complexe

#Instanciation des nombres complexes
real = 0
imaginary = 1
real_2 = 10
imaginary_2 = 1

#Test des méthodes multipliant les nombres complexes
a = Complexe(real, imaginary)
b = Complexe(real_2, imaginary_2)
print(a*b)
print(complex(real,imaginary)*complex(real_2,imaginary_2))
