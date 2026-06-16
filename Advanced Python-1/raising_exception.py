# We can raise custom exceptions using the ‘raise’ keyword in python/

a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
# a=int(input("enter a number3:"))

if(b==0):
    raise ZeroDivisionError("hey not divide by zero")
else:

  print(f"a/b is{a/b}")
