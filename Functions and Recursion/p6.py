l=["hira","dani","mai"]

# def rem(l,word):
#     for item in l:
#          l.remove(word)
#          return l
# print(rem(l,"hira"))
def rem(l,word):
    n=[]
    for item in l:
         if not(item==word):
              
           l.append(item.strip(word))
    return n
print(rem(l,"hira"))