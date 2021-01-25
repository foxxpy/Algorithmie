#Remove : retire un élément spécifique de la liste
liste = ["a", "b", "c", "d", "e", "f"]
liste.remove("b")
print(liste)

#pop : retire un élément à un indice spécifique
liste = ["a", "b", "c", "d", "e", "f"]
liste.pop(2) #retire le c
print(liste)

#del : supprime un élément à un indice spécifique, mais ce n'est pas une méthode appartenant à la classe List.
liste = ["a", "b", "c", "d", "e", "f"]
del liste[3] #retire le d
print(liste)
