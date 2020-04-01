from pyecharts.charts import Gauge,Grid,Liquid
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

def Liquid_NPS(nps_list):
    item = nps_list[0]
    nps = nps_list[1]
    pos = nps_list[2]
    liquid = (
        Liquid(
            init_opts=opts.InitOpts(
                width='350px',
                height='350px'
            )
        )
        .add(
            series_name=item,
            data=nps,
            center=pos,
            label_opts=opts.LabelOpts(
                font_size=25,
                formatter=JsCode(
                    """function(prama) {
                            return(Math.floor(prama.value*10000) / 100) + '%';
                    }"""
                ),
                position='inside'
            )
        )
    )
    return liquid
    # liquid.render('liquid.html')


def BG():
    gauge =Gauge(
            init_opts=opts.InitOpts(
                bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"},
                width='1200px',
                height='900px'
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

def GatherAll():
    liquid1 = Liquid_NPS(['项目1',[0.2533],["20%","33%"]])
    liquid2 = Liquid_NPS(['项目2',[0.2633],["40%","33%"]])
    liquid3 = Liquid_NPS(['项目2', [0.2733], ["60%", "33%"]])
    bg = BG()
    grid = Grid(
        init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"},
            width='1200px',
            height='900px'
        )
    )
    grid.add(bg,grid_opts=opts.GridOpts())
    grid.add(liquid1, grid_opts=opts.GridOpts())
    grid.add(liquid2, grid_opts=opts.GridOpts())
    grid.add(liquid3, grid_opts=opts.GridOpts())
    grid.add_js_funcs("var img = new Image(); img.src = 'https://s1.ax1x.com/2020/03/27/GPWPKI.jpg';")
    grid.render('test_nps.html')

# Liquid_NPS()
GatherAll()
