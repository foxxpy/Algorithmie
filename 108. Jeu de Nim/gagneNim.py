def gagneNim(baton):
    """Détermine si un joueur peut gagner le jeu de Nim suivant le nombre de bâtons
    restants."""

    return baton % 4 != 0
