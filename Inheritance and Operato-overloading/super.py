class employee:
    def __init__(self):
        print("constructor of employee")
    a=2

class programer(employee):
     def __init__(self):
         super().__init__()

         print("constructor of programer")
     b=4

class coder(programer):
     def __init__(self):
        super().__init__()
        print("constructor of coder")
     c=6

object=employee()
print(object.a)

object=programer()
print(object.a,object.b)

object=coder()
print(object.a,object.b,object.c)