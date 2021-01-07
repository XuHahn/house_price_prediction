from conf import *
from house_utils import *

orientation_data_lst = []
for orientation in ORIENTATION_LIST:
    orientation_data_lst.append(select_by_name(orientation))

# ['东北', '东南', '南北', '朝南', '朝北', '朝向暂无', '朝西', '朝东', '西北', '西南']
# --------------------------------------------------------------------------------------------
northeast = orientation_data_lst[0]
northeast_price_lst = []
for i in northeast:
    northeast_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
southeast = orientation_data_lst[1]
southeast_price_lst = []
for i in southeast:
    southeast_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
southnorth = orientation_data_lst[2]
southnorth_price_lst = []
for i in southnorth:
    southnorth_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
south = orientation_data_lst[3]
south_price_lst = []
for i in south:
    south_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
north = orientation_data_lst[4]
north_price_lst = []
for i in north:
    north_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
none_orientation = orientation_data_lst[5]
none_orientation_price_lst = []
for i in none_orientation:
    none_orientation_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
west = orientation_data_lst[6]
west_price_lst = []
for i in west:
    west_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
east = orientation_data_lst[7]
east_price_lst = []
for i in east:
    east_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
northwest = orientation_data_lst[8]
northwest_price_lst = []
for i in northwest:
    northwest_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
southwest = orientation_data_lst[9]
southwest_price_lst = []
for i in southwest:
    southwest_price_lst.append(float(i[5][:-1]))
# --------------------------------------------------------------------------------------------
orientation_num_lst = [len(northeast), len(southeast), len(southnorth), len(south), len(north), len(none_orientation),
                       len(west), len(east), len(northwest), len(southwest), ]
