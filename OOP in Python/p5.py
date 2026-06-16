from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"{self.trainNo}")

    def getFare(self,fro,to):
        print(f"{randint(222,555)}")

t=train(22399)
t.book("lahore","karachi")
t.getFare("lahore","karachi")