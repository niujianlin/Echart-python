"""
pyecharts折线图基础入门
"""

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts


line = Line()
# 折线图x轴
line.add_xaxis(["中国", "美国", "英国"])
# 折线图y轴
line.add_yaxis("GDP", [30, 30, 10])

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"), # 标题
    legend_opts=LegendOpts(is_show=True),   # 图例（默认显示）
    toolbox_opts=ToolboxOpts(is_show=True),  # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True)  # 视觉映射
)


# 通过render()，生成图像
line.render()
