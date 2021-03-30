from evil import is_evil, is_evil_bin

for i in range(0,101):
    print("{} : {}".format(i, is_evil(i)))
    print("{} : {}".format(i, is_evil_bin(i)))
    print()
