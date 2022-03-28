"""
9. Just the numbers

Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings.
The function should return a list with only the integers in the original list in the same order.
"""
mix = ["lels", 12, 2, 0, 11, "peter", 3]

def justnum(mixlist):

    outlist = []

    for item in mixlist:
        try:
            outlist.append(int(item))
        except:
            continue

    return outlist


print(justnum(mix))
