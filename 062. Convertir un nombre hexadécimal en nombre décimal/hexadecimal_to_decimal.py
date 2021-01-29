def hexadecimal_to_decimal(hexadecimal):
    """Convertit un nombre hexadecimal en un nombre décimal"""

    hexa_values = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
                   "7" : 7, "8" : 8, "9" : 9 , "A" : 10, "B" : 11, "C" : 12,
                   "D" : 13, "E" : 14, "F" : 15}

    #Si on a 0x dans le nombre hexadécimal, on le retire
    if "0x" in hexadecimal:
        hexadecimal = hexadecimal.replace("0x", "")

    hexadecimal = hexadecimal.upper()
    total = 0
    for i, digit in enumerate(hexadecimal[::-1]):
        total += hexa_values[digit] * 16**i

    return total
