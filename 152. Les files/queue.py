import sys

class Queue:
    """Structure de données respectant le modèle FIFO (premier entré, premier sorti)."""

    def __init__(self, max_size = None):
        self._items = []
        self.MAX_SIZE = sys.maxint if max_size == None else max_size



    def push(self, item):
        """Ajoute un ou plusieurs éléments dans la file."""

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
                raise IndexError("The queue is already full")



    def pop(self):
        """Retire le premier élément de la file."""

        self._items.pop(0)



    def next_item_to_pop(self):
        """Renvoie le prochain élément qui sera retiré de la file si on fait appel à la méthode pop()."""

        return self._items[0]



    def is_empty(self):
        """Renvoie True si la file est vide, sinon renvoie False."""

        return len(self._items) == 0



    def length(self):
        """Renvoie la longueur de la file."""

        return len(self._items)



    def __str__(self):
        """Renvoie la file sous forme de chaîne de caractères."""

        return str(self._items)



    def min(self):
        """Renvoie la valeur minimum de la file."""

        return min(self._items)



    def max(self):
        """Renvoie la valeur maximum de la file."""

        return max(self._items)



    def find(self, item):
        """Renvoie l'indice de l'élément recherché (item) dans la file."""

        return self._items.index(item)



    def reset(self):
        """Réinitialise la file."""

        self._items = []