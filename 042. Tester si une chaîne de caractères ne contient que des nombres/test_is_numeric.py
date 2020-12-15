from is_numeric import is_numeric

def test_is_numeric():
    texte_sans_nombre = "Bonjour à tous!"
    texte_melange_nombre_char = "Bonjour à vous 2!"
    texte_nombre = "42"
    texte_plusieurs_nombres = "18 65 48 98 72"

    print(is_numeric(texte_sans_nombre))  #False
    print(is_numeric(texte_melange_nombre_char)) #False
    print(is_numeric(texte_nombre)) #True
    print(is_numeric(texte_plusieurs_nombres)) #False

test_is_numeric()
