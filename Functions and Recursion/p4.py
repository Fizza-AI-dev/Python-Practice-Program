def pattern(n):
    if(n==0):
        return# function call stop
    else:
        print("*"*n)
        pattern(n-1)


print(pattern(3))