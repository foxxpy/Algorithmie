from both_list import both_list

#Instanciation de liste1 et liste2
liste1 = []
liste2 = []

#Premier test
for i in range(1,21):
    liste1.append(i)
for i in range(10,21):
    liste2.append(i)
print(both_list(liste1, liste2))

#Second test
liste1 = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2]
liste2 = [4,5,6,7,8,9,10,11,12,13,14,15,1,18,19]
print(both_list(liste1, liste2))
