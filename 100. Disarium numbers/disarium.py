def disarium(n):

    total = 0
    for i, digit in enumerate(str(n)):
        total += int(digit)**(i+1)

    return total == n
