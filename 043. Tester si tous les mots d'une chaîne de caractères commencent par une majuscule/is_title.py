def is_title(text):
    """Renvoie True si tous les mots de text commencent par une majuscule"""
    text_is_title = True
    must_be_uppercase = True
    punctuation = [".", " ", ";", ":", "!", "?", ".", "/", "§", "-", "_", "'", '"',
                   "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for char in text:
        if must_be_uppercase and not 64 < ord(char) < 91 and not char in punctuation:
            text_is_title = False
            break

        elif not must_be_uppercase and 64 < ord(char) < 91:
            text_is_title = False
            break

        #Si on vient de rencontrer une ponctuation, la lettre suivante doit être une lettre majuscule
        if char in punctuation:
            must_be_uppercase = True

        #Sinon c'est qu'on vient de rencontrer une lettre, et donc les autres lettres doivent être en minuscule
        else:
            must_be_uppercase = False

    return text_is_title
