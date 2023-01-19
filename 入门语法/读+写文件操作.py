# 备份正式文件

# 读文件
fr = open("C:/partF/programs/test/数据.txt", "r", encoding="UTF-8")
# 写文件
fw = open("C:/partF/programs/test/数据.txt.bak", "w", encoding="UTF-8")

for line in fr:
    if line.strip().split(",")[4] == "正式":
        fw.write(line)  # 写入备份


fr.close()
fw.close()