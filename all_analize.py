import pyecharts
from pyecharts import globals
from pyecharts import options as opts
from house_type import *
from orientation_data import *
from region_data import *
from regional_data import *

print('-------------------------------------------------------------------------')
print('- Begin draw Pictures')
np.set_printoptions(precision=2)


# --------------------------------------------------------------------------------------------
def gd_hist():
    value_bar = pyecharts.charts.Bar()
    value_bar.add_xaxis(conf.CITY_LIST)
    value_bar.add_yaxis('平均价格', [np.mean(zhongshan_price_lst).round(2),
                                 np.mean(zhuhai_price_lst).round(2),
                                 np.mean(dongguan_price_lst).round(2),
                                 np.mean(huizhou_price_lst).round(2),
                                 np.mean(zhaoqing_price_lst).round(2),
                                 np.mean(shenzhen_price_lst).round(2),
                                 np.mean(foshan_price_lst).round(2),
                                 np.mean(jiangmen_price_lst).round(2),
                                 np.mean(guangzhou_price_lst).round(2)],
                        markline_opts=opts.MarkLineOpts(
                            data=[opts.MarkLineItem(name='Average house price', type_='average')]),
                        markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem('max', type_='max'), opts.MarkPointItem('min', type_='min')])
                        )
    value_bar.add_yaxis('中位数', [
        np.median(zhongshan_price_lst).round(2),
        np.median(zhuhai_price_lst).round(2),
        np.median(dongguan_price_lst).round(2),
        np.median(huizhou_price_lst).round(2),
        np.median(zhaoqing_price_lst).round(2),
        np.median(shenzhen_price_lst).round(2),
        np.median(foshan_price_lst).round(2),
        np.median(jiangmen_price_lst).round(2),
        np.median(guangzhou_price_lst).round(2)],
                        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem('平均中位数', type_='average')]),
                        markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem('最大中位数', type_='max'), opts.MarkPointItem('最小中位数', type_='min')]),
                        )
    value_bar.add_yaxis('标准差', [
        np.sqrt(np.var(zhongshan_price_lst)).round(5),
        np.sqrt(np.var(zhuhai_price_lst)).round(5),
        np.sqrt(np.var(dongguan_price_lst)).round(5),
        np.sqrt(np.var(huizhou_price_lst)).round(5),
        np.sqrt(np.var(zhaoqing_price_lst)).round(5),
        np.sqrt(np.var(shenzhen_price_lst)).round(5),
        np.sqrt(np.var(foshan_price_lst)).round(5),
        np.sqrt(np.var(jiangmen_price_lst)).round(5),
        np.sqrt(np.var(guangzhou_price_lst)).round(5)],
                        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem('平均方差', type_='average')]),
                        markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem('最大方差', type_='max'), opts.MarkPointItem('最小方差', type_='min')]))
    value_bar.add_yaxis('平均面积', [
        np.mean(zhongshan_ave_m_lst).round(2),
        np.mean(zhuhai_ave_m_lst).round(2),
        np.mean(dongguan_ave_m_lst).round(2),
        np.mean(huizhou_ave_m_lst).round(2),
        np.mean(zhaoqing_ave_m_lst).round(2),
        np.mean(shenzhen_ave_m_lst).round(2),
        np.mean(foshan_ave_m_lst).round(2),
        np.mean(jiangmen_ave_m_lst).round(2),
        np.mean(guangzhou_ave_m_lst).round(2),
    ],
                        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem('平均面积', type_='average')]),
                        markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem('最大平均面积', type_='max'),
                                  opts.MarkPointItem('最小平均面积', type_='min')]))
    value_bar.add_yaxis('每平方米平均价格', [
        np.mean(zhongshan_ave_m_price_lst).round(2),
        np.mean(zhuhai_ave_m_price_lst).round(2),
        np.mean(dongguan_ave_m_price_lst).round(2),
        np.mean(huizhou_ave_m_price_lst).round(2),
        np.mean(zhaoqing_ave_m_price_lst).round(2),
        np.mean(shenzhen_ave_m_price_lst).round(2),
        np.mean(foshan_ave_m_price_lst).round(2),
        np.mean(jiangmen_ave_m_price_lst).round(2),
        np.mean(guangzhou_ave_m_price_lst).round(2),
    ],
                        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem('平均每平米房价', type_='average')]),
                        markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem('最大平米均价', type_='max'), opts.MarkPointItem('最小平米均价', type_='min')])
                        )
    return value_bar


# value_bar.render('all/all_analyze_hist.html')
print('- Figure value_bar has been completed!')


# --------------------------------------------------------------------------------------------
def box_fun():
    box_plot = pyecharts.charts.Boxplot()
    box_plot.add_xaxis(conf.CITY_LIST)
    box_plot.add_yaxis('箱型图', box_plot.prepare_data(
        [list(map(lambda x: float(x), list(zhongshan_price_lst))),
         list(map(lambda x: float(x), list(zhuhai_price_lst))),
         list(map(lambda x: float(x), list(dongguan_price_lst))),
         list(map(lambda x: float(x), list(huizhou_price_lst))),
         list(map(lambda x: float(x), list(zhaoqing_price_lst))),
         list(map(lambda x: float(x), list(shenzhen_price_lst))),
         list(map(lambda x: float(x), list(foshan_price_lst))),
         list(map(lambda x: float(x), list(jiangmen_price_lst))),
         list(map(lambda x: float(x), list(guangzhou_price_lst)))
         ]))
    box_plot.set_global_opts(title_opts=opts.TitleOpts(title="各城市房价箱型图"))
    return box_plot


# box_plot.render('all/box_plot.html')
print('- Figure box_plot has been completed!')


# --------------------------------------------------------------------------------------------
def gd_num_pie_fun():
    gd_num_pie = pyecharts.charts.Pie()
    gd_num_pie.add('各市级小区数量', [['中山市', len(zhongshan)],
                               ['珠海市', len(zhuhai)],
                               ['东莞市', len(dongguan)],
                               ['惠州市', len(huizhou)],
                               ['肇庆市', len(zhaoqing)],
                               ['深圳市', len(shenzhen)],
                               ['佛山市', len(foshan)],
                               ['江门市', len(jiangmen)],
                               ['广州市', len(guangzhou)]])
    return gd_num_pie


# .render('all/广东小区数量.html')

print('- Figure gd_num_pie has been completed!')


# --------------------------------------------------------------------------------------------
def orientation_num_fun():
    orientation_num_pie = pyecharts.charts.Pie()
    # ['东北', '东南', '南北', '朝南', '朝北', '朝向暂无', '朝西', '朝东', '西北', '西南']
    orientation_num_pie.add('各朝向房源数量', [[i, j] for i, j in zip(ORIENTATION_LIST, orientation_num_lst)])
    orientation_num_pie.render('all/广东房源朝向数量.html')
    return orientation_num_pie


print('- Figure orientation_num_pie has been completed!')


# --------------------------------------------------------------------------------------------
def orientation_bar_fun():
    orientation_bar = pyecharts.charts.Bar()
    orientation_bar.add_xaxis(ORIENTATION_LIST)
    # ['东北', '东南', '南北', '朝南', '朝北', '朝向暂无', '朝西', '朝东', '西北', '西南']
    orientation_bar.add_yaxis('该朝向平均价格(万/套)', [
        np.mean(northeast_price_lst).round(2),
        np.mean(southeast_price_lst).round(2),
        np.mean(southnorth_price_lst).round(2),
        np.mean(south_price_lst).round(2),
        np.mean(north_price_lst).round(2),
        np.mean(none_orientation_price_lst).round(2),
        np.mean(west_price_lst).round(2),
        np.mean(east_price_lst).round(2),
        np.mean(northwest_price_lst).round(2),
        np.mean(southwest_price_lst).round(2),
    ], markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem('平均价格', type_='average')]),
                              markpoint_opts=opts.MarkPointOpts(
                                  data=[opts.MarkPointItem('最大均价', type_='max'),
                                        opts.MarkPointItem('最小均价', type_='min')]))

    orientation_bar.add_yaxis('该朝向价格中位数(万/套)', [
        np.median(northeast_price_lst).round(2),
        np.median(southeast_price_lst).round(2),
        np.median(southnorth_price_lst).round(2),
        np.median(south_price_lst).round(2),
        np.median(north_price_lst).round(2),
        np.median(none_orientation_price_lst).round(2),
        np.median(west_price_lst).round(2),
        np.median(east_price_lst).round(2),
        np.median(northwest_price_lst).round(2),
        np.median(southwest_price_lst).round(2),
    ],
                              markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem('平均中位数', type_='average')]),
                              markpoint_opts=opts.MarkPointOpts(
                                  data=[opts.MarkPointItem('最大中位数', type_='max'),
                                        opts.MarkPointItem('最小中位数', type_='min')]))
    return orientation_bar


# .render('all/orientation_hist.html')

print('- Figure orientation_bar has been completed!')


# --------------------------------------------------------------------------------------------
def region_ava_effect_scatter_fun():
    region_ava_effect_scatter_map = pyecharts.charts.Geo(init_opts=opts.InitOpts('1200px', '1500px'))
    region_ava_effect_scatter_map.add_schema('广东')
    region_ava_effect_scatter_map.add_coordinate('大涌镇', 113.306477, 22.469488)
    region_ava_effect_scatter_map.add_coordinate('中堂镇', 113.663426, 23.098861)
    region_ava_effect_scatter_map.add_coordinate('仲恺区', 113.295537, 23.10926)
    region_ava_effect_scatter_map.add_coordinate('三角镇', 113.424647, 22.682987)
    region_ava_effect_scatter_map.add_coordinate('阜沙镇', 113.355928, 22.673398)
    region_ava_effect_scatter_map.add_coordinate('南头镇', 113.298263, 22.723871)
    region_ava_effect_scatter_map.add_coordinate('黄圃镇', 113.345688, 22.717214)
    region_ava_effect_scatter_map.add_coordinate('五桂山镇', 113.473008, 22.422351)
    region_ava_effect_scatter_map.add_coordinate('茶山镇', 113.876358, 23.083319)
    region_ava_effect_scatter_map.add_coordinate('东凤镇', 113.263852, 22.708441)
    region_ava_effect_scatter_map.add_coordinate('板芙镇', 113.328551, 22.422136)
    region_ava_effect_scatter_map.add_coordinate('横栏镇', 113.256519, 22.541325)
    region_ava_effect_scatter_map.add_coordinate('民众镇', 113.500514, 22.628181)
    region_ava_effect_scatter_map.add_coordinate('石碣镇', 113.819675, 23.105471)
    region_ava_effect_scatter_map.add_coordinate('小榄镇', 113.257409, 22.678125)
    region_ava_effect_scatter_map.add_coordinate('古镇镇', 113.19739, 22.619296)
    region_ava_effect_scatter_map.add_coordinate('坦洲镇', 113.474447, 22.260279)
    region_ava_effect_scatter_map.add_coordinate('神湾镇', 113.369887, 22.308331)
    region_ava_effect_scatter_map.add_coordinate('大亚湾区', 114.513204, 22.747707)
    region_ava_effect_scatter_map.add_coordinate('樟木头镇', 114.089719, 22.92077)
    region_ava_effect_scatter_map.add_coordinate('常平镇', 113.998921, 22.981577)
    region_ava_effect_scatter_map.add_coordinate('开发区（含凯茵）', 113.470062, 22.502275)
    region_ava_effect_scatter_map.add_coordinate('厚街镇', 113.677087, 22.942053)
    region_ava_effect_scatter_map.add_coordinate('寮步镇', 113.881138, 23.003735)
    region_ava_effect_scatter_map.add_coordinate('禅城', 113.091382, 23.011382)
    region_ava_effect_scatter_map.add_coordinate('虎门镇', 113.678872, 22.820851)
    region_ava_effect_scatter_map.add_coordinate('横琴新区', 113.554757, 22.119694)
    region_ava_effect_scatter_map.add_coordinate('大岭山镇', 113.849049, 22.906067)
    region_ava_effect_scatter_map.add_coordinate('南沙', 113.531406, 22.808019)
    region_ava_effect_scatter_map.add_coordinate('坪山', 114.353907, 22.69667)
    region_ava_effect_scatter_map.add_coordinate('塘厦镇', 114.079051, 22.81293)
    region_ava_effect_scatter_map.add_coordinate('光明', 113.91502, 22.791931)
    region_ava_effect_scatter_map.add_coordinate('龙华', 114.033739, 22.655811)
    region_ava_effect_scatter_map.add_coordinate('港口镇', 113.392468, 22.591267)
    region_ava_effect_scatter_map.add_coordinate('白云', 113.306382, 23.191426)
    region_ava_effect_scatter_map.add_coordinate('清溪镇', 114.171051, 22.850317)
    region_ava_effect_scatter_map.add_coordinate('松山湖', 113.893865, 22.941246)
    region_ava_effect_scatter_map.add_coordinate('高新区', 113.892648, 22.928377)
    region_ava_effect_scatter_map.add_coordinate('万江区', 113.74855, 23.051032)
    region_ava_effect_scatter_map.add_coordinate('蓬江区', 113.085432, 22.6011)
    region_ava_effect_scatter_map.add_coordinate('江海区', 113.117597, 22.566975)
    region_ava_effect_scatter_map.add_coordinate('大旺区', 113.061397, 22.198361)
    region_ava_effect_scatter_map.add_coordinate('石岐区', 113.391363, 22.538282)
    region_ava_effect_scatter_map.add_coordinate('长安镇', 113.808855, 22.821128)
    region_ava_effect_scatter_map.add_coordinate('石龙镇', 113.880838, 23.112166)
    region_ava_effect_scatter_map.add_coordinate('南城区', 113.745342, 23.00623)
    region_ava_effect_scatter_map.add_coordinate('南区', 113.333328, 22.45838)
    region_ava_effect_scatter_map.add_coordinate('东区', 113.409764, 22.52797)
    region_ava_effect_scatter_map.add_coordinate('西区', 113.214428, 22.685344)
    region_ava_effect_scatter_map.add_coordinate('东城区', 113.784069, 23.03539)
    region_ava_effect_scatter_map.add_coordinate('道滘镇',113.68167,23.010235)
    region_ava_effect_scatter_map.add_coordinate('洪梅镇',113.68167,23.010235)
    region_ava_effect_scatter_map.add('各市级小区数量',
                                      [[i, int(j)] for i, j in zip(region_name_arr, region_ave_price_arr)],
                                      type_=globals.GeoType.EFFECT_SCATTER)
    region_ava_effect_scatter_map.set_global_opts(
        title_opts=opts.TitleOpts(title="广东省地图"),
        visualmap_opts=opts.VisualMapOpts(max_=1000, min_=int(region_ave_price_arr.min())))
    return region_ava_effect_scatter_map


# region_ava_effect_scatter_map.render('all\\region_ava_effect_scatter.html')
print('- Figure region_ava_effect_scatter_map has been completed!')


# --------------------------------------------------------------------------------------------
def region_hot_map_fun():
    region_hot_map = pyecharts.charts.Geo(init_opts=opts.InitOpts('1200px', '1500px'))
    region_hot_map.add_schema('广东')
    region_hot_map.add_coordinate('大涌镇', 113.306477, 22.469488)
    region_hot_map.add_coordinate('中堂镇', 113.663426, 23.098861)
    region_hot_map.add_coordinate('仲恺区', 113.295537, 23.10926)
    region_hot_map.add_coordinate('三角镇', 113.424647, 22.682987)
    region_hot_map.add_coordinate('阜沙镇', 113.355928, 22.673398)
    region_hot_map.add_coordinate('南头镇', 113.298263, 22.723871)
    region_hot_map.add_coordinate('黄圃镇', 113.345688, 22.717214)
    region_hot_map.add_coordinate('五桂山镇', 113.473008, 22.422351)
    region_hot_map.add_coordinate('茶山镇', 113.876358, 23.083319)
    region_hot_map.add_coordinate('东凤镇', 113.263852, 22.708441)
    region_hot_map.add_coordinate('板芙镇', 113.328551, 22.422136)
    region_hot_map.add_coordinate('横栏镇', 113.256519, 22.541325)
    region_hot_map.add_coordinate('民众镇', 113.500514, 22.628181)
    region_hot_map.add_coordinate('石碣镇', 113.819675, 23.105471)
    region_hot_map.add_coordinate('小榄镇', 113.257409, 22.678125)
    region_hot_map.add_coordinate('古镇镇', 113.19739, 22.619296)
    region_hot_map.add_coordinate('坦洲镇', 113.474447, 22.260279)
    region_hot_map.add_coordinate('神湾镇', 113.369887, 22.308331)
    region_hot_map.add_coordinate('大亚湾区', 114.513204, 22.747707)
    region_hot_map.add_coordinate('樟木头镇', 114.089719, 22.92077)
    region_hot_map.add_coordinate('常平镇', 113.998921, 22.981577)
    region_hot_map.add_coordinate('开发区（含凯茵）', 113.470062, 22.502275)
    region_hot_map.add_coordinate('厚街镇', 113.677087, 22.942053)
    region_hot_map.add_coordinate('寮步镇', 113.881138, 23.003735)
    region_hot_map.add_coordinate('禅城', 113.091382, 23.011382)
    region_hot_map.add_coordinate('虎门镇', 113.678872, 22.820851)
    region_hot_map.add_coordinate('横琴新区', 113.554757, 22.119694)
    region_hot_map.add_coordinate('大岭山镇', 113.849049, 22.906067)
    region_hot_map.add_coordinate('南沙', 113.531406, 22.808019)
    region_hot_map.add_coordinate('坪山', 114.353907, 22.69667)
    region_hot_map.add_coordinate('塘厦镇', 114.079051, 22.81293)
    region_hot_map.add_coordinate('光明', 113.91502, 22.791931)
    region_hot_map.add_coordinate('龙华', 114.033739, 22.655811)
    region_hot_map.add_coordinate('港口镇', 113.392468, 22.591267)
    region_hot_map.add_coordinate('白云', 113.306382, 23.191426)
    region_hot_map.add_coordinate('清溪镇', 114.171051, 22.850317)
    region_hot_map.add_coordinate('松山湖', 113.893865, 22.941246)
    region_hot_map.add_coordinate('高新区', 113.892648, 22.928377)
    region_hot_map.add_coordinate('万江区', 113.74855, 23.051032)
    region_hot_map.add_coordinate('蓬江区', 113.085432, 22.6011)
    region_hot_map.add_coordinate('江海区', 113.117597, 22.566975)
    region_hot_map.add_coordinate('大旺区', 113.061397, 22.198361)
    region_hot_map.add_coordinate('石岐区', 113.391363, 22.538282)
    region_hot_map.add_coordinate('长安镇', 113.808855, 22.821128)
    region_hot_map.add_coordinate('石龙镇', 113.880838, 23.112166)
    region_hot_map.add_coordinate('南城区', 113.745342, 23.00623)
    region_hot_map.add_coordinate('南区', 113.333328, 22.45838)
    region_hot_map.add_coordinate('东区', 113.409764, 22.52797)
    region_hot_map.add_coordinate('西区', 113.214428, 22.685344)
    region_hot_map.add_coordinate('东城区', 113.784069, 23.03539)
    region_hot_map.add_coordinate('道滘镇', 113.68167, 23.010235)
    region_hot_map.add_coordinate('洪梅镇', 113.68167, 23.010235)
    region_hot_map.add('各市级小区数量',
                       [[i, int(j)] for i, j in zip(region_name_arr, region_ave_price_arr)],
                       type_=globals.GeoType.HEATMAP)
    region_hot_map.set_global_opts(
        title_opts=opts.TitleOpts(title="广东省地图"), visualmap_opts=opts.VisualMapOpts(max_=1000, min_=0))
    return region_hot_map


# region_hot_map.render('all\\region_hot_map.html')
print('- Figure region_hot_map has been completed!')


# --------------------------------------------------------------------------------------------
def region_hist_fun():
    region_hist = pyecharts.charts.Bar(init_opts=opts.InitOpts(height='6000px'))
    region_hist.add_xaxis(list(region_name_arr))
    region_hist.add_yaxis('各区县平均房价(万/套)', list(region_ave_price_arr), bar_min_width=10, bar_max_width=20,
                          label_opts=opts.LabelOpts(position='right'))
    region_hist.add_yaxis('各区县房价中位数(万/套)', list(region_median_price_arr), bar_min_width=10, bar_max_width=20,
                          label_opts=opts.LabelOpts(position='right'))
    region_hist.add_yaxis('各区县房屋平均面积(平方)', list(region_m_data_arr), bar_min_width=10, bar_max_width=20,
                          label_opts=opts.LabelOpts(position='right'))
    region_hist.add_yaxis('各区县房屋一平方价格(元/平方)', list(region_m_price_arr), bar_min_width=10, bar_max_width=20,
                          label_opts=opts.LabelOpts(position='right'))
    region_hist.reversal_axis()
    # region_hist.render('all\\orientation_analyze.html')
    return region_hist


print('- Figure region_hist has been completed!')
# --------------------------------------------------------------------------------------------
def word_cloud_fun():
    word_cloud = pyecharts.charts.WordCloud()
    word_cloud.add('城市词云', [[i, j] for i, j in zip(list(region_name_arr), list(region_ave_price_arr))])
    word_cloud.render('all\\word_cloud.html')
    return word_cloud
print('- Figure word_cloud has been completed!')
# --------------------------------------------------------------------------------------------
def house_type_bar_fun():
    house_type_bar = pyecharts.charts.Bar(init_opts=opts.InitOpts(height='6000px'))
    house_type_bar.add_xaxis(list(house_type_x_axis))
    house_type_bar.add_yaxis('各户型平均价格', list(house_type_mean_price_arr), bar_min_width=10, bar_max_width=20,
                             label_opts=opts.LabelOpts(position='right'))
    house_type_bar.add_yaxis('各户型价格中位数', list(house_type_median_price_arr), bar_min_width=10, bar_max_width=20,
                             label_opts=opts.LabelOpts(position='right'))
    house_type_bar.reversal_axis()
    house_type_bar.render('all\\house_type_price_bar.html')
    return house_type_bar


print('- Figure house_type_bar has been completed!')


# --------------------------------------------------------------------------------------------
def house_type_nun_pie_fun() -> pyecharts.charts.Pie:
    house_type_num_pie = pyecharts.charts.Pie(init_opts=opts.InitOpts(height='3000px'))
    house_type_num_pie.add('各房型数量', [[i, int(j)] for i, j in zip(list(house_type_x_axis), list(house_type_num))])
    house_type_num_pie.render('all\\house_type_num_pie.html')
    return house_type_num_pie


print('- Figure house_type_num_pie has been completed!')

# --------------------------------------------------------------------------------------------
gd_page = (
    pyecharts.charts.Page()
        .add(
        gd_num_pie_fun(),
        gd_hist(),
        box_fun()
    )
        .render('html\\guangdong.html')
)
print('- Page guangdong_page has been completed!')
# --------------------------------------------------------------------------------------------
orientation_page = (
    pyecharts.charts.Page()
        .add(
        orientation_num_fun(),
        orientation_bar_fun()
    )
        .render('html\\orientation.html')
)
print('- Page orientation_page has been completed!')
# --------------------------------------------------------------------------------------------
map_page = (
    pyecharts.charts.Page()
        .add(
        region_hist_fun(),
        region_ava_effect_scatter_fun(),
        region_hot_map_fun()
    )
        .render('html\\region.html')
)
print('- Page region_page has been completed!')
# --------------------------------------------------------------------------------------------
house_type = (
    pyecharts.charts.Page()
        .add(
        house_type_nun_pie_fun(),
        house_type_bar_fun()
    )
        .render('html/house_type.html')
)
print('- Page house_type has been completed!')
# --------------------------------------------------------------------------------------------
all_page = (
    pyecharts.charts.Page()
        .add(
        gd_num_pie_fun(),
        gd_hist(),
        box_fun(),
        word_cloud_fun(),
        orientation_num_fun(),
        orientation_bar_fun(),
        region_hist_fun(),
        region_ava_effect_scatter_fun(),
        region_hot_map_fun(),
        house_type_nun_pie_fun(),
        house_type_bar_fun()
    )
        .render('html/all_page.html')
)
print('- Page all_page has been completed!')
# --------------------------------------------------------------------------------------------
print('- draw end')
# os.system('all\\all_analyze_hist.html')
# print('1')
# os.system('all\\box_plot.html')
# print('2')
# os.system('all\\广东小区数量.html')
# print('3')
# os.system('all\\广东房源朝向数量.html')
# print('4')
# os.system('all\\orientation_hist.html')
# print('5')
# os.system('all\\orientation_analyze.html')
# print('end')
