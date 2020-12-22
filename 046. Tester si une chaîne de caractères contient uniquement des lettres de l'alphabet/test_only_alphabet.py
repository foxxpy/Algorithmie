from only_alphabet import only_alphabet

def test_only_alphabet():
    pseudonyme1 = "Foxxpy"
    pseudonyme2 = "Foxxpy68"
    prenom = "Félix"
    phrase = "Bonjour. Vous allez bien?"

    print(only_alphabet(pseudonyme1)) #True
    print(only_alphabet(pseudonyme2)) #False
    print(only_alphabet(prenom)) #True
    print(only_alphabet(phrase)) #False

test_only_alphabet()
