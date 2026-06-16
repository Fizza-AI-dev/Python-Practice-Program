class employee:
    language="english"  #class attribute
    salary=2000000

    def getinfo(self):
        print(f"{self.salary} and {self.language}")



hira=employee()
hira.name="Hira Nazir"  #object attribute/instance attribute
print(
     
    hira.salary,
    hira.name,
    hira.language,
    

)
hira.getinfo()