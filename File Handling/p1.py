f=open("poems.txt")
user=input("enter a word:")

content=f.read()
if (user in content):
    print("word is present")
else:
    print("not present")
f.close()