def binary_to_decimal(binary):
    """Convertit un nombre en base binaire en un nombre en base décimale"""
    
    if "0b" in binary:
        binary = binary.replace("0b", "")
        
    total = 0
    for i, bit in enumerate(binary[::-1]):
        total += int(bit) * 2**i

    return total
