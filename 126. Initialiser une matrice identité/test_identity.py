from identity import identity, alt_identity
from pprint import pprint

for i in range(1, 11):
    print("--------- {} ---------- \n".format(i))
    pprint(identity(i))
    print()
    pprint(alt_identity(i))
    print()
