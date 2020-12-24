from multi_dict import *



def test_new_multiply_value():

    #Promotion appliquée sur tous les articles d'un magasin de vêtements
    prix_de_vente = {"Jean" : 35.00, "Veste" : 55.00, "Caleçon" : 8.00, "Chaussettes" : 4.00}
    promotion = new_multiply_value(prix_de_vente, 0.80)
    print(prix_de_vente)
    print(promotion)

    print()
    #Buff qui multiplie par 2 la force des personnages du groupe
    heros = {"Luciferas" : 25, "Luffy" : 40, "Magicarpe" : 1}
    heros_buff = new_multiply_value(heros, 2)
    print(heros)
    print(heros_buff)



def test_multiply_value():

    #Promotion appliquée sur tous les articles d'un magasin de vêtements
    prix_de_vente = {"Jean" : 35.00, "Veste" : 55.00, "Caleçon" : 8.00, "Chaussettes" : 4.00}
    promotion = multiply_value(prix_de_vente, 0.80)
    print(prix_de_vente)
    print(promotion)

    print()
    #Buff qui multiplie par 2 la force des personnages du groupe
    heros = {"Luciferas" : 25, "Luffy" : 40, "Magicarpe" : 1}
    heros_buff = multiply_value(heros, 2)
    print(heros)
    print(heros_buff)



test_new_multiply_value()
print()
test_multiply_value()
