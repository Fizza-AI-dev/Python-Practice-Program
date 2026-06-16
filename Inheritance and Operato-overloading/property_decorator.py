class employee:
    a=2
    # @classsmethod
    def show(self):
        print(f"{self.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

        

object=employee()
object.name="hira nazir"
print(object.fname,object.lname)
# object.a=45 #it will show 2 instead of 45 because of class method

object.show()