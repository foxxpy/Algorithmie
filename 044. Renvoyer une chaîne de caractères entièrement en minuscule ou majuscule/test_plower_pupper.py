from plower_pupper import plower, pupper

def test_upper_lower():
    #Déclaration des variables
    string_avec_majuscule_et_minuscule = "Bonjour à tous!"
    string_majuscule = "BONJOUR A TOUS!"
    string_minuscule = "bonjour à tous!"
    string_ponctuation = "Bonjour! Vous allez bien? Moi... oui!"
    string_chiffre = "J'ai 3 chats. Et vous?"

    #Test de pupper() et plower()
    print(pupper(string_avec_majuscule_et_minuscule))
    print(plower(string_avec_majuscule_et_minuscule))
    print()

    print(pupper(string_majuscule))
    print(plower(string_majuscule))
    print()

    print(pupper(string_minuscule))
    print(plower(string_minuscule))
    print()

    print(pupper(string_ponctuation))
    print(plower(string_ponctuation))
    print()

    print(pupper(string_chiffre))
    print(plower(string_chiffre))
    print()

test_upper_lower()
