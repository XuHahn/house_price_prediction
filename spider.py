from selenium import webdriver
from lxml import etree
import requests
import time
import csv

# 使用selenium模拟网页打开，不使用点击下一页按钮。为了爬取效率直接跳到下一页
# 创建csv
file = open('original_data.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(('楼盘名称', '区域', '单价', '本小区均价', '新区片均价', '总价', '面积', '房源编号', '户型', '朝向', '核心卖点', '户型简介', '交通配套', '城市'))  # 写入列标题


def get_info(links):
    for link in links:
        link = 'https://' + city + '.leyoujia.com' + link
        rq = requests.get(link, headers=headers)  # 对网页进行请求
        rq.content.decode(encoding='utf-8')  # 对文本进行解码
        link_dom = etree.HTML(rq.text, etree.HTMLParser(encoding="utf-8"))
        try:
            # 楼盘名称
            name = link_dom.xpath('//*[@class="fl xqname"]/a/text()')[0]
            # 区域
            region = link_dom.xpath('//*[@class="location fl mr10"]/a[1]/text()')[0]
            # 单价
            price = link_dom.xpath('//*[@style="padding-top:8px;"]/em/text()')[0]
            try:
                # 本小区均价
                bmean = link_dom.xpath('//*[@class="trend-vs clearfix"]/div[2]/span[2]/em/text()')[0]
            except:
                bmean = '空'
            try:
                # 新区均价
                xmean = link_dom.xpath('//*[@class="vs-item vs-item3"]/span[2]/em/text()')[0]
            except:
                xmean = '空'
            # 总价
            total = link_dom.xpath('//*[@class="price fl cred"]/em/text()')[0]
            # 面积
            area = link_dom.xpath('//*[@class="intro-box2 clearfix"]/span[2]/text()')[0]
            try:
                # 房源编号
                num = link_dom.xpath('//*[@class="intro-box3 clearfix"]/p[5]/span[2]/text()')[0]
            except:
                num = '空'
            # 户型
            type = link_dom.xpath('//*[@style="text-align: left;"]/text()')[0].strip()
            # 朝向
            orientations = link_dom.xpath('//*[@style="margin-right: 0;"]/text()')[0].strip()
            try:
                # 核心卖点
                bright_points = link_dom.xpath('//*[@class="comm-box fy-intro"]/div[3]/div/text()')[0].strip()
            except:
                bright_points = '空'
            try:
                # 户型简介
                introduction = link_dom.xpath('//*[@class="comm-box fy-intro"]/div[5]/div/text()')[0].strip()
            except:
                introduction = '空'
            try:
                # 交通配套
                traffic = link_dom.xpath('//*[@class="comm-box fy-intro"]/div[6]/div/p/span/text()')[0].strip()  # 交通配套
            except:
                traffic = '空'
            writer.writerow((name, region, price + '元/平米', bmean + '元/平米', xmean + '元/平米', total + '万',
                             area, num, type, orientations, bright_points, introduction, traffic, c))  # 将数据写入到csv文件中
            data = {
                '楼盘名称': name,
                '区域': region,
                '单价': price + '元/平米',
                '本小区均价': bmean + '元/平米',
                '新区片均价': xmean + '元/平米',
                '总价': total + '万',
                '面积': area,
                '房源编号': num,
                '户型': type,
                '朝向': orientations,
                '核心卖点': bright_points,
                '户型简介': introduction,
                '交通配套': traffic,
                '城市': c
            }
            print(data)
        except:
            pass

# 深圳29641，广州 23455，zh 4000,
if __name__ == '__main__':
    cities = ['shenzhen', 'guangzhou', 'zhuhai', 'foshan', 'dongguan', 'huizhou', 'zhaoqing', 'zhongshan', 'jiangmen']
    chengshi = ['深圳', '广州', '珠海', '佛山', '东莞', '惠州', '肇庆', '中山', '江门']
    for city, c in zip(cities, chengshi):
        urls = ['https://' + city + '.leyoujia.com/esf/?n={}'.format(number) for number in range(1, 500)]  # 页数设置
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; '
                                 'Intel Mac OS X 10_14_0) AppleWebKit/'
                                 '537.36 (KHTML, like Gecko) Chrome'
                                 '/85.0.4183.102 Safari/537.36'}
        driver = webdriver.Chrome()
        pg = 1
        for url in urls:
            driver.get(url)
            driver.implicitly_wait(10)  # 隐式等待10秒，让请求的网页全部渲染完
            dom = etree.HTML(driver.page_source, etree.HTMLParser(encoding="utf-8"))
            links = dom.xpath('//*[@class="list-box"]/ul/li/div[2]/p[1]/a/@href')  # 详细页链接
            get_info(links)
            print('第' + str(pg) + '页爬取完毕！  城市：' + c)
            time.sleep(10)
            pg = pg + 1
        driver.close()  # 关闭弹窗

