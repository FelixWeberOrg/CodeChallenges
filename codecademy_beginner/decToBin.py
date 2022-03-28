"""
3. Convert a decimal number into binary

Write a function in Python that accepts a decimal number and returns the equivalent binary number.
To make this simple, the decimal number will always be less than 1,024, so the binary number returned will
always be less than ten digits long.
"""

def decToBin(decimal):
    try:
        binary = str(bin(decimal))[2:]
        binary = int(binary)
        return binary

    except:
        return "something is wrong"


print(decToBin(1024))
