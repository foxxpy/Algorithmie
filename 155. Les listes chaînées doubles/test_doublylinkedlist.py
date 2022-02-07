from doublylinkedlist import DoublyLinkedList

dl = DoublyLinkedList()

#Ajout de 2,3,4
print("Ajout de 2,3,4")
dl.add(2)
dl.add(3)
dl.add(4)
dl.traverse_list()
dl.display_first_last()
print()

#Ajout de 2 au début, 6 à la fin, puis on retire le 6 et on retire le 2 au début
print("Ajout de 2 au début, 6 à la fin")
dl.add_first(2)
dl.add(6)
dl.traverse_list()
dl.display_first_last()
print()

print("On retire le 6 et le 2 au début")
dl.remove_last()
dl.remove_first()
dl.traverse_list()
dl.display_first_last()
print()

#On ajoute le 1 au début, le 5 à la fin
print("On ajoute le 1 au début, le 5 à la fin")
dl.add_first(1)
dl.add(5)
dl.traverse_list()
dl.display_first_last()
print()

#On ajoute le 6, puis le 8, puis le 10
print("On ajoute le 6, puis le 8, puis le 10")
dl.add(6)
dl.add(8)
dl.add(10)
dl.traverse_list()
dl.display_first_last()
print()

#On insère le 7 à l'indice 6 et le 9 à l'indice 8
print("On insère le 7 à l'indice 6 et le 9 à l'indice 8")
dl.insert(6, 7)
dl.traverse_list()
dl.insert_after(7, 9)
dl.traverse_list()
dl.display_first_last()
print()


print("Noeud à l'indice 5 :", dl.get_node(5)._item)
print("Noeud à l'indice 0 :", dl.get_node(0)._item)
print("Noeud à l'indice 9 :", dl.get_node(9)._item)
print("Longueur de la liste chaînée double :", dl.length())
print("Est vide?", dl.is_empty())
dl.display_first_last()

print()
print("On retire le 10")
dl.remove(10)
dl.traverse_list()
dl.display_first_last()
print()