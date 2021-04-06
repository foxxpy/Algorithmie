def super_digit(n):
    while len(str(n)) > 1:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n
