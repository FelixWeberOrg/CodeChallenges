"""
6. Are the Xs equal to the Os?

Create a Python function that accepts a string.
This function should count the number of Xs and the number of Os in the string.
It should then return a boolean value of either True or False.
If the count of Xs and Os are equal, then the function should return True.
If the count isn't the same, it should return False.
If there are no Xs or Os in the string, it should also return True because 0 equals 0.
The string can contain any type and number of characters.
"""

teststr_1 = "aksnjfoooxxx"  # same nr of x and o
teststr_2 = "aksnjfooxxxx"  # not same nr of x and o


def compXO(sentence):
    numOfX = 0
    numOfO = 0

    sentence = sentence.lower()

    for letter in sentence:
        if letter == "x":
            numOfX += 1
        elif letter == "o":
            numOfO += 1

    if numOfX == numOfO:
        return True
    else:
        return False


print(compXO(teststr_1))
print(compXO(teststr_2))
