"""
1. Convert radians into degrees

Write a function in Python that accepts one numeric parameter.
This parameter will be the measure of an angle in radians.
The function should convert the radians into degrees and then return that value.
While you might find a Python library to do this for you, you should write the function yourself.
One hint you get is that you'll need to use Pi in order to solve this problem.
You can import the value for Pi from Python's math module.
"""

from math import pi


def radiantToDegree(rad):
    try:
        deg = (rad / (2 * pi)) * 360
        return deg

    except:
        return "Enter valid factor!"


value = input("Enter Radiant as factor of pi: ")

try:
    value = int(value)
    value = value * pi

except:
    value = "not a valid factor!"


print("Calculating degree value of radiant: " + str(value))

radiant = radiantToDegree(value)

print("Radiant: " + str(radiant))
