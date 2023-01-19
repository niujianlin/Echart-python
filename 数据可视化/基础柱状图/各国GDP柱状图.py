"""
带有时间线的柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 构建柱状图
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # 数据显示在柱状条的右侧
bar1.reversal_axis()  # x y轴翻转

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 50, 50], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 60, 60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 构建时间线，主题设置
timeline = Timeline({"theme": ThemeType.LIGHT})
# 在时间线中添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点1")
timeline.add(bar3, "点1")
# 用时间线绘图，而不是Bar柱状图绘图
timeline.render("基础时间线柱状图.html")
# 设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)