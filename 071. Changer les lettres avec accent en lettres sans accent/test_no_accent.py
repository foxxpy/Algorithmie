from no_accent import no_accent_char, no_accent_word

#On teste pour les lettres avec accent
for char in ["ç","é", "ê", "ë", "è", "à", "â", "ä", "ï", "î", "ö", "ô", "û", "ù", "ü"]:
    print("{} => {}".format(char, no_accent_char(char)))

#Test avec des mots
string = "Félicitations! Tu as réussi ton examen!"
print(no_accent_word(string))

string = "J'ai créé un remède."
print(no_accent_word(string))
