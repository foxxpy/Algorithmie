def retirer_ponctuation(string):
    """Retire les ponctuations d'une chaîne de caractères"""

    if not string.isalpha():
        #On retire tous les caractères avant les majuscule (65) dans la table ascii
        for i in range(65):
            if chr(i) in string:
                string = string.replace(chr(i), "")

        for i in range(91, 97):
            if chr(i) in string:
                string = string.replace(chr(i), "")

        for i in range(123, 128):
            if chr(i) in string:
                string = string.replace(chr(i), "")

        for i in range(128, 192):
            if chr(i) in string:
                string = string.replace(chr(i), "")

        if chr(8217) in string:
            string = string.replace(chr(8217), "")

    return string
