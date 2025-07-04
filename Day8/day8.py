import numpy as np

# 创建数组
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
print("a:", a)
print("b:", b)
# 常用的初始化方式
print(np.zeros((2, 3)))  # 两行三列  全0
print(np.ones((2, 2)))  # 两行两列  全1
print(np.eye(3))  # 单位矩阵
print(np.arange(0, 10, 2))  # 从0到10的步长为2的数组
print(np.random.rand(2, 2))  # 随机数

# 数组的基本操作
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
print(x * y)
print(np.dot(x, y))  # 点乘

m = np.array([[1, 2], [3, 4]])
print(m.T)  # 转置

# 索引与切片
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0, 1])  # 第一行第二列
print(arr[:, 1])  # 所有行第二列
print(arr[1, :])  # 第二行所有列

# 任务
matrix = np.eye(3)
print(matrix)
vector = np.arange(1, 101)
vector[vector % 3 == 0] = 0
print(vector)
