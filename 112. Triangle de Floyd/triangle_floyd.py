def triangle_floyd(n):
    """Affiche les n premières lignes du triangle de Floyd"""

    nombre = 1
    for ligne in range(1, n+1):
        for _ in range(nombre_par_ligne):
            print(nombre, end=" ")
            nombre += 1
        print()

        
