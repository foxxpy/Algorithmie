#Liste des lettres avec un accent
accents = ["à", "â", "ä",
          "ù","ü","û",
          "é","è","ê", "ë",
          "ô","ö"]

#Affichage du code ascii en minuscule et en majuscule des lettres avec un accent
for accent in accents:
    print("{} - code ascii : {} - Majuscule : {} - code ascii majuscule : {}".format(
        accent, ord(accent), accent.upper(), ord(accent.upper())))


#Recherche d'un pattern entre les minuscules et les majuscules
print("\n\n")
for accent in accents:
    print("{} - {} : {}".format(accent, accent.upper(), ord(accent)-ord(accent.upper())))

for accent in accents:
    print("{}".format(accent.upper()))
