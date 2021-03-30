from romain_vers_entier import romain_vers_entier
from entier_vers_romain import entier_vers_romain

#Pour tester notre méthode romain_vers_entier, on convertit d'abord des entiers en romain
#Puis on vérifie si notre méthode réussit à les reconvertir en nombre entier

romain = []
for i in range(1,101):
    romain.append(entier_vers_romain(i))

for i in range(1010,1199):
    romain.append(entier_vers_romain(i))

for rom in romain:
    print(romain_vers_entier(rom))

