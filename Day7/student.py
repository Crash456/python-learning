class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        print(
            f"My name is {self.name}, I am {self.age} years old, and my score is {self.score}"
        )
