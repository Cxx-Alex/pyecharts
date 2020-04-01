from pyecharts.charts import Gauge,Bar,Page
from pyecharts.components import Image
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.options import ComponentTitleOpts

def NPS(NPS_List):
    Item = NPS_List[0]
    nps = NPS_List[1]
    laber = str(NPS_List[1]) + '%'
    gauge =Gauge(
            init_opts=opts.InitOpts(
                width='400px',
                height='300px'
            )
        )
    gauge.add(
        series_name=Item,
        data_pair=[('NPS',nps)],
        min_=-100,
        max_=100,
        split_number=4,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.5, "#37a2da"], [1, "#fd666d"]],
                width=30
            )
        ),
        itemstyle_opts=opts.ItemStyleOpts(
            color='rgba(212,105,105,1)'
        ),
        detail_label_opts=opts.LabelOpts(
            font_size=20,
            position='bottom',
            formatter=laber
        )
    )
    gauge.set_global_opts(
        title_opts=opts.TitleOpts(
            subtitle='NPS-' + Item,
            pos_right='center',
            subtitle_textstyle_opts=opts.TextStyleOpts(
                color='rgba(0,0,0,0.8)',
                font_size=16
            )
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    return gauge

def BG():
    gauge =Gauge(
            init_opts=opts.InitOpts(
                bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"},
                width='1200px',
                height='300px'
            )
        )
    gauge.set_global_opts(
        title_opts=opts.TitleOpts(
            title='碧桂园集中式商业消费者满意度研究',
            pos_left='center',
            title_textstyle_opts=opts.TextStyleOpts(
                color='rgba(0,0,0,0.8)',
                font_size=20
            )
        )
    )
    gauge.add_js_funcs("var img = new Image(); img.src = 'https://s1.ax1x.com/2020/03/27/GPWPKI.jpg';")
    return gauge

def Gather_in_Page():
    Data_List = [['项目2',25.02]]
    bg= BG()
    page = Page(layout=Page.DraggablePageLayout)
    page.add(bg)
    for NPS_List in Data_List:
        gauge = NPS(NPS_List)
        page.add(gauge)
    page.render('NPS.html')

Gather_in_Page()
# NPS1()