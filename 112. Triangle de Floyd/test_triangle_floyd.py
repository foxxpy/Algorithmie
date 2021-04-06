from triangle_floyd import triangle_floyd

#On affiche les 10 premiers triangles de Floyd
for i in range(1,11):
    print("---")
    print(i)
    print("---")
    triangle_floyd(i)
