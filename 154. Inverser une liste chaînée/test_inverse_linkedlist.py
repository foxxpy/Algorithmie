from linkedlist import LinkedList

l = LinkedList()

#On ajoute 10 éléments à notre liste chaînée
for i in range(1, 10):
    l.add(i)

print("---- Liste chaînée 1 ----")
l.traverse_list()
print("Inverse de la liste")
l.inverse()
l.traverse_list()

l2 = LinkedList()
l2.add(1)
l2.add(2)
print("---- Liste chaînée 2 ----")
l2.traverse_list()
l2.inverse()
l2.traverse_list()

l3 = LinkedList()
l3.add(1)
print("---- Liste chaînée 3 ----")
l3.traverse_list()
l3.inverse()
l3.traverse_list()