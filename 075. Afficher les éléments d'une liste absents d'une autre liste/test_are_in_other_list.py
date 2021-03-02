from are_in_other_list import are_in_other_list

liste1 = [1,2,3,4]
liste2 = [1,2,3]
print(are_in_other_list(liste1, liste2))

print()
liste1 = [x for x in range(100)]
liste2 = [x for x in range(50,101)]
print(are_in_other_list(liste1, liste2))

print()
liste1 = ["Bernard", "Antoine", "Fabrice"]
liste2 = ["Antoine", "Fabrice", "Bernard"]
print(are_in_other_list(liste1, liste2))

print()
liste1 = ["Bernard", "Antoine", "Fabrice", "John", "Frédéric"]
liste2 = ["Antoine", "Fabrice", "Bernard"]
print(are_in_other_list(liste1, liste2))
