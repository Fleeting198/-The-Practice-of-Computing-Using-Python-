# -*- coding:utf-8 -*-
# !/usr/bin/python
import pandas as pd
from prettytable import PrettyTable


def getDataList(file_name):
    """从csv中读取数据"""
    dataList = pd.read_csv(file_name, parse_dates=['Date'])
    dataList = dataList[['Date', 'Volume', 'Adj Close']]  # 保留需要的字段
    dataList.columns = [['Date', 'Volume', 'AdjClose']]  # 为了pandas处理方便起见去掉key中的空格

    return dataList


def getMonthlyAverages(data_list):
    """计算每月平均值，返回元组列表"""
    lMonthlyAvg = []
    dict_tmp = {}

    for line in data_list.itertuples():
        monthDate = str(line[1])[:7]
        if monthDate not in dict_tmp:
            dict_tmp[monthDate] = [line[2] * line[3], line[2]]
        else:
            dict_tmp[monthDate][0] += line[2] * line[3]
            dict_tmp[monthDate][1] += line[2]

    # 以日期为第一列，值为第二列，组装成元组形式返回
    for k, v in dict_tmp.items():
        lMonthlyAvg.append((k, round(v[0] / v[1], 2)))

    return lMonthlyAvg


def printInfo(monthlyAveragesList):
    # 按照平均值降序排序
    lMonthlyAvg = sorted(monthlyAveragesList, key=lambda x: x[1], reverse=True)

    # 使用PrettyTable 输出美观的控制台表格
    table = PrettyTable()
    table.field_names = ['date', 'average']
    if len(lMonthlyAvg) > 6:
        print('最高六个：')
        for data in lMonthlyAvg[:6]:
            table.add_row(data)
        print(table)
        table.clear_rows()

        print('最低六个：')
        for data in lMonthlyAvg[-1:-7:-1]:
            table.add_row(data)
        print(table)
        table.clear_rows()

    else:
        for data in lMonthlyAvg:
            table.add_row(data)
        print(table)


if __name__ == '__main__':
    printInfo(getMonthlyAverages(getDataList('table.csv')))
