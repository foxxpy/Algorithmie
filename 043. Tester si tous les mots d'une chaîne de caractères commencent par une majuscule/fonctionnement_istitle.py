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

print(texte_chaque_mot_commence_par_une_majuscule.istitle()) #True
print(texte_sans_majuscule.istitle()) #False
print(texte_avec_des_nombres.istitle()) #True
print(texte_avec_des_nombres_2.istitle()) #True
print(texte_entierement_majuscule.istitle()) #False
print(texte_apostrophe_minuscule.istitle()) #False
print(texte_apostrophe_minuscule_majuscule.istitle()) #False
print(texte_apostrophe_majuscule.istitle()) #True
print(texte_nimporte_comment.istitle()) #False
print(texte_avec_tirets.istitle()) #False
print(texte_avec_tirets_majuscule.istitle()) #True
