from linkedlist import LinkedList
from addition_number_linkedlist import addition_linkedlist

print("Addition de 1000 et 671")
l1 = LinkedList()
l2 = LinkedList()
l1.add(1)
l1.add(0)
l1.add(0)
l1.add(0)
l2.add(6)
l2.add(7)
l2.add(1)
l1.traverse_list()
l2.traverse_list()
node = addition_linkedlist(l1.first, l2.first)
while node:
    print(node._item, end="")
    node = node.next
print()

print("Addition de 11111 et 99999")
l1 = LinkedList()
l2 = LinkedList()
l1.add(1)
l1.add(1)
l1.add(1)
l1.add(1)
l1.add(1)
l2.add(9)
l2.add(9)
l2.add(9)
l2.add(9)
l2.add(9)
l1.traverse_list()
l2.traverse_list()
node = addition_linkedlist(l1.first, l2.first)
while node:
    print(node._item, end="")
    node = node.next
print()