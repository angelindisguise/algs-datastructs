# Python program for binary search
import random
# Create randomNumbers array


def randomNumbersArray():
    randomnumbers = []
    i = 0
    while i < 24:
        randomnumbers.append(random.randint(1, 100))
        i += 1

    print(f"\nRandom unsorted list of numbers {randomnumbers}\n")

    return randomnumbers


def sorting(randNums):
    list.sort(randNums)
    print(f"Sorted list of random numbers {randNums}\n")

    return randNums


def numToGuess(numbers):
    pos = random.randint(0, (len(numbers)-1))
    target = numbers[pos]

    print(f"Position is {pos}")
    print(f"What number am I thinking of? {target}\n")

    return target, pos


def binSearch(target, numbers, pos):
    minimum = 0
    maximum = len(numbers)-1
    guess = round((maximum + minimum)/2,)

    while guess != pos:

        if guess < pos:
            valGuess = numbers[guess]
            print(f"My guess is {valGuess} at position {guess}")
            print("Target position is larger than your guess\n")

            minimum = guess + 1
            guess = round((maximum + minimum)/2, )

        elif guess > pos:
            valGuess = numbers[guess]
            print(f"My guess is {valGuess} at position {guess}")
            print("Target is less than your guess\n")

            maximum = guess - 1
            guess = round((maximum + minimum)/2, )

    else:
        print(f"My final guess is {guess}")
        print(f"That's right my number is {target}!")


def main():
    randNums = randomNumbersArray()
    sortedNums = sorting(randNums)
    target, pos = numToGuess(sortedNums)
    binSearch(target, sortedNums, pos)


main()
