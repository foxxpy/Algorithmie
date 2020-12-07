from bissextile import bissextile

def test_bissextile():
    print("2000 : ", bissextile(2000))
    print("1900 : ", bissextile(1900))
    print("331 : ", bissextile(331))
    print("1 : ", bissextile(1))
    print("1800 : ",bissextile(1800))
    print("16 : ", bissextile(16))
    print("100 : ",bissextile(100))
    print("2020 : ", bissextile(2020))
    print("0: ", bissextile(0))
    print("-4 : ", bissextile(-4))
test_bissextile()
