from linkedlist import LinkedList

l1 = LinkedList()
print("Est vide?", l1.is_empty())

#On insère 10 éléments dans la liste chaînée
for i in range(10):
    l1.add(i)

l1.traverse_list()
l1.display_first_last()
print()

print("Longueur :", l1.length())
print("Est vide?", l1.is_empty())
print("Noeud à l'indice 5 :", l1.get_node(5))

print()
print("On ajoute la valeur 50 à l'indice 5")
l1.insert(5, 50)
l1.traverse_list()
l1.display_first_last()

print()
print("On retire le 50")
l1.remove(50)
l1.traverse_list()
l1.display_first_last()

print()
print("On ajoute le 11 et le 10")
l1.insert_after(9, 11)
l1.insert_after(9, 10)
l1.traverse_list()
l1.display_first_last()

print()
print("On insère un 10 après le 5")
l1.insert_after(5, 10)
l1.traverse_list()
l1.display_first_last()

print()
print("On retire le 10 après le 5")
l1.pop(6)
l1.traverse_list()
l1.display_first_last()

print()
print("On retire le 9, le 10 et le 11")
l1.remove(9)
l1.remove_last()
l1.remove_last()
l1.traverse_list()
l1.display_first_last()

print()
print("On retire le 0")
l1.remove(0)
l1.traverse_list()
l1.display_first_last()

print()
print("On retire tous les éléments allant de 1 à 5 inclus.")
for i in range(1, 6):
    l1.remove(i)
l1.traverse_list()
l1.display_first_last()

print()
print("On retire le premier élément")
l1.remove_first()
l1.traverse_list()
l1.display_first_last()

print()
print("On retire le premier élément")
l1.pop(0)
l1.traverse_list()
l1.display_first_last()

print()
print("On retire le premier élément")
l1.pop(0)
l1.traverse_list()
l1.display_first_last()