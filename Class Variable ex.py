class Staff:
    cnt = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Staff.cnt = Staff.cnt+1
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("\n")

s1 = Staff("Sedhu",22)
s1.display()
s2 = Staff("Lingam",23)
s2.display()
print("Total Objects Created: ",Staff.cnt)