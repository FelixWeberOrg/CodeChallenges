"""
7. Create a calculator function

Write a Python function that accepts three parameters.
The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or .
The third parameter will also be an integer.
The function should perform a calculation and return the results.
For example, if the function is passed 6 and 4, it should return 24.
"""

def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "invalid operator"


print(calculate(4, "*", 6))
print(calculate(10, "-", 11))
print(calculate(40, "/", 6))
print(calculate(10, "+", 11))
