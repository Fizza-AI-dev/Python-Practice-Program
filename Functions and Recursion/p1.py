# a=2
# b=3
# c=4

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(greatest(2,3,4))
