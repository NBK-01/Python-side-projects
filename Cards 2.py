import itertools
import random


deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))


random.shuffle(deck)


print("You have:")
for i in range(14):
    print(deck[i][0], "of", deck[i][1])
