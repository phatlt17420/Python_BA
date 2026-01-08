class Person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    def Display (self):
        print (f"Tên: {self.Name} | Tuổi: {self.Age}")
class Student(Person):
    def __init__(self, Name, Age):
        super().__init__(Name, Age)
    def displayStudent(self):
       self.Display()

SVA = Student('Nguyễn Văn A',30)
SVA.displayStudent()

