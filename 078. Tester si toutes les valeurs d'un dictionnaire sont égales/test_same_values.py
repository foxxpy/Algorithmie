from same_values import *

dictionnaire = {"a" : 1, "b" : 1}
print(dictionnaire)
print(same_values(dictionnaire))
print(same_values_set(dictionnaire))
print()

dictionnaire = {"a" : 1, "b" : 2}
print(dictionnaire)
print(same_values(dictionnaire))
print(same_values_set(dictionnaire))
print()

dictionnaire = {"Johnny" : 1000, "Sarah" : 1000}
print(dictionnaire)
print(same_values(dictionnaire))
print(same_values_set(dictionnaire))
print()

dictionnaire = {"Johnny" : 1000, "Sarah" : 1000, "Bernard" : 999}
print(dictionnaire)
print(same_values(dictionnaire))
print(same_values_set(dictionnaire))
print()

dictionnaire = {"a" : 1, "b" : 1, "c" : 1, "d" : "bonjour"}
print(dictionnaire)
print(same_values(dictionnaire))
print(same_values_set(dictionnaire))
print()
