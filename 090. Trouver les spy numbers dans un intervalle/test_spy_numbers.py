from spy_numbers import spy_numbers

for i in range(1000):
    if spy_numbers(i):
        print("{} est un nombre espion".format(i))
