from sum_dict import sum_dict

def test_sum_dict():
    
    #Prix en boulangerie
    dictionnaire = {"Baguette" : 0.85,
                "Pain au chocolat" : 1.10,
                "Croissant" : 1.00,
                "Tradition" : 1.05
    }

    #Comptes en banque
    dictionnaire_2 = {
        "Sarah" : 10,
        "Lucie" : 30,
        "Antoine" : 40,
        "Marc" : 5,
        "Sylvester" : 15
        
    }

    #Somme des éléments des dictionnaires instanciés
    print(sum_dict(dictionnaire))
    print(sum_dict(dictionnaire_2))

test_sum_dict()
