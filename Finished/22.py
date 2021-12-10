#!/usr/bin/env python3

LETTER_VALUES = {
    "A": 1
    , "B": 2
    , "C": 3
    , "D": 4
    , "E": 5
    , "F": 6
    , "G": 7
    , "H": 8
    , "I": 9
    , "J": 10
    , "K": 11
    , "L": 12
    , "M": 13
    , "N": 14
    , "O": 15
    , "P": 16
    , "Q": 17
    , "R": 18
    , "S": 19
    , "T": 20
    , "U": 21
    , "V": 22
    , "W": 23
    , "X": 24
    , "Y": 25
    , "Z": 26
}

def main():
    # Read file
    f = open("22_names.txt", "r")
    names = []
    for name in f.read().split(","):
        names.append(name.replace('"', ''))
    names.sort()

    # Alphabetical score --> Name score --> Increment
    result = 0
    for i, name in enumerate(names):
        alphabeticalValue = 0
        for letter in name:
            alphabeticalValue += LETTER_VALUES[letter]
        result += alphabeticalValue * (i + 1)
        # print(f"Appended {name} with value {alphabeticalValue * (i + 1)}")
    print(f"Sum of name scores is: {result}")

if __name__ == "__main__":
    main()
