n1=int(input("Enter a first number:"))
n2=int(input("Enter a second number:"))
n3=int(input("Enter a third number:"))

if(n1>n2 and n1>n3):
    print(f"Largest is {n1}")
elif(n2>n1 and n3>n3):
    print(f"Largest is {n2}")
else:
    print(f"largest is {n3}")
