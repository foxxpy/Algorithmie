#Fonction qui teste si la chaîne de caractères envoyée est un palindrome
#Exemple palindromes : "Un radar nu", "Engage le jeu que je le gagne", "Le ruban à Burel", "Un roc cornu"

def recursion_palindrome(message, i=0, j=0):

    if i == 0 and j == 0:
        j = len(message) - 1
    is_palindrome = True

    if j - i > 1:
        c = [" ", ",", "-", "'", "!", "?"]
        if message[i] in c:
            is_palindrome = recursion_palindrome(message, i+1, j)   

        elif message[j] in c:
            is_palindrome = recursion_palindrome(message, i, j-1)

        elif message[i].lower() != message[j].lower() and j - i > 1:
            return False  

        else:
            is_palindrome = recursion_palindrome(message, i+1, j-1)

    return is_palindrome

#Exemple avec le palindrome : "Un roc cornu"
#recursion_palindrome("Un roc cornu", i=0, j=0)
#   recursion_palindrome("Un roc cornu", i=1, j=10)
#       recursion_palindrome("Un roc cornu", i=2, j=9)
#           recursion_palindrome("Un roc cornu", i=3, j=9)
#               recursion_palindrome("Un roc cornu", i=4, j=8)
#                   recursion_palindrome("Un roc cornu", i=5, j=7)
#                       recursion_palindrome("Un roc cornu", i=6, j=6)
#                       return True
#                   return True
#               return True
#           return True
#       return True
#   return True
#return True

# --- Palindromes ---
#Eh ! ça va, la vache ?
#La mariee ira mal
#Un port trop nu
#Engage le jeu que je le gagne
#La mere Gide digere mal
#Tu l'as trop ecrase, Cesar, ce Port-Salut
