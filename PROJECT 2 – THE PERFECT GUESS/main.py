import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    a=int(input("Guess a number:"))
    if(a>n):
        print("Lower number please!")
        guesses=guesses+1

    elif(a<n):
        print("Higher number please!")
        guesses=guesses+1


print(f"you have guess the number correctly {n} in {guesses} attempt!")
    