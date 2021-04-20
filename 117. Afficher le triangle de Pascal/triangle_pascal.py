def triangle_pascal(n):
    """Affiche les n premières lignes du triangle de Pascal"""

    if n == 0:
        return []

    pascal = [[1]]

    for i in range(1,n):
        line = [1]
        for j in range(len(pascal)):
            if j+1 < len(pascal):
                line.append(pascal[i-1][j] + pascal[i-1][j+1])
        line.append(1)
        pascal.append(line)

    return pascal
            
