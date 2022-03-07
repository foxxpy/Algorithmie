from inverse_doublylinkedlist import DoublyLinkedList

dl = DoublyLinkedList()

print("Inversion de la liste 1,2,3,4")
dl.add(1)
dl.add(2)
dl.add(3)
dl.add(4)
dl.traverse_list()
dl.inverse()
dl.traverse_list()

print("Inverse d'une liste avec un seul élément")
dl2 = DoublyLinkedList()
dl2.add(2)
dl2.inverse()
dl2.traverse_list()