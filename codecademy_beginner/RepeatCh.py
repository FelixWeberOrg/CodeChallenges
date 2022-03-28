"""
10. Repeat the characters

Create a Python function that accepts a string.
The function should return a string, with each character in the original string doubled.
If you send the function "now" as a parameter, it should return "nnooww,"
and if you send "123a!", it should return "112233aa!!".
"""

teststr = "12 hey you!"


def doubleCh(words):

    words_out = ""
    for cha in words:

        if cha != " ":

            words_out = words_out + cha + cha

        else:
            words_out = words_out + cha

    return words_out


print(doubleCh(teststr))
