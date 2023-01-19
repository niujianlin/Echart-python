"""
GDP大量数据动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ThemeType
# ---------------------准备、处理数据-------------------
# 读取文件
f = open("C:/partF/programs/test/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()  # list格式
# print(f"{type(data_lines)}")
# print(f"{data_lines}")

# 关闭文件
f.close()
# 删除第一行
data_lines.pop(0)
# 定义一个字典格式化存储这些数据
# {1960:[[美国,123],[中国,321],...], 1961:[[美国,123],[中国,321],...]}
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        # data_dict一开始是空的，data_dict[1960]不存在，若存在，则添加二维的列表
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 打印字典全部数据
# print(data_dict)

# 因为字典无序，年份无序，需要先排序
sorted_year_list = sorted(data_dict.keys())
print(f"{sorted_year_list}")

# ---------------------准备、处理数据完成-------------------

# ------遍历数据并创建动态图表（时间线保存每次遍历新建的图表）-------

# 创建时间线对象，保存下面遍历的每一个柱状图Bar，并添加颜色主题
timeline = Timeline({"theme": ThemeType.LIGHT})

# 遍历创建Bar柱状图
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年分前8的国家
    country_list = data_dict[year][:8]
    x_data = []
    y_data = []
    for country_info in country_list:
        x_data.append(country_info[0])  # x轴添加国家数据
        y_data.append(country_info[1]/100000000)  # y轴添加gdp数据
    # 构建柱状图
    bar = Bar()
    x_data.reverse()  # 翻转x y 的目的是让数据高的显示在上面
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 翻转x y轴
    bar.reversal_axis()
    # 设置每一年图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    # 添加至时间线保存
    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
# 绘图渲染
timeline.render("1960-2019全球GDP前8国家.html")
