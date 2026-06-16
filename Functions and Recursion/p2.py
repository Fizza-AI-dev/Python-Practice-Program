#celsius to foreign height

def c_to_f(f):
    return 5*(f-32)/9
f=int(input("enter temperature"))
c=c_to_f(f)
print("temp is : ",round(c,2))
