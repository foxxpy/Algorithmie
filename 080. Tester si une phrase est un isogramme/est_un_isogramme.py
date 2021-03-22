def no_accent_char(char):
    table_correspondance = {192 : 65,
                            193 : 65,
                            194 : 65,
                            195 : 65,
                            196 : 65,
                            197 : 65,
                            198 : 65,
                            199 : 67,
                            200 : 69,
                            201 : 69,
                            202 : 69,
                            203 : 69,
                            204 : 73,
                            205 : 73,
                            206 : 73,
                            207 : 73,
                            208 : 68,
                            209 : 78,
                            210 : 79,
                            211 : 79,
                            212 : 79,
                            213 : 79,
                            214 : 79,
                            216 : 79,
                            217 : 85,
                            218 : 85,
                            219 : 85,
                            220 : 85,
                            221 : 89,
                            224 : 97,
                            225 : 97,
                            226 : 97,
                            227 : 97,
                            228 : 97,
                            229 : 97,
                            230 : 97,
                            231 : 99,
                            232 : 101,
                            233 : 101,
                            234 : 101,
                            235 : 101,
                            236 : 105,
                            237 : 105,
                            238 : 105,
                            239 : 105,
                            240 : 111,
                            241 : 110,
                            242 : 111,
                            243 : 111,
                            244 : 111,
                            245 : 111,
                            246 : 111,
                            248 : 111,
                            249 : 117,
                            250 : 117,
                            251 : 117,
                            252 : 117,
                            253 : 121
                            
        
    }

    if 192 <= ord(char) <= 214 or 216 <= ord(char) <= 253:
        return chr(table_correspondance[ord(char)])
    else:
        return char

    return new_string



#Méthode codée à l'épisode 71 pour enlever tous les accents d'une phrase
def no_accent_word(string):
    new_string = ""
    for char in string:
        new_string += no_accent_char(char)

    return new_string



#Codée à l'épisode 78 : Tester si toutes les valeurs d'un dictionnaire sont égales
def same_values_set(dictionnaire):
    """Renvoie True si toutes les valeurs d'un dictionnaire sont pareils. False sinon."""
    if len(set(dictionnaire.values())) == 1:
        return True
    else:
        return False

    

def est_un_isogramme(mot):
    """Un mot est un isogramme si toutes ses lettres se répètent le même nombre de fois"""

    number_of_letters = {}

    #On traite le mot en retirant les accents, et en mettant les lettres en minuscule
    mot = no_accent_word(mot)
    mot = mot.lower()
    
    #Les clés du dictionnaire sont les lettres
    #Leur valeur associée est le nombre d'apparitions
    for letter in mot:
        if letter in number_of_letters.keys():
            number_of_letters[letter] += 1
        else:
            number_of_letters[letter] = 1

    #Si toutes les lettres ont le même nombre d'apparitions
    if same_values_set(number_of_letters):
        return True
    else:
        return False
