from no_accent import no_accent_word
from retirer_ponctuation import retirer_ponctuation

def is_palindrome(phrase):
    phrase = phrase.upper()
    phrase= no_accent_word(phrase)
    phrase = retirer_ponctuation(phrase)

    return phrase == phrase[::-1]

print(is_palindrome("À révéler mon nom, mon nom relèvera"))
print(is_palindrome("Eh ! ça va, la vache ?"))
print(is_palindrome("L'ami naturel ? Le rut animal."))
print(is_palindrome("Ta bête te bat."))
print(is_palindrome("Engage le jeu que je le gagne"))
print(is_palindrome("Noël a trop par rapport à Léon"))
print(is_palindrome("À l'étape, épate-la ! "))
print(is_palindrome("La mère Gide digère mal"))
print(is_palindrome("Léon, émir cornu, d'un roc rime Noël "))
print(is_palindrome("Élu par cette crapule"))
print(is_palindrome("Ésope reste ici et se repose"))
print(is_palindrome("Luc notre valet alla te laver ton cul "))
print(is_palindrome("Tâte l'État ! "))
print(is_palindrome(" rue Verlaine gela le génial rêveur "))
print(is_palindrome("Elle dira hélas à la sale haridelle"))
