import pandas as pd
# web界面可视化 pyecharts
from pandas import options
from pyecharts.charts import Bar
from pyecharts.charts import Line
import DBHeple
import os

db = DBHeple.MyDBmySQL()
# 1.股票涨跌趋势图 折现图

# 2.股票交易额 柱状图
df = pd.read_sql("SELECT name, amount from tb_xueqiu ORDER BY amount desc limit 20", con=db.conn)
x = df['name'].values.tolist()
y = df['amount'].values.tolist()
c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("成交额的数据", y)
    .set_global_opts(
        title_opts=options.TitleOpts(title="股票交易额图表"),
        #     设置一个放大镜
        datazoom_opts=options.DataZoomOpts()
    )
)
c.render('股票交易额图表.html')
os.system('股票交易额图表.html')
