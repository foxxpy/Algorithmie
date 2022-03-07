from node import Node

class DoublyLinkedList:
    """Liste doublement chaînée."""

    def __init__(self):
        self.first = None
        self.last = None



    def add_first(self, item):
        """Ajoute un élément au début de la liste doublement chaînée."""

        node_item = Node(item)
        node_item.next = self.first
        self.first.previous = node_item
        self.first = node_item



    def add_node_first(self, node):
        """Ajoute un noeud au début de la liste doublement chaînée."""

        node.next = self.first
        self.first.previous = node
        self.first = node

    

    def add(self, item):
        """Ajout d'un élément à la fin de la liste doublement chaînée."""

        #Si la liste doublement chaînée est vide
        if self.first == None:
            self.first = Node(item)
            self.last = self.first

        #Si la liste doublement chaînée ne contient qu'un seul élément
        elif self.last == self.first:
            self.last = Node(item)
            self.first.next = self.last
            self.last.previous = self.first

        else:
            current = Node(item)
            self.last.next = current
            current.previous = self.last
            self.last = current



    def add_node(self, node):
        """Ajoute un noeud à la fin de la liste doublement chaînée."""

        #Si la liste doublement chaînée est vide
        if self.first == None:
            self.first = node
            self.last = node

        #Si la liste doublement chaînée ne contient qu'un seul élément
        elif self.first == self.last:
            self.last = node
            self.first.next = self.last
            self.last.previous = self.first

        else:
            self.last.next = node
            node.previous = self.last
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

            while i < index:
                i += 1
                node = node.next

            node_item = Node(item)
            node_item.next = node
            node.previous.next = node_item
            node_item.previous = node.previous
            node.previous = node_item



    def insert_after(self, index, item):
        """Insère un élément après l'indice i"""

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
            previous_node = None
            while i < index:
                i += 1
                node = node.next

            print(node._item)
            node_item = Node(item)
            node_item.previous = node
            node_item.next = node.next
            node.next.previous = node_item
            node.next = node_item




    def get_node(self, index):
        """Renvoie le noeud à l'indice index."""

        #Si la liste chaînée double est vide
        if self.length() == 0:
            raise IndexError("This doubly linked list is empty.")

        #Si l'index donné est plus grand que le nombre d'éléments qu'il y'a dans la liste
        if index >= self.length():
            raise IndexError("This linked list is too short to get an element at this index.")

        #Si l'indice est plus grand que la moitié du nombre d'élements de la liste chaînée double
        #On part de la fin pour le rechercher
        elif index > self.length() // 2:
            i = self.length() - 1
            node = self.last
            while i > index:
                i -= 1
                node = node.previous
            return node

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



    def traverse_list(self, reverse=False):
        """Parcourt la liste chaînée et affiche ses éléments."""

        if self.first is None:
            print("La liste chaînée est vide.")
            return

        #Si on veut la liste chaînée double de la fin vers le début
        if reverse:
            n = self.last
            while n is not None:
                print(n._item, " ", end="")
                n = n.previous
            print()

        #Si on veut la liste chaînée double du début vers la fin
        else:
            n = self.first
            while n is not None:
                print(n._item, " ", end="")
                n = n.next
            print()



    def traverse_list_info(self, reverse=False):
        """Parcourt la liste chaînée et affiche ses éléments."""

        if self.first is None:
            print("La liste chaînée est vide.")
            return

        #Si on veut la liste chaînée double de la fin vers le début
        if reverse:
            n = self.last
            while n is not None:
                print(n._item, " ", end="")
                n = n.previous
            print()

        #Si on veut la liste chaînée double du début vers la fin
        else:
            n = self.first
            while n is not None:
                if n.previous is None and n.next is None:
                    print("Item :", n._item, "- Previous : None", "- Next : None")

                elif n.previous is None:
                    print("Item :", n._item, "- Previous : None", "- Next :", n.next._item)                
                elif n.next is None:
                    print("Item :", n._item, "- Previous :", n.previous._item, "- Next : None")
                else:
                    print("Item :", n._item, "- Previous :", n.previous._item, "- Next :", n.next._item, " ")
                n = n.next
            print()



    def remove_first(self):
            """Supprime le premier noeud de la liste chaînée double et le renvoie."""

            if self.length() == 0:
                raise ValueError("La liste chaînée est vide.")

            elif self.length() == 1:
                self.first = None
                self.last = None

            else:
                self.first = self.first.next
                self.first.previous = None



    def remove_last(self):
        """Retire le dernier noeud de la liste chaînée et le renvoie."""

        if self.length() == 0:
            raise ValueError("La liste chaînée est vide.")

        elif self.length() == 1:
            self.first = None
            self.last = None

        else:
            self.last = self.last.previous
            self.last.next = None



    def remove(self, item):
        """Retire tous les éléments qui ont pour valeur item."""

        if self.length() == 0:
            raise ValueError("La liste chaînée est vide.")

        node = self.first
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
                    node.previous.next = node.next

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
            while i < index:
                i += 1
                node = node.next

            node.previous.next = node.next
            node.next.previous = node.previous



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



    def inverse(self):
        """Inverse cette liste doublement chaînée."""

        node = self.last
        self.first = self.last
        node.next = node.previous
        node.previous = None

        while node.next is not None:
            node = node.next
            temp = node.next
            node.next = node.previous
            node.previous = temp

        self.last = node
