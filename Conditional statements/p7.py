marks=int(input("enter marks:"))

if(marks<=100 and marks>=90):
    print("Excellent")
elif(marks<0 and marks>=80):
    print("A grade")
elif(marks<80 and marks>=70):
    print("B grade")
elif(marks<70 and marks>=60):
    print("C grade")
elif(marks<60 and marks>=50):
    print("D grade")
else:
    print("you are fail")