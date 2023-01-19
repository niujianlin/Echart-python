# 统计文本中特定字符的出现次数

# f读完记录位置，下次从该位置接着读

f = open("C:/partF/programs/test/testword.txt", "r", encoding="UTF-8")
# line1 = f.readline()
# print(f"{f.read()}\n类型是:{type(f.read())}")
# print(f"{lines}")
# list = f.read().split(" ")
count = 0
for line in f:
    print(f"每一行数据是：{line} ，类型是：{type(line)}")
    # 去掉换行符\n：strip()
    line = line.strip()
    for elem in line.split(" "):
        if elem == "itheima":
            count += 1

print(f"count={count}")

f.close()
