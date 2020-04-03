def caller(func, params):
    return func(*params)

def printer(name, origin):
    print("I'am {} of {}!".format(name, origin))

caller(printer, ["moana", "Motunui"])
########################$$$Map Fucntion$$$#########################



#map(func, iterable_object)# it applies func on each element of the iterable_object

"""def squarify(a):
    return a ** 2

list(map(squarify, range(5)))
Output: [0, 1, 4,9, 16]"""

#######################$$$Filter function$$$#######################


#filter(func, iterable_object) it applies func on each element and return True results of func
"""def is_positive(a):
    return a > 0

list(filter(is_positive, range(-2, 3)))

Output: [1, 2]"""


#######################$$$Lambda func$$$############################


#lambda param: actions  anonymous func. Usually used if you need t only in the context
"""list(map(lambda x: x ** 2, range(5)))

type(lambda x: x ** 2)
Output: function"""
