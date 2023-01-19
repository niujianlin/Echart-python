"""
本代码演示
各类字面量的写法
"""
from random import random

666
money = 123.14
print("money=", money, "元")
print("money=", money - 10, "元")
"niu"
# 输出
print(666)
print(13.14)
print("牛建霖")

name = "niujl"
age = 10
# age = str(age)
print("年龄：" + str(age))
# 注意没有逗号
print("年龄：%d" % age)
print("年龄：%d，姓名：%s" % (age, name))

price = 19.99
year = 2006
print("价格是%.1f" % price)
# %m.nf m是宽度（不常用） n是小数精度（有四舍五入）
print("价格是%4.1f" % price)
# 使用f"{}" ，不控制精度，原封不动，方便，可以计算表达式
print(f"价格是{price}，年份是{year}，明年的年份是{year + 1}")

# 判断语句
if age >= 10:
    print("大于等于10岁")
else:
    print("小于10岁")
print("缩进则判断，不缩进直接输出")

if age >= 10:
    print("大于等于10岁")
elif age == 9:
    print("等于9岁")
else:
    print("小于9岁")

# 循环语句
i = 0
while i < 100:
    print("%d" % i)
    i += 1

# range(3) -> 0 1 2
# range(1,4) -> 1 2 3
# range(1, 5, 2) -> 1 3 (从1开始相差2输出，不包括5)
for i in range(5):
    print(i)
# 循环 打印99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end=' ')
    # 换行
    print()

# import random
num = random.randint(4, 10)
print(f"{num}")

# 列表（数组）

mylist = ["niujl", "niuniu", "python"]
# 元素对应下标位置
index = mylist.index("niuniu")
print(f"{index}")
# 取最后一个元素
element = mylist[-1]
print(f"{mylist}")
# 在对应位置插入元素
mylist.insert(1, "best")
print(f"{mylist}")
# 在末尾追加元素
mylist.append("666")
print(f"{mylist}")

# extend列表尾部追加一批元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"{mylist}")

# 删除列表元素
mylist3 = [1, 2, 3, 4]
del mylist3[1]
print(mylist3)
mylist3 = [1, 2, 3, 4]
mylist3.pop(1)
print(mylist3)
mylist3 = ["name", "age", "city", "country"]
mylist3.remove("age")
print(mylist3)
# 清空列表
mylist3.clear()
print(f"列表被清空，结果是：{mylist3}")
# 统计列表有多少相同元素
mylist3 = ["name", "age", "name", "country"]
num = mylist3.count("name")
print(f"相同元素有{num}个")
# 统计列表全部元素数量
print("列表一共有%d个元素" % (len(mylist3)))

# 列表的遍历
i = 0
while i < len(mylist3):
    ele = mylist3[i]
    print(f"第{i}个元素是{ele}")
    i += 1

for elem in mylist3:  # 把mylist3挨个取出来给elem
    print(f"列表元素有：{elem}")

# 元组 不能篡改
t1 = (1, "hello, True")
t2 = ()
t3 = tuple()  # 空元组

t4 = ("Hello")
print(f"t4的类型是{type(t4)}")
# 定义一个单独的元组，必须加逗号！
t4 = ("Hello",)
print(f"t4的类型是{type(t4)}")

# 二维元组，支持index(元素) count(元素) len(元组)
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5:{t5}")
# 元组遍历与列表相同

# 字符串replace()
my_str = "niujl"
new_str = my_str.replace("jl", "99")
print(f"{my_str}----{new_str}")
# 字符串split() 将字符串分割成列表
my_str = "hello python world"
new_str = my_str.split(" ")
print(f"数据是{new_str}，类型是{type(new_str)}")
# 字符串strip方法，不传参去除首尾空格
my_str = "  hello python!  "
new_str = my_str.strip()
print(f"字符串{my_str}被strip后，结果：{new_str}")
# 字符串strip方法，传参则去除参数
my_str = "12hello python!21"
new_str = my_str.strip("12")
print(f"字符串{my_str}被strip12后，结果：{new_str}")
# 子字符串出现次数用count()  字符串长度用len()

# 列表、元组、字符串的切片
mylist = [0, 1, 2, 3, 4, 5, 6]
result1 = mylist[1:4]  # 默认步长是1
print(f"结果1：{result1}，类型是{type(result1)}")

result2 = mylist[:]  # 默认步长是1
print(f"结果2：{result2}，类型是{type(result2)}")

mylist_tuple = (0, 1, 2, 3, 4, 5, 6)
result3 = mylist_tuple[:]  # 默认步长是1
print(f"结果3：{result3}，类型是{type(result3)}")

my_str = "01234567"
result4 = my_str[::2]  # 没写就是从头到尾，最后步长为2
print(f"结果4：{result4}，类型是{type(result4)}")
result5 = my_str[::-1]  # -1表示从尾到头，步长为1
print(f"结果5：{result5}，类型是{type(result5)}")
result6 = my_str[3:1:-1]  # -1表示从后到头前，步长为1
print(f"结果6：{result6}，类型是{type(result6)}")
result7 = my_str[6:1:-2]  # -2表示从后到头前，步长为2
print(f"结果7：{result7}，类型是{type(result7)}")

# 切片练习：只要"黑马程序员"
str_practise = "万过薪月，员序程马黑来"
res = str_practise[::-1]
print(f"{res}，类型是{type(res)}")
res1 = res[1:6]
print(f"{res1}")

# 集合  去重，无序，无下标，支持for elem in set: ，不支持while，因为没下标
# .add() .remove() .pop()(随机删除) .clear() .union() .len()(不含重复)
# .difference(集合2)(得到新集合，包含差集) .difference_update(集合2)(消除和集合2相同的元素)
my_set = {"hello", "world", "python"}
# 空集合定义
my_set = set()

# 字典 （key:value） 无序、武侠表、不支持重复key,直接覆盖
# 添加\修改:dict[key]=value 获取全部key:.keys() 清空:.clear() 键值对数量:len()
# 字典定义
{"niu": 1, "niuniu": 2}
my_dict = {"niu": 1, "niuniu": 2, "jjj": 3}
my_dict = dict()  # 空字典
# 定义嵌套字典
stu_score_dict = {
    "aaa": {
        "english": 99,
        "math": 88
    },
    "bbb": {
        "english": 100,
        "math": 90
    },
    "ccc": {
        "english": 80,
        "math": 70
    }
}
print(f"{stu_score_dict}")

# 排序
mylist = [1, 0, 2, 4, 3, 5, 6]
print(f"{sorted(mylist)}")
print(f"{sorted(mylist, reverse=True)}")

# 二维列表（嵌套列表）排序
my_list = [["a", 33], ["b", 55], ["c", 11]]
# 定义排序方法
def choose_sort_key(elem):
    return elem[1]
my_list.sort(key=choose_sort_key, reverse=True)  # 大到小

# 因为字典无序，需要先格局关键字排序，然后遍历排好的关键字key从字典里找
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
