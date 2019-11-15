import operator
from functools import reduce

"""
dynamic_reduder([1, 2, 3,], '+' )# 6
dynamic_reduder([1, 2, 3,], '-' )# -
dynamic_reduder([1, 2, 3,], '*' )# -
dynamic_reduder([1, 2, 3,], '/' )# -
"""
def dynamic_reducer(collection, op):
    operators = {
       "+": operator.add,
       "-" : operator.sub,
       "*" : operator.mul,
       "/" : operator.truediv 
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)


print (dynamic_reducer([1, 2, 250], '+'))
print (dynamic_reducer([1, 2, 3], '-' ))
print (dynamic_reducer([1, 2, 55], '*' ))
print (dynamic_reducer([100, 2, 3], '/' ))



