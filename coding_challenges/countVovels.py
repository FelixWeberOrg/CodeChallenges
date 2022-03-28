"""
4. Count the vowels in a string

Create a function in Python that accepts a single word and returns the number of vowels in that word.
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""


teststring = "I am Bob Ross, there are some vowels in that sentence."

vowels = ["a", "e", "i", "o", "u"]


def countVow(sentence):
    numOfVow: int = 0
    sentence = sentence.lower()
    print(sentence)

    for letter in sentence:
        print(letter)
        if letter in vowels:
            numOfVow += 1

    return numOfVow


print(countVow(teststring))
