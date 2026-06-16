from functools import reduce
l=[2,5,89,56]
def max(a,b):

    if(a>b):
        return a
    return b

print(reduce(max,l))