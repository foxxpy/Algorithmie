from is_title import is_title

def test_is_title():
    texte_chaque_mot_commence_par_une_majuscule = "Bonjour A Tous Les Amis!"
    texte_sans_majuscule = "bonjour à tous!"
    texte_avec_des_nombres = "Vous Venez Tous Les 3?"
    texte_avec_des_nombres_2 = "Ils Ont 3 Chiens Et 2 Chats!"
    texte_entierement_majuscule = "JE CRIE TRES TRES FORT!"
    texte_apostrophe_minuscule = "l'alien Est Descendu Sur La Terre"
    texte_apostrophe_minuscule_majuscule = "l'Alien Est Descendu Sur La Terre"
    texte_apostrophe_majuscule = "L'Alien Est Descendu Sur La Terre"
    texte_nimporte_comment = "JE VouS AdoRE!"
    texte_avec_tirets = "Peut-être Que Tu Es Malade."
    texte_avec_tirets_majuscule = "Peut-Etre Que Tu Es Malade."

    print(is_title(texte_chaque_mot_commence_par_une_majuscule))
    print(is_title(texte_sans_majuscule))
    print(is_title(texte_avec_des_nombres))
    print(is_title(texte_avec_des_nombres_2))
    print(is_title(texte_entierement_majuscule))
    print(is_title(texte_apostrophe_minuscule))
    print(is_title(texte_apostrophe_minuscule_majuscule))
    print(is_title(texte_apostrophe_majuscule))
    print(is_title(texte_nimporte_comment))
    print(is_title(texte_avec_tirets))
    print(is_title(texte_avec_tirets_majuscule))

test_is_title()
