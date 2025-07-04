# 类与对象的基本结构
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"你好,我是{self.name},今年{self.age}岁")


# 创建对象
p = Person("Asher", 20)
p.say_hello()


# 类的继承
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # 继承父类属性
        self.grade = grade

    def say_score(self):
        print(f"{self.name}的分数是{self.grade}")


p1 = Student("Asher", 20, 100)
p1.say_hello()
p1.say_score()


# 任务
class Student1:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        print(f"我是{self.name},年龄{self.age},分数{self.score}")


p2 = Student1("Asher", 21, 90)
p3 = Student1("Mike", 20, 80)
p2.introduce()
p3.introduce()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


p4 = Rectangle(5, 10)
print(p4.area())
print(p4.perimeter())


class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"Balance: {self.balance}")


p5 = Account("Jose", 100)
p5.deposit(10)
p5.withdraw(200)
p5.show_balance()
