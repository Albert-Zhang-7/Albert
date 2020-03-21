# def __init__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, 'can walk')
        print(self.name, 'is', self.age)


s1 = Student("Albert", "18")
s1.walk()
s2 = Student(name="Min", age="33")
s2.walk()
