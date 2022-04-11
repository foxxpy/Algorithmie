from node import Node

def addition_linkedlist(n1, n2):
    """Additionne deux nombres formés par des listes chaînées. Retourne le premier noeud
    de la liste chaînée qui forme le résultat de l'addition.
    :type n1: Node()
    :type n2: Node()
    :rtype: Node()
    
    Leetcode 445 de l'application Android Leetcode Python"""


    num1, num2 = 0, 0

    node = n1
    while node:
        num1 = num1 * 10 + node._item
        node = node.next
    node = n2
    while node:
        num2 = num2 * 10 + node._item
        node = node.next

    total = num1 + num2
    if total == 0:              # return single node with zero
        return Node(0)
    result = None

    while total:
        total, digit = divmod(total, 10)
        new_node = Node(digit)
        new_node.next = result  # make digit start of result
        result = new_node

    return result