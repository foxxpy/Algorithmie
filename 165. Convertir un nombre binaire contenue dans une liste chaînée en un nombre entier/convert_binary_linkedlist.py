from linkedlist import LinkedList

def get_decimal_value(liste):
    """
    Renvoie la valeur en base décimale d'un nombre binaire représenté par une liste chaînée.
    :type first: ListNode
    :rtype: int

    Leetcode 1290 de l'application Android Leetcode Python
    """
    result = 0
    first = liste.first

    while first:
        result = result * 2 + first._item
        first = first.next

    return result