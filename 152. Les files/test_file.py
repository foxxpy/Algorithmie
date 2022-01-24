from queue import Queue

f1 = Queue(10)

#On ajoute 10 éléments à la file : 1,2,3,4,5,6,7,8,9,10
for i in range(10):
    f1.push(i)
    print(f1)

#On supprime 5 éléments de la file.
for i in range(5):
    f1.pop()
    print(f1)

print("Valeur maximale :", f1.max())
print("Valeur minimale :", f1.min())
print("Longueur de la file :", f1.length())
print("Prochain élément à être supprimé :", f1.next_item_to_pop())
print("Est vide?", f1.is_empty())
print("Indice de l'élément 8 :", f1.find(8))
print("---- Réinitialisation de la file ----")
f1.reset()
print(f1)
print("Est vide?", f1.is_empty())