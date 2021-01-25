from delete_char import delete_char

def test_delete_char():
    #En supprimant le caractère à l'indice 2
    string = "Foxxpy"
    s1 = delete_char("Foxxpy", 2)
    print(s1)

    #En supprimant le premier caractère
    print()
    s2 = delete_char("Foxxpy", 0)
    print(s2)

    #En supprimant le dernier caractère
    print()
    s3 = delete_char("Foxxpy", 5)
    print(s3)

    #Indice hors de la chaîne de caractères
    print()
    s4 = delete_char("Foxxpy", 100)
    print(s4)

    #Indice hors de la chaîne de caractères 2
    print()
    s5 = delete_char("Foxxpy", -600)
    print(s5)

test_delete_char()
