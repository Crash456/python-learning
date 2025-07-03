# 条件语句 if-elif-else
score = 85

if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
else:
    print("需要努力")

# for 循环:遍历列表

names = ["Asher", "Tom", "jerry"]

for name in names:
    print("你好", name)

# 遍历数字范围

for i in range(5):
    print(i)
# while 循环

count = 0
while count < 3:
    print("现在是第", count + 1, "次")
    count += 1


# 任务
score = 92
if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

nums = [10, 20, 30, 40]
sum = 0
for num in nums:
    sum += num
print(sum)

# 这个不对
for i in range(3):
    for j in range(3):
        if j <= i:
            print("*")
# 这个对
for i in range(1, 4):
    print("*" * i)
