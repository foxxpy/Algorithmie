from poids_hamming import poids_hamming, poids_hamming_leetcode

for i in range(1,100):
    print(poids_hamming(bin(i)))
    print(poids_hamming_leetcode(bin(i)))
    print()
