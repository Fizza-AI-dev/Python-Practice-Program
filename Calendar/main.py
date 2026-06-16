import calendar

def show_calendar():
    try:
       year=(int(input("Enter a Year: ")))
       month=(int(input("Enter a Month: ")))
       print("/n calendar")
       print(calendar.month(year,month))

    except ValueError:
     print("Enter a valid number")


def main():
  while True:
    print(".....calendar......")
    print("1,Show calendar")
    print("2,Exit!")
    choice=input("choose options")
    
    if choice== '1':
      show_calendar()
    elif choice=='2':
       print("GoodBye")
       break
    else:
       print("Invalid choice.....")

main()

   

