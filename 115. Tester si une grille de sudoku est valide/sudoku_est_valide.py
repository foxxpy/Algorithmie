def sudoku_est_valide(grille):

    #Test des lignes
    for line in grille:
        if not len(set(line)) == 9:
            return False

    #Test des colonnes
    for i in range(9):
        column = []
        for j in range(9):
            column.append(grille[j][i])
        if not len(set(column)) == 9:
            return False

    x0 = (x//3) * 3
    y0 = (y//3) * 3
    #On détermine si le nombre est valide dans sa sous-grille 3x3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True
            
