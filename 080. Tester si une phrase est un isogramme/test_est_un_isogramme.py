from est_un_isogramme import est_un_isogramme

print("----- ISOGRAMME -----")
string = "Dodo"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "Grain"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "MANGER"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "MouLinE"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "DélatION"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "SaXoNiQuE"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "complaire"
print("{} : {}".format(string, est_un_isogramme(string)))

print("\n----- NON ISOGRAMME -----")

string = "mEnteur"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "Battre"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "créé"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "créée"
print("{} : {}".format(string, est_un_isogramme(string)))

string = "maîtriser"
print("{} : {}".format(string, est_un_isogramme(string)))
