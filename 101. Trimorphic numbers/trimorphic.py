def trimorphic(n):
    """Un nombre trimorphique est un nombre dont le cube se termine par les mêmes
    chiffres que le nombre qui a été calculé au cube"""

    len_n = len(str(n))

    #i représente la longueur de n (len_n ci-dessus)
    #Si les i derniers caractères de n**3 sont égaux à n, alors n est trimorphic
    if str(n**3)[-len_n:] == str(n):
        return True
    else:
        return False
