l=[3,5,15,34,25]
def divisible(n):
    if(n%5==0):
        return True
    return False
onlyDivisible=filter(divisible,l)
print(list(onlyDivisible))