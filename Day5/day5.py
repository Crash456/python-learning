# 操作文本文件.txt

# 写入文件(覆盖写入)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("你好,Asher\n")
    f.write("hello world")
# 追加写入
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("继续学习")
# 读取文件内容
with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 操作CSV文件

import csv

# 写入CSV文件
with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "分数"])
    writer.writerow(["Asher", 95])
    writer.writerow(["Tom", 88])
# 读取CSV文件
with open("output.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 操作JSON文件
import json

data = {"name": "Asher", "score": 95, "pass": True}
# 写入JSON文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
# 读取JSON文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)


# 任务
with open("info.txt", "w", encoding="utf-8") as f:
    f.write("你好,Asher\n")
    f.write("欢迎来到python的世界")
with open("info.txt", "r", encoding="utf-8") as f:
    print(f.read())

import csv

with open("student.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "分数"])
    writer.writerow(["Asher", 100])
    writer.writerow(["Tom", 90])
with open("student.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    # 跳过标题行
    next(reader)
    for row in reader:
        name, score = row  # 解包每一行
        print(f"{name} 的分数是 {score}")

import json

data = {"name": "Asher", "age": 20, "skills": ["Python", "Git", "深度学习"]}

with open("info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
with open("info.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
