from doublylinkedlist import DoublyLinkedList

print("On va tester si la liste doublement chaînée [1,3,5,3,1] est palindromique.")
dl1 = DoublyLinkedList()
dl1.add(1)
dl1.add(3)
dl1.add(5)
dl1.add(3)
dl1.add(1)
dl1.traverse_list()
print("Palindrome?", dl1.is_palindrome())
print()

print("On va tester si la liste doublement chaînée [1,3,5,5,3,1] est palindromique.")
dl2 = DoublyLinkedList()
dl2.add(1)
dl2.add(3)
dl2.add(5)
dl2.add(5)
dl2.add(3)
dl2.add(1)
dl2.traverse_list()
print("Palindrome?", dl2.is_palindrome())
print()

print("On va tester si la liste doublement chaînée [1,3,5,5,3,0] est palindromique.")
dl3 = DoublyLinkedList()
dl3.add(1)
dl3.add(3)
dl3.add(5)
dl3.add(5)
dl3.add(3)
dl3.add(0)
dl3.traverse_list()
print("Palindrome?", dl3.is_palindrome())
print()

print("On va tester si la liste doublement chaînée [1,3,5,3,0] est palindromique.")
dl4 = DoublyLinkedList()
dl4.add(1)
dl4.add(3)
dl4.add(5)
dl4.add(3)
dl4.add(0)
dl4.traverse_list()
print("Palindrome?", dl4.is_palindrome())
print()
