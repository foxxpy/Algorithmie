from merge_dict import merge_dict, merge_dict_for

def test_merge_dict():
    
    #Clients d'une banque
    client1 = {"Fabrice" : 1000.85, "Jérome" : 2400.00}
    client2 = {"Clémentine" : -124.00, "Capucine" : 3762.00, "Sarah" : 685.24}
    print(merge_dict(client1, client2))
    print(merge_dict_for(client1, client2))

    print()
    #Sportifs
    sport1 = {"Henry" : "Football", "Emmy" : "Karaté", "Martin" : "Rugby"}
    sport2 = {"Jenny" : "Boxe", "Alain" : "Danse classique"}
    print(merge_dict(sport1, sport2))
    print(merge_dict_for(sport1, sport2))

    print()
    #Test avec une clé similaire dans chaque dictionnaire
    test1 = {"1" : 1, "2" : 2}
    test2 = {"1" : 3}
    print(merge_dict(test1, test2))
    print(merge_dict_for(test1, test2))

test_merge_dict()
