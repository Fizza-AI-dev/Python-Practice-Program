m1=int(input("enter subject 1:"))
m2=int(input("enter subject 1:"))
m3=int(input("enter subject 1:"))

total_percentage=(100)*(m1+m2+m3)/300

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("you are pass",total_percentage)
else:
    print("you are failed",total_percentage)