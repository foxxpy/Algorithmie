from sudoku_est_valide import sudoku_est_valide

grille_valide = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[9, 1, 2, 3, 4, 5, 6, 7, 8],
[3, 4, 5, 6, 7, 8, 9, 1, 2],
[6, 7, 8, 9, 1, 2, 3, 4, 5],
[8, 9, 1, 2, 3, 4, 5, 6, 7],
[2, 3, 4, 5, 6, 7, 8, 9, 1],
[5, 6, 7, 8, 9, 1, 2, 3, 4]]

grille_non_valide = [
[4, 3, 5, 2, 6, 9, 7, 8, 1],
[6, 8, 2, 5, 7, 1, 4, 9, 3],
[1, 9, 7, 8, 3, 4, 5, 6, 2],
[8, 2, 6, 1, 9, 5, 3, 4, 7],
[3, 7, 4, 6, 8, 2, 9, 1, 5],
[1, 5, 9, 7, 4, 3, 6, 2, 8],
[5, 1, 9, 3, 2, 6, 8, 7, 4],
[2, 4, 8, 9, 5, 7, 1, 3, 6],
[7, 6, 3, 4, 1, 8, 2, 5, 9]
]

grille_non_valide2 = [
[5, 9, 6, 1, 4, 2, 5, 3, 7],
[6, 1, 4, 3, 5, 8, 2, 4, 8],
[5, 6, 9, 4, 1, 2, 5, 3, 6],
[1, 9, 5, 3, 6, 8, 4, 1, 6],
[5, 9, 3, 6, 3, 4, 8, 2, 1],
[5, 9, 5, 3, 2, 1, 4, 5, 6],
[1, 3, 6, 4, 8, 6, 5, 2, 5],
[4, 1, 2, 3, 6, 8, 4, 9, 2],
[3, 6, 8, 7, 4, 1, 5, 6, 3]
]

grille_non_valide3 = [
[4, 3, 5, 2, 6, 9, 7, 8, 1],
[6, 8, 2, 5, 7, 1, 4, 9, 3],
[1, 9, 7, 8, 3, 4, 5, 6, 2],
[8, 2, 6, 1, 9, 5, 3, 4, 7],
[3, 7, 4, 6, 8, 2, 9, 1, 5],
[1, 5, 9, 7, 4, 3, 6, 2, 8],
[5, 1, 9, 3, 2, 6, 8, 7, 4],
[2, 4, 8, 9, 5, 7, 1, 3, 6],
[7, 6, 3, 4, 1, 8, 2, 5, 9]
]

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
        
    #On teste les sous-grilles 3x3
    for y0 in [0, 3, 6]:
        for x0 in [0, 3, 6]:
            subgrid = []
            for i in range(0, 3):
                for j in range(0, 3):
                    if grille[y0+i][x0+j] in subgrid:
                        return False
                    subgrid.append(grille[y0+i][x0+j])
                    
    return True

print(sudoku_est_valide(grille_valide))
print(sudoku_est_valide(grille_non_valide))
print(sudoku_est_valide(grille_non_valide2))
print(sudoku_est_valide(grille_non_valide3))
