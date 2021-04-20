from monnaie import monnaie, calcul_montant_rendu, diram

prix = 100.50
paiement = 120.00
print(monnaie(prix,paiement))
print("Monnaie rendu : {}".format(calcul_montant_rendu(monnaie(prix,paiement))))
print()

#Le client a payé le montant exact
prix = 120.00
paiement = 120.00
print(monnaie(prix,paiement))
print()

#Le client n'a pas assez d'argent
prix = 150
paiement = 140
print(monnaie(prix,paiement))
print()

prix = 2010.50
paiement = 3000
print(monnaie(prix,paiement))
print("Monnaie rendu : {}".format(calcul_montant_rendu(monnaie(prix,paiement))))
print()
