from occurrence import occurrence

def test_occurence():
    liste = [1,2,3,4,1,1, 2, 3]
    print(occurrence(liste, 1)) #Le 1 est présent 3 fois
    print(occurrence(liste, 2)) #Le 2 est présent 2 fois
    print(occurrence(liste, 3)) #Le 3 est présent 2 fois

test_occurrence()
