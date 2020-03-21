class Student():
    name = input("Your name is: ")
    age = input("Your age is: ")

    def eat(self):
        print('Student named %s can eat and he is %s.' % (self.name, self.age))

    @staticmethod
    def walk():
        print('Student can walk.')


Stu = Student()
Stu.eat()
Stu.walk()
