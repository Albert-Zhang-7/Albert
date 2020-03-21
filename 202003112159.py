class Father:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Father named %s can eat." % self.name)


class Mother:
    def walk(self):
        print('walk like mother.')


class Son(Father, Mother):
    def eat(self):
        print("eat like son")


littleSon = Son(name="Albert")
littleSon.eat()
littleSon.walk()
