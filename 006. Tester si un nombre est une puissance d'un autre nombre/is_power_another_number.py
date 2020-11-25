def is_power_another_number(n,p):
    """Teste si un nombre n est la puissance d'un autre nombre i à la puissance p"""
    for i in range(1, n):
        if i**p > n:
            return False
        elif i**p == n:
            return True


print(is_power_another_number(100,2))
print(is_power_another_number(27,3))
print(is_power_another_number(100,3))
print(is_power_another_number(81,3))
print(is_power_another_number(243,3))
print(is_power_another_number(25,2))
