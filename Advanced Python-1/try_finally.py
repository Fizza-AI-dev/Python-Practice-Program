try:
  a=int(input("enter number:"))
except Exception as e:
    # print("hey please enter a valid number")
    print(e)



finally:
   print("i am inside of finally")