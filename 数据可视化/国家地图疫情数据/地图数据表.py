"""
全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("C:/partF/programs/test/地图数据/疫情.txt", "r", encoding="UTF-8")

data = f.read()
# 关闭文件
f.close()

# json转换成数据字典
data_dict = json.loads(data)
# 从字典中取中国各区的数据
data_province = data_dict["areaTree"][0]["children"]
# 列表记录 各区的区名和确诊人数，给map使用
data_list = []
# 循环取出各区的区名和确诊人数
for province in data_province:
    province_name = province["name"]+"省"
    province_confirm = province["total"]["confirm"]
    data_list.append((province_name, province_confirm))  # 省名和确诊人数作为元组传进去
print(f"{data_list}")

# 构建map对象
map = Map()
map.add("各省确诊人数", data_list, "china")

# 设置地图全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable":"1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+",  "color": "#990033"},

        ]
    )
)

# 绘图渲染
map.render("全国疫情地图.html")
