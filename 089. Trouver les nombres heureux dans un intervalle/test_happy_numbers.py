from happy_numbers import happy

for i in range(1000):
    if happy(i):
        print("{} est un nombre heureux".format(i))
