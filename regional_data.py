import re

import numpy as np

from house_utils import select_by_name
# --------------------------------------------------------------------------------------------
zhongshan = select_by_name('中山')
zhongshan_price_lst = []
zhongshan_ave_m_price_lst = []
zhongshan_ave_m_lst = []
for i in zhongshan:
    zhongshan_price_lst.append(float(i[5][:-1]))
    zhongshan_ave_m_price_lst.append(float(i[3][:-4]))
    zhongshan_ave_m_lst.append(float(i[6][:-1]))
zhongshan_price_lst = np.array(zhongshan_price_lst)
# --------------------------------------------------------------------------------------------

zhuhai = select_by_name('珠海')
zhuhai_price_lst = []
zhuhai_ave_m_price_lst = []
zhuhai_ave_m_lst = []
for i in zhuhai:
    zhuhai_price_lst.append(float(i[5][:-1]))
    zhuhai_ave_m_price_lst.append(float(i[3][:-4]))
    zhuhai_ave_m_lst.append(float(i[6][:-1]))
zhuhai_price_lst = np.array(zhuhai_price_lst)
# --------------------------------------------------------------------------------------------

dongguan = select_by_name('东莞')
dongguan_price_lst = []
dongguan_ave_m_price_lst = []
dongguan_ave_m_lst = []
for i in dongguan:
    dongguan_price_lst.append(float(i[5][:-1]))
    dongguan_ave_m_price_lst.append(float(i[3][:-4]))
    dongguan_ave_m_lst.append(float(i[6][:-1]))
dongguan_price_lst = np.array(dongguan_price_lst)
# --------------------------------------------------------------------------------------------

huizhou = select_by_name('惠州')
huizhou_price_lst = []
huizhou_ave_m_price_lst = []
huizhou_ave_m_lst = []
for i in huizhou:
    huizhou_price_lst.append(float(i[5][:-1]))
    huizhou_ave_m_price_lst.append(float(i[3][:-4]))
    huizhou_ave_m_lst.append(float(i[6][:-1]))
huizhou_price_lst = np.array(huizhou_price_lst)
# --------------------------------------------------------------------------------------------

zhaoqing = select_by_name('肇庆')
zhaoqing_price_lst = []
zhaoqing_ave_m_price_lst = []
zhaoqing_ave_m_lst = []
for i in zhaoqing:
    zhaoqing_price_lst.append(float(i[5][:-1]))
    zhaoqing_ave_m_price_lst.append(float(i[3][:-4]))
    zhaoqing_ave_m_lst.append(float(i[6][:-1]))
zhaoqing_price_lst = np.array(zhaoqing_price_lst)
# --------------------------------------------------------------------------------------------

shenzhen = select_by_name('深圳')
shenzhen_price_lst = []
shenzhen_ave_m_price_lst = []
shenzhen_ave_m_lst = []
for i in shenzhen:
    shenzhen_price_lst.append(float(i[5][:-1]))
    shenzhen_ave_m_price_lst.append(float(i[3][:-4]))
    shenzhen_ave_m_lst.append(float(i[6][:-1]))
shenzhen_price_lst = np.array(shenzhen_price_lst)
# --------------------------------------------------------------------------------------------

foshan = select_by_name('佛山')
foshan_price_lst = []
foshan_ave_m_price_lst = []
foshan_ave_m_lst = []
for i in foshan:
    foshan_price_lst.append(float(i[5][:-1]))
    foshan_ave_m_price_lst.append(float(i[3][:-4]))
    foshan_ave_m_lst.append(float(i[6][:-1]))
foshan_price_lst = np.array(foshan_price_lst)
# --------------------------------------------------------------------------------------------

jiangmen = select_by_name('江门')
jiangmen_price_lst = []
jiangmen_ave_m_price_lst = []
jiangmen_ave_m_lst = []
for i in jiangmen:
    jiangmen_price_lst.append(float(i[5][:-1]))
    jiangmen_ave_m_price_lst.append(float(i[3][:-4]))
    jiangmen_ave_m_lst.append(float(i[6][:-1]))
jiangmen_price_lst = np.array(jiangmen_price_lst)
# --------------------------------------------------------------------------------------------

guangzhou = select_by_name('广州')
guangzhou_price_lst = []
guangzhou_ave_m_price_lst = []
guangzhou_ave_m_lst = []
for i in guangzhou:
    guangzhou_price_lst.append(float(i[5][:-1]))
    guangzhou_ave_m_price_lst.append(float(i[3][:-4]))
    guangzhou_ave_m_lst.append(float(i[6][:-1]))
guangzhou_price_lst = np.array(guangzhou_price_lst)
# --------------------------------------------------------------------------------------------