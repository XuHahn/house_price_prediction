from house_utils import *
from conf import *
import csv

x = []
y = []
for i in DATA_LIST[1:]:
    x.append([float(i[3][:-4]),  # 面积均价
              float(i[6][:-1]),  # 面积
              HOUSE_TYPE_DICT[i[7]],  # 户型
              ORIENTATION_DICT[i[8]],  # 朝向
              convert_traffic_to_digital(i[9]),  # 交通配套
              CITY_DICT[i[10]]])  # 城市
    y.append(float(i[5][:-1]))


# with open('digital.csv','w',encoding='utf-8',newline='') as f:
#     writer = csv.writer(f)
#     for i in range(len(x)):
#         writer.writerow([x[i],y[i]])
