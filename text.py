#題目一
class MyClass:
    def __init__(self, attribute1, attribute2, attribute3):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

    def function1(self):
        print(f"Function 1 called. Attributes: {self.attribute1}, {self.attribute2}, {self.attribute3}")

    def function2(self):
        print(f"Function 2 called. Attributes: {self.attribute1}, {self.attribute2}, {self.attribute3}")

    def function3(self):
        print(f"Function 3 called. Attributes: {self.attribute1}, {self.attribute2}, {self.attribute3}")

obj1 = MyClass("A1", "B1", "C1")
obj2 = MyClass("A2", "B2", "C2")
obj3 = MyClass("A3", "B3", "C3")

obj1.function1()
obj1.function2()
obj1.function3()

obj2.function1()
obj2.function2()
obj2.function3()

obj3.function1()
obj3.function2()
obj3.function3()

#題目二
