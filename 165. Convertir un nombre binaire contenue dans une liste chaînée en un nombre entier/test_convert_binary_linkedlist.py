from convert_binary_linkedlist import get_decimal_value
from linkedlist import LinkedList

print("Conversion de 101 en base décimale")
l1 = LinkedList()
l1.add(1)
l1.add(0)
l1.add(1)
l1.traverse_list()
print("=> ", get_decimal_value(l1))
print()

print("Conversion de 1010 en base décimale")
l2 = LinkedList()
l2.add(1)
l2.add(0)
l2.add(1)
l2.add(0)
l2.traverse_list()
print("=> ", get_decimal_value(l2))
print()

print("Conversion de 1 en base décimale")
l3 = LinkedList()
l3.add(1)
l3.traverse_list()
print("=> ", get_decimal_value(l3))
print()

print("Conversion de 0 en base décimale")
l4 = LinkedList()
l4.add(0)
l4.traverse_list()
print("=> ", get_decimal_value(l4))
print()

