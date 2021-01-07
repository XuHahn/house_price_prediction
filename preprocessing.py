import csv

import pandas as pd

df = pd.read_csv('data/original_data_3.csv')
df2 = pd.read_csv('data/original_data.csv')
df3 = pd.read_csv('data/original_data_2.csv')
alL_csv = pd.concat([df, df2, df3])
print('---------------------------')
print(f'- Total: {alL_csv.shape[0]} rows,{alL_csv.shape[1]} columns before refine')
alL_csv = alL_csv.drop_duplicates(
    subset=['楼盘名称', '区域', '单价', '本小区均价', '新区片均价', '总价', '面积', '房源编号', '户型', '朝向', '核心卖点', '户型简介', '交通配套', '城市'],
    keep='first')
alL_csv.to_csv('house_data.csv', index=False)
print('- Begin refine data')
with open('house_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    useful_data = []
    for i in reader:
        useful_data.append(i[:7] + i[8:10] + i[12:])
    with open('house_data.csv', 'w', encoding='utf-8',newline='') as w:
        writer = csv.writer(w)
        writer.writerows(useful_data)
        print('- File is created')
        print(f'- Total: {alL_csv.shape[0]} rows,{alL_csv.shape[1]} columns after refine')

# refine_data()
