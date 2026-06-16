class employee:
    company="microsoft"
    name="hira"
    salary=67000
    def show(self):
        print(f"name is {self.name} and salary {self.salary}")

class coder:
    language="python"
    def printLang(self):
        print(f"{self.language}")

# class programer:
#     company="google"
#     def show(self):
#         print(f"name is {self.name} and salary {self.salary}")

# class showLanguage:
#     def show(self):
#         print(f"name is {self.name} and salary {self.salary}")

class programer(employee, coder):
    company="google"

a=employee()
b=programer()
b.show()
b.printLang()


# print(a.company,b.company,b.printLang)