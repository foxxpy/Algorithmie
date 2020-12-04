from pjoin import pjoin

def test_pjoin():
    liste = ["F", "o", "x", "x,", "p", "y"]
    print(pjoin("", liste))
    print(pjoin("-", liste))
    print(pjoin(" ", liste))
    print(pjoin("xxx", liste))
    print(pjoin("Danseaveclesstars", liste))

test_pjoin()
