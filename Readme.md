# 广州周边地区二手房价数据分析

#### 介绍
就图一乐的房屋放假预测分析（基于广州周边地区）

#### 软件架构
######1、项目结构
>house_prece
>> all -> 所有可视化出来的html文件
> 
>> data -> 爬取的原始数据都在这
> 
>> html -> 分类总结后的可视化的html文件
> 
>> all_analize.py -> 所有可视化过程都在这
> 
>> conf -> 配置项
> 
>> gui.py -> 这个东西直接无视掉，原来想写个gui界面方便预测分析，然鹅我懒，等一个大佬的提交请求（dddd）
> 
>> convert_to_digital.py -> 数据映射成数字
>
>> house_type.py / orientation_data.py / regional_data.py / region_data.py / regional_data.py 直译就是放这些东西的数据
>
>> predict.py -> 房价预测在这 
> 
>> house_data.csv / digital.csv 这两个就是数字数据
> 
>> preprocessing.py -> 数据预处理
> 
>> requirements.txt -> 环境依赖
>
>> spider.py -> 爬虫
> 
>> render.html / heatmap_with_label_show.html -> 无视掉

#### 安装教程

~~~Bash
cd house_price
pip install -r requirements.txt
~~~

#### 使用说明

1. ~~~Bash
   python spider.py
   ~~~
2. ~~~Bash
   python preprocessing.py
   ~~~
3. ~~~Bash
   python convert_to_digital.py
   ~~~
4. ~~~Bash
   all_analize.py
   ~~~
#### 参与贡献
    自己的大作业自己瞎写，给大家参考用
#禁止任何商业用途！！！！（虽然我代码很垃圾）

#### 引用
    大家伙要拿去用的话麻烦点个start就好了，不拿去任何商业用途我都允许，如果能标注原作者那就更好了对吧hxd？