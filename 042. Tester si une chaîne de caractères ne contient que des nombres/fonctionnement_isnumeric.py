texte_sans_nombre = "Bonjour à tous!"
texte_melange_nombre_char = "Bonjour à vous 2!"
texte_nombre = "42"
texte_plusieurs_nombres = "65 48 98 72"

print(texte_sans_nombre.isnumeric()) #False
print(texte_melange_nombre_char.isnumeric()) #False
print(texte_nombre.isnumeric()) #True
print(texte_plusieurs_nombres.isnumeric()) #False

#La méthode isnumeric() teste si il n'y a que des chiffres dans la chaîne de
#caractères sans aucun autre caractère, pas même les caractères spéciaux ou l'espace.
