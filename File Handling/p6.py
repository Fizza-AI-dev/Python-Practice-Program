with open("log.txt") as f:
    content=f.read()

if("python" in content):
    print("yes present")
else:
    print("not present")
