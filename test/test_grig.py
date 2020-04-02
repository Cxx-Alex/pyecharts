from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

fn = """
    function
    """

def NPS_Pie():
    pie = Pie()
    pie.add(
        series_name='项目1',
        data_pair=[list(z) for z in zip(['推荐者','中立者','贬损者'],[55.11,20.54,24.45])],
        center=['15%','20%'],
        radius=[50,70],
        rosetype='radius',
    )