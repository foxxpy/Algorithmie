import sys

class Pile:
    """Structure de données respectant le modèle LIFO (dernier entré, premier sorti)."""

    def __init__(self, maxSize=None):
        self._items = []
        self.MAX_SIZE = sys.maxint if maxSize == None else maxSize



    def push(self, item):
        """Ajoute un ou plusieurs éléments sur la pile."""

        if type(item) is list:
            for it in item:
                if len(self._items) < self.MAX_SIZE:
                    self._items.append(it)
                else:
                    break
        else:
            if len(self._items) < self.MAX_SIZE:
                self._items.append(item)
            else:
                raise IndexError("The stack is already full")


    
    def next_item_to_pop(self):
        """Renvoie le prochain élément qui sera retiré de la pile si on fait appel à la méthode pop()."""

        self._items[-1]



    def pop(self):
        """Retire le dernier élément qui a été ajouté à la pile."""

        if len(self._items) <= 0:
            raise IndexError("Can't pop from empty stack")
        self._items.pop(-1)



    def is_empty(self):
        """Renvoie True si la pile est vide, sinon renvoie False."""

        return len(self._items) == 0



    def length(self):
        """Renvoie la longueur de la pile."""

        return len(self._items)



    def __str__(self):
        """Renvoie la pile sous forme de chaîne de caractères."""

        return str(self._items)



    def min(self):
        """Renvoie la valeur minimum de la pile."""

        return min(self._items)



    def max(self):
        """Renvoie la valeur maximum de la pile."""

        return max(self._items)



    def find(self, item):
        """Renvoie l'indice de l'élément recherché (item) dans la pile."""

        return self._items.index(item)



    def reset(self):
        """Réinitialise la pile."""

        self._items = []