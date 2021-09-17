def complement(number):
    """Le complément d'un nombre est ce nombre avec tous les bits inversés"""

    new_number = ""

    if isinstance(number, int):
        number = bin(number)

    if "0b" in number:
        number = number.replace("0b", "")

    for bit in number:
        if bit == "0":
            new_number += "1"
        else:
            new_number += "0"

    return new_number

