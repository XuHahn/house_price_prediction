import numpy as np

from conf import *
from house_utils import *

region_data_lst = []
for i in REGION_LIST:
    region_data_lst.append(select_by_name(i))
region = [r for r in region_data_lst]

region_price_data_lst = []
region_m_price_data_lst = []
region_m_data_lst = []
for i in region:
    price_lst = []
    m_price_lst = []
    m_lst = []
    if (len(i)) == 0:
        price_lst = [0.]
        m_price_lst = [0.]
        m_lst = [0.]
    else:
        for j in i:
            price_lst.append(float(j[5][:-1]))
            m_price_lst.append(float(j[3][:-4]))
            m_lst.append(float(j[6][:-1]))
    region_price_data_lst.append(price_lst)
    region_m_price_data_lst.append(m_price_lst)
    region_m_data_lst.append(m_lst)

region_ave_price_arr = np.array([np.mean(i).round(2) for i in region_price_data_lst])
region_median_price_arr = np.array([np.median(i).round(2) for i in region_price_data_lst])
region_m_price_arr = np.array([np.mean(i).round(2) for i in region_m_price_data_lst])
region_m_data_arr = np.array([np.mean(i).round(2) for i in region_m_data_lst])

arg_sort = np.argsort(region_ave_price_arr)

region_ave_price_arr = region_ave_price_arr[arg_sort]
region_median_price_arr = region_median_price_arr[arg_sort]
region_m_price_arr = region_m_price_arr[arg_sort]
region_m_data_arr = region_m_data_arr[arg_sort]
region_name_arr = np.array(REGION_LIST)[arg_sort]
