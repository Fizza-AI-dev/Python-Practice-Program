class employee:
    a=2

class programer(employee):
    b=4

class coder(programer):
    c=6

object=employee()
print(object.a)

object=programer()
print(object.a,object.b)

object=coder()
print(object.a,object.b,object.c)