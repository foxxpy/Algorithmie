from order_doublon import doublon
from no_order_doublon import enlever_doublon

liste = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5]
liste_nom = ["Sarah", "Sarah", "Sarah", "Antoine", "Filip", "Filip"]
print(doublon(liste))
print(doublon(liste_nom))
print(enlever_doublon(liste))
print(enlever_doublon(liste_nom))
