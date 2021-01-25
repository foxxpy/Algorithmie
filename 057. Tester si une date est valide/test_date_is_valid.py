from date_is_valid import date_is_valid

def test_date_is_valid():
    j1, m1, a1 = 20, 2, 2020
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 29, 2, 2000
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 29, 2, 1900
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = -4, 5, 2020
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 60, 7, 2000
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 12, 13, 2020
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 1, 0, 2020
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 0, 5, 2020
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 31, 12, 2020
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 30, 8, 2020
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 1, 1, 0
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    j1, m1, a1 = 2, 2, 10284
    print("{}/{}/{} : {}".format(j1,m1,a1,date_is_valid(j1,m1,a1)))

    
test_date_is_valid()
