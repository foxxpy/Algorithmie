from pile import Pile

p1 = Pile()
p1.push(1)
p1.push(2)
p1.push(3)
print("Min :", p1.min())
print("Max :", p1.max())
print("Find 2 :", p1.find(2))
print("Longueur :", p1.length())
print("Taille maximale : ", p1.MAX_SIZE)
print(p1)
p1.pop()
print(p1)
p1.reset()
print(p1)
print("-------------------")
p2 = Pile(5)
p2.push(1)
p2.push(2)
p2.push([3,4,5])
p2.push(6)