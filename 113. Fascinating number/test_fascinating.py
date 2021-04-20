from fascinating import is_fascinating

for i in range(1, 1001):
    if is_fascinating(i):
        print("{} est un fascinating number.".format(i))
