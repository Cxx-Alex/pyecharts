from pyecharts.charts import Bar,Grid
from pyecharts import options as opts
from snapshot_selenium import snapshot as dirver
from pyecharts.render import make_snapshot

# xaxis = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# yaxis = [5,20,36,10,75,90]
# bar = (
#     Bar()
#     .add_xaxis(xaxis)
#     .add_yaxis("商家",yaxis)
# )
#
# make_snapshot(dirver, bar.render(),"bar.png")

columns = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

bar = (
    Bar()
    .add_xaxis(xaxis_data = columns)
    .add_yaxis(
        series_name="降水量",
        yaxis_data=data1
    )
    .add_yaxis(
        series_name="蒸发量",
        yaxis_data=data2
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title ="柱状图",subtitle="一年的降水量和蒸发量"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_='average',name='平均值')
            ]
        ),
        markpoint_opts=opts.MarkPointOpts(
            data = [
                opts.MarkPointItem(type_='max',name='最大值'),
                opts.MarkPointItem(type_='mix',name='最小值')
            ]
        )

    )

)
grid = Grid()
grid.add(bar,grid_opts=opts.GridOpts(pos_left=''))

bar.render()


