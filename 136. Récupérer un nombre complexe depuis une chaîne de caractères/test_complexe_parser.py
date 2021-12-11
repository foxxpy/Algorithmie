from complexe_parser import *

#On créé nos nombres complexes
z1 = "2 + 5i"
z2 = "-1 - 2i"
z3 = "10i"
z4 = "-16"
z5 = "   3      -          5j        "
z6 = "1.3 + 2.5j"
z7 = "10e5 - 1.066j"
z8 = "5e2"
z9 = "-3e-2j"
z10 = "-5e-5 - 10e-2j"

#On teste la méthode string_to_complex()
print(" ---- string_to_complex() ----")
print(z1, ":", string_to_complex(z1))
print(z2, ":", string_to_complex(z2))
print(z3, ":", string_to_complex(z3))
print(z4, ":", string_to_complex(z4))
print(z5, ":", string_to_complex(z5))
print(z6, ":", string_to_complex(z6))
print(z7, ":", string_to_complex(z7))
print(z8, ":", string_to_complex(z8))
print(z9, ":", string_to_complex(z9))
print(z10, ":", string_to_complex(z10))

#On teste la méthode string_to_complex_2()
print(" ---- string_to_complex_2() ----")
print(z1, ":", string_to_complex_2(z1))
print(z2, ":", string_to_complex_2(z2))
print(z3, ":", string_to_complex_2(z3))
print(z4, ":", string_to_complex_2(z4))
print(z5, ":", string_to_complex_2(z5))
print(z6, ":", string_to_complex_2(z6))
print(z7, ":", string_to_complex_2(z7))
print(z8, ":", string_to_complex_2(z8))
print(z9, ":", string_to_complex_2(z9))
print(z10, ":", string_to_complex_2(z10))