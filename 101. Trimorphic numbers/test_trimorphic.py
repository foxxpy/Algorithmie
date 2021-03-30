from trimorphic import trimorphic

for n in range(100):
    if trimorphic(n):
        print("{} : {}".format(n, n**3))
