# 列表推导式
nums = [1, 2, 3, 4, 5]
squares = [x * x for x in nums]
print(squares)

# 条件过滤版本
evens = [x for x in nums if x % 2 == 0]
print(evens)

# 常用内置函数
names = ["Asher", "Tom", "Jerry"]
for idx, name in enumerate(names):
    print(idx, name)

a = [1, 2, 3]
b = ["a", "b", "c"]
for x, y in zip(a, b):
    print(x, y)

# 任务
list1 = [x for x in range(1, 11) if x % 2 == 0]
print(list1)
list2 = [x * x for x in range(1, 11)]
print(list2)

list3 = [x for x in range(1, 21) if x % 3 == 0]
print(list3)

names = ["Asher", "Tom", "Jerry"]
scores = [90, 85, 78]

for x, y in zip(names, scores):
    print(x, "的分数是", y)

list4 = [1, 2, 3, 4, 5]
print(sum(list4))
print(max(list4))
print(min(list4))
print(list(reversed(list4)))

for id, name in enumerate(list4):
    print(id, name)

nums = [1, 2, 3, 4, 5]
times_10 = list(map(lambda x: x * 10, nums))
print(times_10)  # [10, 20, 30, 40, 50]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]
