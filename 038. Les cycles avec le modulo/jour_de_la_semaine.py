jour_de_la_semaine = ["Lundi",  #indice 0
                      "Mardi", #indice 1
                      "Mercredi", #indice 2
                      "Jeudi", #indice 3
                      "Vendredi", #indice 4
                      "Samedi", #indice 5
                      "Dimanche"] #indice 6


#Boucle permettant d'illustrer les cycles au sein de l'utilisation de l'opérateur
#modulo
for i in range(100):
    print("{} : {}".format(i%7, jour_de_la_semaine[i%7]))
    
