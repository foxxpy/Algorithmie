from euclidean import distance_euclidienne

pt1 = (0,0)
pt2 = (1,1)
print(distance_euclidienne(pt1, pt2))
print()

#Deux points de même coordonnée
pt1 = (35,35)
pt2 = (35,35)
print(distance_euclidienne(pt1, pt2))
print()

#Deux points de même coordonnée : dimension 4
pt1 = (35,35,1,2)
pt2 = (35,35,1,2)
print(distance_euclidienne(pt1, pt2))
print()

pt1 = (0,0,0)
pt2 = (2,2,2)
print(distance_euclidienne(pt1, pt2))
print()
