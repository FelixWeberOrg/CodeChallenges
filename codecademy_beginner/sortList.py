"""
2.Sort a list

Create a function in Python that accepts two parameters.
The first will be a list of numbers.
The second parameter will be a string that can be one of the following values: asc, desc, and none.
If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
If it's "desc," then the list should be in descending order, and if it's "none," it should
return the original list unaltered.
"""


mylist = [1, 2, 3, 5, 6, 7, 10, 4, 11, 81, 81, 82]

print(type(mylist))


def sortList(page, param):
    if (param == "asc" or param == "desc" or param == "none") and (type(page) == list):

        if param == "asc":
            return sorted(page)

        elif param == "desc":
            return sorted(page, reverse=True)

        else:
            return page

    else:
        return "something is wrong"


print(sortList(mylist, "asc"))
