# -*- coding: utf-8 -*-
import pandas as pd
import sys
from prettytable import PrettyTable

# ==========导入上证指数的原始数据
# 这里填写数据文件的路径，注意路径的相对性
url_stokeData = "/index data/sh000001.csv"
index_data = pd.read_csv(sys.path[0] + url_stokeData, parse_dates=['date'])
index_data = index_data[['date', 'high', 'low', 'close']]  # 保留需要的字段
index_data.sort_values(by='date', inplace=True)  # 按日期升序排序

# ==========计算海龟交易法则的买卖点
# 设定海龟交易法则的两个参数，当收盘价大于最近N1天的最高价时买入，当收盘价低于最近N2天的最低价时卖出
# 这两个参数可以自行调整大小，但是一般N1 > N2
N1 = 5
N2 = 5

tag_highestN1 = 'highest in ' + str(N1)
tag_lowestN2 = 'lowest in ' + str(N1)

# 通过rolling_max方法计算最近N1个交易日的最高价
index_data[tag_highestN1] = index_data['high'].rolling(window=N1, center=False).max()
# 对于上市不足N1天的数据，取上市至今的最高价
index_data[tag_highestN1].fillna(value=index_data['high'].expanding().max(), inplace=True)

# 通过相似的方法计算最近N2个交易日的最低价
index_data[tag_lowestN2] = index_data['low'].rolling(window=N1, center=False).min()
index_data[tag_lowestN2].fillna(value=index_data['low'].expanding().min(), inplace=True)

# 当天的【close】> 昨天的【最近N1个交易日的最高点】时，将【suggest】设为“买入”
buy_index = index_data[index_data['close'] > index_data[tag_highestN1].shift(1)].index
index_data.loc[buy_index, 'suggest'] = '买入'
# 当天的【close】< 昨天的【最近N2个交易日的最低点】时，将【合适操作】设为“卖出”
sell_index = index_data[index_data['close'] < index_data[tag_lowestN2].shift(1)].index
index_data.loc[sell_index, 'suggest'] = '卖出'

index_data['suggest'].fillna(value='', inplace=True)

# 使用prettytable模块构建控制台显示的表格
# 列名
headers = ['序号', '日期', '最高点', '最低点', '收盘价', '最近' + str(N1) + '天最高点', '最近' + str(N2) + '天最低点', '建议操作']

table = PrettyTable()
table.field_names = headers

# 遍历pandas.dataframe的每一行，转为prettytable的行
for line in index_data.itertuples():
    line = list(line)
    line[1] = str(line[1])[:10]  # 将pandas的日期转为字符串
    table.add_row(line)

table.align = 'l'  # 向左对齐
print(table)

# 将数据保存到本.py文件同目录下
index_data.columns = headers[1:]
index_data.to_csv(sys.path[0] + '/turtle.csv', index=False, encoding='gbk')
