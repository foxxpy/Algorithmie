class Node:
    """Noeud d'une liste chaînée"""
    
    def __init__(self, data):
        self._item = data
        self.next = None