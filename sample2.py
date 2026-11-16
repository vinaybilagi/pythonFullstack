class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def study(self):
        print(f"{self.name} is studying")


# Creating an object
s1 = Student("Rahul", 22)

# Calling methods
s1.display()
s1.study()