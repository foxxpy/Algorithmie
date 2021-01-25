from two_lists_to_dict import two_lists_to_dict

def test_two_lists_to_dict():

    #Des personnes et l'argent dans leur porte-monnaie
    liste1 = ["Marc", "Antoine", "Cyril"]
    liste2 = [20, 60, 80]
    print(two_lists_to_dict(liste1, liste2))

    #Deux listes de longueur différente
    nombre1 = [1,2,3,4]
    nombre2 = [1,2,3]
    print(two_lists_to_dict(nombre1, nombre2))

    

test_two_lists_to_dict()
