def monnaie(prix, paiement):
    """Calcul le rendu de monnaie quand le paiement du client est plus élevé
    que le prix d'achat"""

    if prix >= paiement:
        return 0
    
    rendu = {}
    difference = paiement - prix
    fiduciaire = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.2, 0.1, 0.05, 0.02, 0.01]

    for m in fiduciaire:
        if difference // m > 0:
            rendu[m] = difference // m
            difference = difference % m

    return rendu
            


def calcul_montant_rendu(rendu):
    """Calcul le montant rendu en fonction de la monnaie utilisée"""

    total = 0
    for key, value in rendu.items():
        total += key*value
    return total
