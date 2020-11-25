def bubble_sort(liste):
    """Trie une liste en utilisant l'algorithme du tri à bulles"""
    
    permutation = True
    j = 0
    while permutation:
        permutation = False
        j = j + 1
        for i in range(0, len(liste) - j):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                permutation = True

    return liste

liste = [9,8,7,6,5,4,3,2,1]
print(bubble_sort(liste))
