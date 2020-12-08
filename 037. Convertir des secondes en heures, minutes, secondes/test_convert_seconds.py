from convert_seconds import convert_seconds

def test_convert_seconds():
    h, m ,s = convert_seconds(360)
    print("360 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(60)
    print("60 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(3600)
    print("3600 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(3601)
    print("3601 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(10000)
    print("10000 : ", h, " heures, ", m, " minutes, ", s, " secondes")

    h, m ,s = convert_seconds(45)
    print("45 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(7442)
    print("7442 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(64)
    print("64 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(122000)
    print("122000 : ", h, " heures, ", m, " minutes, ", s, " seconde")

    h, m ,s = convert_seconds(6845)
    print("6845 : ", h, " heures, ", m, " minutes, ", s, " secondes")

test_convert_seconds()
