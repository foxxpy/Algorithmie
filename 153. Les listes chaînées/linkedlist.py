from node import Node

class LinkedList:
    """Implémentation d'une liste chaînée simple."""

    def __init__(self):
        self.first = None
        self.last = None



    def add_first(self, item):
        """Ajoute un élément au début de la liste chaînée."""

        node_item = Node(item)
        node_item.next = self.first
        self.first = node_item



    def add_node_first(self, node):
        """Ajoute un noeud au début de la liste chaînée."""

        node.next = self.first
        self.first = node



    def add(self, item):
        """Ajoute un élément à la fin de la liste chaînée."""

        if self.first == None:
            self.first = Node(item)
            self.last = self.first

        elif self.last == self.first:
            self.last = Node(item)
            self.first.next = self.last

        else:
            current = Node(item)
            self.last.next = current
            self.last = current



    def add_node(self, node):
        """Ajoute un noeud à la fin de la liste chaînée."""

        if self.first == None:
            self.first = node
            self.last = self.first

        elif self.last == self.first:
            self.last = node
            self.first.next = self.last

        else:
            self.last.next = node
            self.last = node



    def insert(self, index, item):
        """Insère un élément à l'indice i."""

        if index < 0:
            raise IndexError("The index can't be inferior to 0.")

        elif index > self.length():
            raise IndexError("The index is bigger than the size of this linked list.")

        else:
            i = 0
            node = self.first
            while i < (index - 1):
                i += 1
                node = node.next

            node_item = Node(item)
            node_item.next = node.next
            node.next = node_item



    def insert_after(self, index, item):
        """Insère un noeud après l'indice i."""

        #Si l'indice donné correspond à l'indice du dernier élément
        if index == self.length() - 1:
            self.add(item)

        #Si l'indice est plus grand ou égal à la taille de la liste chaînée
        elif index >= self.length():
            raise IndexError("This linked list is too short to insert an element at this index.")

        #Sinon on insère l'élément
        else:
            i = 0
            node = self.first
            while i < index:
                i += 1
                node = node.next

            node_item = Node(item)
            node_item.next = node.next
            node.next = node_item
            


    def get_node(self, index):
        """Renvoie le noeud à l'indice index."""

        if index >= self.length():
            raise IndexError("This linked list is too short to get an element at this index.")

        else:
            i = 0
            node = self.first
            while i < index:
                i += 1
                node = node.next
            return node



    def is_empty(self):
        """Renvoie True si la liste chaînée est vide, renvoie False sinon."""

        return self.first == None



    def length(self):
        """Renvoie la taille de la liste chaînée."""

        node = self.first
        i = 0
        while node is not None:
            node = node.next
            i += 1

        return i



    def traverse_list(self):
        """Parcourt la liste chaînée et affiche ses éléments."""

        if self.first is None:
            print("La liste chaînée est vide.")
            return
        else:
            n = self.first
            while n is not None:
                print(n._item, " ", end="")
                n = n.next
            print()



    def traverse_list_info(self):
        """Parcourt la liste chaînée et affiche ses éléments."""

        if self.first is None:
            print("La liste chaînée est vide.")
            return
        else:
            n = self.first
            while n is not None:
                if n.next is None:
                    print("Item :", n._item, "- Next : None")
                else:
                    print("Item :", n._item, "- Next :", n.next._item)
                n = n.next
            print()



    def remove_first(self):
        """Supprime le premier noeud de la liste chaînée et le renvoie."""

        if self.length() == 0:
            raise ValueError("La liste chaînée est vide.")

        elif self.length() == 1:
            self.first = None
            self.last = None

        else:
            self.first = self.first.next



    def remove_last(self):
        """Retire le dernier noeud de la liste chaînée et le renvoie."""

        if self.length() == 0:
            raise ValueError("La liste chaînée est vide.")

        elif self.length() == 1:
            self.first = None
            self.last = None

        else:
            node = self.first
            while node.next.next is not None:
                node = node.next

            node.next = None
            self.last = node



    def remove(self, item):
        """Retire tous les éléments qui ont pour valeur item."""

        if self.length() == 0:
            raise ValueError("La liste chaînée est vide.")

        node = self.first
        previous_node = None
        while node is not None:
            if node._item == item:

                #Si il n'y a qu'un seul noeud dans la liste chaînée
                if self.first == self.last:
                    self.first = None
                    self.last = None

                #Si le noeud à supprimer est le dernier
                elif node == self.last:
                    self.remove_last()

                #Si le noeud à supprimer est le premier
                elif node == self.first:
                    self.remove_first()

                else:
                    #Le noeud précédant le noeud à supprimer fait référence au noeud suivant le noeud à supprimer
                    previous_node.next = node.next

            else:
                previous_node = node

            node = node.next



    def pop(self, index):
        """Retire un élément à l'indice index"""

        if index < 0:
            raise IndexError("The index can't be inferior to 0.")

        elif index > self.length():
            raise IndexError("The index is bigger than the size of this linked list.")

        if self.first == self.last:
            self.first = None
            self.last = None

        elif index == 0:
            self.remove_first()

        elif index == self.length() - 1:
            self.remove_last()

        else:
            i = 0
            node = self.first
            previous_node = None
            while i < index:
                i += 1
                previous_node = node
                node = node.next

            previous_node.next = node.next



    def display_first_last(self):
        """Affiche le premier et le dernier élement de la liste chaînée."""

        if self.first is None and self.last is None:
            print("First : None - Last : None")

        elif self.first is None and not self.last is None:
            print("First : None - Last :", self.last._item)

        elif not self.first is None and self.last is None:
            print("First :", self.first._item, "- Last : None")
        
        else:
            print("First :", self.first._item, "- Last :", self.last._item)