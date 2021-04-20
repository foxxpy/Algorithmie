import numpy as np

grid = []

def n_valide(y, x, n):
    """Détermine si un nombre n peut être mis sur une case à la colonne x et à la ligne"""
    global grid
    #On détermine si le nombre est valide sur sa ligne
    for x0 in range(len(grid)):
        if grid[y][x0] == n:
            return False

    #On détermine si le nombre est valide sur sa colonne
    for y0 in range(len(grid)):
        if grid[y0][x] == n:
            return False
    
    x0 = (x//3) * 3
    y0= (y//3) * 3
    #On détermine si le nombre est valide dans sa sous-grille 3x3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if n_valide(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end="")
        print()
    exit(0)
