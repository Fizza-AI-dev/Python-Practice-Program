import random

def dice_rolling():
    while True:
        dice=random.randint(1,6)
        print(f"you rolled:{dice}")

        choice=input("you want to roll again(y/n)").lower()
        #  if choice=='y':
        #     dice=random.randint(1,6)
        #     choice=input("you want to roll again(y/n)").lower()
        #     dice_rolling()
        # print(f"you rolled:{dice}")


        if choice=='n':
             print("Thanks for playing! GoodBye")
             break
        
dice_rolling()
             
        # elif choice=='y':
        #     dice_rolling()
        #     dice=random.randint(1,6)
        # # print(f"you rolled:{dice}")

        # choice=input("you want to roll again(y/n)").lower()

