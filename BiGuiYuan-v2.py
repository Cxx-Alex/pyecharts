from pyecharts.charts import Bar,Tab,Grid
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from CleanData import CleanData
# import sys
# sys.path.append("D:/Software/pycharm/Projects/pyecharts/test")
# from test_liqud import PageALL

def Satisfaction(CenterName,TabName,Scores_List):
    Items = CenterName
    SubTitle = TabName + "指标得分"
    Scores = Scores_List
    BigTitle = '碧桂园集中式商业消费者满意度研究'
    Color_Com ='rgba(61,109,207,0.6)'
    Color_Min = 'rgba(55,148,140,1)'
    Color_Max ='rgba(212,105,105,1)'
    bar =Bar(
        init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"},
        )
    )
    bar.add_xaxis(xaxis_data=Items)
    for i in range(len(Scores)):
        if(i == 0):
            bar.add_yaxis(
                series_name=Scores[i][0],
                yaxis_data=Scores[i][1:],
                itemstyle_opts=opts.ItemStyleOpts(color=Color_Com),
                label_opts=opts.LabelOpts(position='inside'),
            )
        else:
            bar.add_yaxis(
                is_selected=False,
                series_name=Scores[i][0],
                yaxis_data=Scores[i][1:],
                itemstyle_opts=opts.ItemStyleOpts(color=Color_Com),
                label_opts=opts.LabelOpts(position='inside')
            )
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
            title=BigTitle,
            subtitle=SubTitle,
            pos_right='center',
            title_textstyle_opts=opts.TextStyleOpts(
                color='rgba(0,0,0,0.8)',
                font_size=20
            ),
            subtitle_textstyle_opts=opts.TextStyleOpts(
                color='rgba(0,0,0,0.8)',
                font_size=16
            )
        ),
        legend_opts=opts.LegendOpts(
            orient= 'vertical',
            pos_left='85%',
            pos_top='middle',
            item_width=10,
            item_height=11,
            item_gap=20,
            selected_mode='single'
        )
    )
    bar.set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(name='Average',type_='average')
            ],
            linestyle_opts=opts.LineStyleOpts(color=Color_Max,width=3,type_='dashed')
        ),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(name='Min_Score',type_='min', symbol_size=75,itemstyle_opts=opts.ItemStyleOpts(color=Color_Min)),
                opts.MarkPointItem(name='Max_Score',type_='max', symbol_size=75,itemstyle_opts=opts.ItemStyleOpts(color=Color_Max))
            ]
        )
    )
    bar.add_js_funcs("var img = new Image(); img.src = 'https://s1.ax1x.com/2020/03/27/GPWPKI.jpg';")
    grid = Grid(
        init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"},
            width='1200px',
            height='650px'
        )
    )
    grid.add_js_funcs("var img = new Image(); img.src = 'https://s1.ax1x.com/2020/03/27/GPWPKI.jpg';")
    grid.add(bar,grid_opts=opts.GridOpts(width=850,pos_top='90'))
    return grid

def NPS(CenterName):
    Items = CenterName
    SubTitle = "各项目NPS"
    NPS_Scores = [25.01,26.33,27.21,22.22,21.11,20.03,23.00,24.44,26.36]
    BigTitle = '碧桂园集中式商业消费者满意度研究'
    Color_Com = 'rgba(61,109,207,0.6)'
    Color_Min = 'rgba(55,148,140,1)'
    Color_Max = 'rgba(212,105,105,1)'
    bar = Bar(
        init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"},
        )
    )
    bar.add_xaxis(xaxis_data=Items)
    bar.add_yaxis(
        series_name='NPS',
        yaxis_data=NPS_Scores,
        itemstyle_opts=opts.ItemStyleOpts(color=Color_Com),
        label_opts = opts.LabelOpts(
            position='inside',
            formatter="{c}%"
        )
    )
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
            title=BigTitle,
            subtitle=SubTitle,
            pos_right='center',
            title_textstyle_opts=opts.TextStyleOpts(
                color='rgba(0,0,0,0.8)',
                font_size=20
            ),
            subtitle_textstyle_opts=opts.TextStyleOpts(
                color='rgba(0,0,0,0.8)',
                font_size=16
            )
        ),
        legend_opts=opts.LegendOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}%"))
    )
    bar.set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(name='Average', type_='average')
            ],
            linestyle_opts=opts.LineStyleOpts(color=Color_Max, width=3, type_='dashed'),
            label_opts=opts.LabelOpts(formatter="{c}%")
        ),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(name='Min_Score', type_='min', symbol_size=75, itemstyle_opts=opts.ItemStyleOpts(color=Color_Min)),
                opts.MarkPointItem(name='Max_Score', type_='max', symbol_size=75, itemstyle_opts=opts.ItemStyleOpts(color=Color_Max))
            ],
            label_opts=opts.LabelOpts(formatter="{c}%",font_size=10,position='inside')
        )
    )
    bar.add_js_funcs("var img = new Image(); img.src = 'https://s1.ax1x.com/2020/03/27/GPWPKI.jpg';")
    grid = Grid(
        init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"},
            width='1200px',
            height='650px'
        )
    )
    grid.add_js_funcs("var img = new Image(); img.src = 'https://s1.ax1x.com/2020/03/27/GPWPKI.jpg';")
    grid.add(bar, grid_opts=opts.GridOpts(width=850, pos_top='90'))
    return grid

def Gather():
    tab = Tab(page_title='碧桂园集中式商业消费者满意度研究')
    CenterName,Data_Dict = CleanData()
    TabNames = list(Data_Dict.keys())
    for TabName in TabNames:
        Scores_List = Data_Dict[TabName]
        tab.add(Satisfaction(CenterName,TabName,Scores_List), TabName)
    tab.add(NPS(CenterName),'NPS')
    tab.render('满意度得分展示Demo.html')

Gather()