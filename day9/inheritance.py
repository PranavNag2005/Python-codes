class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)

class student(person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def mark(self):
        super().printname()
        print(f"{self.name} got {self.marks} in the end exam")

s = student("pranav", 45, 45)
s.mark()
