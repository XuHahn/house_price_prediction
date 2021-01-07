import numpy as np

from conf import *
from house_utils import *

house_type_list = []

# 得到房屋
for i in HOUSE_TYPE_LIST:
    house_type_list.append(select_by_name(i))

# 朝向热力图
house_type_mean_price_arr = []
house_type_median_price_arr = []
house_type_num = []
for house_type_data in house_type_list:
    price_lst = []
    house_type_num.append(len(house_type_data))
    for price in house_type_data:
        price_lst.append(float(price[5][:-1]))
    house_type_mean_price_arr.append(np.mean(price_lst).round(2))
    house_type_median_price_arr.append(np.median(price_lst).round(2))

house_type_mean_price_arr = np.array(house_type_mean_price_arr)
house_type_num = np.array(house_type_num)

arg_sort = np.argsort(house_type_num)

house_type_num = house_type_num[arg_sort]
house_type_x_axis = np.array(HOUSE_TYPE_LIST)[arg_sort]
house_type_median_price_arr = np.array(house_type_median_price_arr)[arg_sort]
house_type_mean_price_arr = house_type_mean_price_arr[arg_sort]
