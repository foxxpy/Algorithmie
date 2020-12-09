joueurs = ["Sarah", "Lucie", "Antoine", "Olivier"]

#Boucle de distribution des cartes depuis un jeu de 52 cartes
for i in range(52):
    print("{}. Une carte est distribuée à {}".format(i%4, joueurs[i%4]))

    #Permet d'ajouter un espacement toutes les 4 lignes
    if i%4 == 3:
        print()

