a1=int(input("enter number:"))
a2=int(input("enter number:"))
a3=int(input("enter number:"))
a4=int(input("enter number:"))


if(a1>a2 and a1>a3 and a1>a4):
    print("greater is:",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("greater is:",a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("greater is:",a3)
# elif(a1>a2 and a1>a3 and a1>a4):
else:
    print("greater is:",a4)
