class number:
    def __init__(self,n):
       self.n=n


    def __add__(self,num):
     return self.n + num.n


n=number(12)
m=number(13)

print(n+m)
