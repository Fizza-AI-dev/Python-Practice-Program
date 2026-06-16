try:
    a=int(input("no 1"))
    b=int(input("no 2"))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")

print("thank you")