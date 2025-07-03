# 函数定义与调用
def say_hello(name):
    print("你好," + name + "!")


say_hello("小王")


# 函数返回值
def add(x, y):
    return x + y


result = add(3, 5)
print(result)


# 默认参数
def greet(name="同学"):
    print(f"你好,{name}!")


greet()
greet("小王")

# 局部变量 VS 全局变量
x = 10


def foo():
    x = 5
    print("函数内", x)


foo()
print("函数外", x)


# 任务
def is_even(num):
    return num % 2 == 0


print(is_even(10))
print(is_even(7))


def get_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


print(get_grade(85))


def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


print(sum_list([1, 2, 3, 4, 5]))


def print_star_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


print_star_pyramid(4)
