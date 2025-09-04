class Parent:
    def __init__(self, father_name, mother_name, father_age, mother_age):
        self.father_name = father_name
        self.mother_name = mother_name
        self.father_age = father_age
        self.mother_age = mother_age


class Child(Parent):
    def __init__(self, name, age, father_name, mother_name, father_age, mother_age):
        
        super().__init__(father_name, mother_name, father_age, mother_age)
        self.name = name
        self.age = age

    def display(self):
        print(f"My name: {self.name}")
        print(f"My Age: {self.age}")
        print(f"My Father's Name: {self.father_name}")
        print(f"My Father's Age: {self.father_age}")
        print(f"My Mother's Name: {self.mother_name}")
        print(f"My Mother's Age: {self.mother_age}")



s1 = Parent("Virat Kohli", "Anushka Sharma", 42, 34)
s2 = Child("Viruksha", 23, "Virat Kohli", "Anushka Sharma", 42, 34)


s2.display()
