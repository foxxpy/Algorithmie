#Si l'ordre de la liste n'importe pas, il suffit de caster la liste en set,
#puis de la recaster en liste.

def enlever_doublon(liste):
    """Enlève les doublons dans une liste mais ne conserve pas forcément les éléments
    dans leur ordre d'apparition"""
    
    return list(set(liste))
