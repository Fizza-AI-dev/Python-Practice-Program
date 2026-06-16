class employee:
    a=2
    @classmethod
    def show(cls):
        print(f"{cls.a}")

object=employee()
object.a=45 #it will show 2 instead of 45 because of class method

object.show()