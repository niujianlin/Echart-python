"""
对json数据进行处理并显示折线图
可以使用json在线编辑器看JSON结构 https://www.89tool.com/
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 导入文件
f_us = open("C:/partF/programs/test/折线图数据/美国.txt", "r", encoding="UTF-8")
f_jp = open("C:/partF/programs/test/折线图数据/日本.txt", "r", encoding="UTF-8")
f_in = open("C:/partF/programs/test/折线图数据/印度.txt", "r", encoding="UTF-8")

# 获取文本
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

# 删除json以外的数据-头数据
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 删除json以外的数据-尾);
us_data = us_data[:-2]  # 头到倒数第二个（不包含倒数第二个）切片
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# print(f"类型：{type(us_data)}")
# print(f"{us_data}")
# str转字典（键值对）
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# 获取JSON中的确诊数据和对应的日期信息
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]
# 截取314条日期信息作为x轴（有一条其实就行，是公用的x轴）
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
in_x_data = in_trend_data["updateDate"][:314]
# 截取314条确诊数据作为y轴
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]

# 构建图标
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")

)
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()

