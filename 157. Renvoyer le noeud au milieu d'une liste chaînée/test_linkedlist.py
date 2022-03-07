from linkedlist import LinkedList

l = LinkedList()

print("Renvoie le noeud central d'une liste chaînée de longueur 5 (longueur impaire)")
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.traverse_list()
print(l.get_middle_node()._item)
print()

print("Renvoie le noeud central d'une liste chaînée de taille 20 (longueur paire)")
l1 = LinkedList()
for i in range(1, 21):
    l1.add(i)
l1.traverse_list()
print(l1.get_middle_node()._item)

print("Renvoie le noeud central d'une liste chaînée de longueur 1")
l2 = LinkedList()
l2.add(5)
l2.traverse_list()
print(l2.get_middle_node()._item)