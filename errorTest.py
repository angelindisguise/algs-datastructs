# Python program for binary search
import random
# Create randomNumbers array


def randomNumbersArray():
    randomnumbers = []
    i = 0
    while i < 24:
        randomnumbers.append(random.randint(1, 100))
        i += 1

    print(randomnumbers)
    print(len(randomnumbers))
    print()

    return randomnumbers


def sorting(randomnumbers):
    list.sort(randomnumbers)
    print(randomnumbers)

    return randomnumbers


randnums = randomNumbersArray()
sorting(randnums)
