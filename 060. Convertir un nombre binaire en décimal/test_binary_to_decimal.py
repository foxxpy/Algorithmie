from binary_to_decimal import *

#On convertit les 100 premiers nombres binaires en nombres décimaux
for i in range(100):
    i = bin(i)
    print(binary_to_decimal(i))
