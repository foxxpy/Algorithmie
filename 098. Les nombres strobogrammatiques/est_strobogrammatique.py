def est_strobogrammatique(n):
    """Un nombre strobogrammatique est un nombre qui se lit toujours de la même façon
    après avoir pivoté de 180 degrés."""
    strobo = {"0" : "0", "1" : "1", "8" : "8", "6" : "9", "9" : "6"}

    #Si n est un entier, on le caste en chaîne de caractères
    if type(n) is int:
        n = str(n)

    left = 0
    right = len(n) - 1

    while right - left >= 0:
        if not n[left] in strobo.keys() or not n[right] in strobo.keys() or n[left] != strobo[n[right]]:
            return False
        right -= 1
        left += 1

    return True
