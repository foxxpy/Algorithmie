from linkedlist import LinkedList

l1 = LinkedList()

print("On créé une première liste chaînée de 20 éléments et on échange ses pairs de valeurs")
for i in range(1, 21):
    l1.add(i)

l1.traverse_list()
l1.swap_pairs()
l1.traverse_list()
l1.display_first_last()
print()

print("On créé une deuxième liste chaînée avec un nombre impair d'élément")
l2 = LinkedList()
for i in range(1, 12):
    l2.add(i)

l2.traverse_list()
l2.swap_pairs()
l2.traverse_list()
l2.display_first_last()
print()

print("Swap sur une liste chaînée de taille 1")
l3 = LinkedList()
l3.add(1)
l3.traverse_list()
l3.swap_pairs()
l3.traverse_list()
l3.display_first_last()
print()

print("Swap sur une liste chaînée de taille 2")
l4 = LinkedList()
l4.add(1)
l4.add(2)
l4.traverse_list()
l4.swap_pairs()
l4.traverse_list()
l4.display_first_last()
print()