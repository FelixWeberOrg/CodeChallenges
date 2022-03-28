"""
5. Hide the credit card number

Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent "4444444444444444", then it should return "4444".
"""

cardnr = 1234123412349999


def hidenr(nr):
    nr = str(nr)[12:]
    return "************" + nr


print(hidenr(cardnr))
