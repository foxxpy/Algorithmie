from super_digit import super_digit

#On calcule les super digits des 1000 premiers nombres
for i in range(1, 1001):
    print("{} => {}".format(i, super_digit(i)))
