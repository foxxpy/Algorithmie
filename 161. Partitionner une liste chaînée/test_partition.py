from linkedlist import LinkedList
import random

l1 = LinkedList()

print("On créé la liste chaînée : 7, 11, 9, 50, 49, 10, 2")
l1.add(7)
l1.add(11)
l1.add(9)
l1.add(50)
l1.add(49)
l1.add(10)
l1.add(2)
l1.traverse_list()

print("On la partitionne avec la valeur x = 10")
l1_partition = l1.partition(10)
l1_partition.traverse_list()
print()

l2 = LinkedList()
print("On créé une liste chaînée avec des valeurs allant de 1 à 20 mélangées")
shuffled_range = [x for x in range(1,21)]
random.shuffle(shuffled_range)

for i in shuffled_range:
    l2.add(i)
l2.traverse_list()

print("On la partitionne avec la valeur x = 12")
l2_partition = l2.partition(12)
l2_partition.traverse_list()


