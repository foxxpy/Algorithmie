from min_dict import min_dict


def test_min_dict():

    #Argent de poche
    dictionnaire = {"Alfred" : 100, "Julie" : 150, "Antoine" : 20}
    print(min_dict(dictionnaire))

    #Magasin de luxe
    luxe = {"Bague" : 3200, "Montre" : 5600, "Sac à main" : 1400}
    print(min_dict(luxe))



test_min_dict()
