import random

def game():
    print("you are playing the game")
    score=random.randint(1,62)
    #fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"you score:{score}")
    if(score>hiscore):
        #write this hiscore to the file
        with open ("hiscore.txt", "w") as f:
            f.write(str(score)) #write fun takes the string
    return score

game()







