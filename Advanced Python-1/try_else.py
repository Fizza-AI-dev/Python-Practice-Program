try:
  a=int(input("enter number:"))
except Exception as e:
    # print("hey please enter a valid number")
    print(e)

else:
   print("i am inside else")