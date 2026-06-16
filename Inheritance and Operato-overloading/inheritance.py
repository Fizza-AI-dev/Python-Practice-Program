class employee:
    company="microsoft"
    def show(self):
        print(f"name is {self.name} and salary {self.salary}")

# class programer:
#     company="google"
#     def show(self):
#         print(f"name is {self.name} and salary {self.salary}")

# class showLanguage:
#     def show(self):
#         print(f"name is {self.name} and salary {self.salary}")

class programer(employee):
    company="microsoft"

a=employee
b=programer

print(a.company,b.company)