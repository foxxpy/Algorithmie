def is_fascinating(n):
    """Un nombre fascinant est un nombre auquel on concatene son multiple de 2
    et son multiple de 3. Si le nombre obtenu contient tous les chiffres de 1
    à 9, alors c'est un nombre fascinant."""
    
    #Si il y'a moins 3 chiffres
    if len(str(n)) < 3:
        return None

    #On concatène n, n*2 et n*3
    num = n
    num = int(str(num) + str(n*2))
    num = int(str(num) + str(n*3))

    #On cherche si tous les chiffres sont présents dans num
    liste_chiffres = ["1","2","3","4","5","6","7","8","9"]
    for chiffre in str(num):
        if chiffre in liste_chiffres:
            liste_chiffres.remove(chiffre)
        if len(liste_chiffres) == 0:
            break

    #Si il ne reste plus de chiffres dans liste_chiffres, c'est qu'ils étaient tous dans num
    if len(liste_chiffres) == 0:
        return True
    else:
        return False
        
