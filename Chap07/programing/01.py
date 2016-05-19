# -*- coding:utf-8 -*-
from datetime import datetime


def getDataList(file_name):
    """ 从csv中读取数据 """
    data_file = open(file_name, 'r')
    data_list = []
    for line in data_file:
        data_list.append(line.strip().split(','))
    return data_list[1:]


def getMonthlyAverages(data_list):
    """ 计算每月平均值，返回元组列表 """
    lMonthlyAvg = []
    dict_tmp = {}
    for dataOneDay in data_list:
        thisDate = datetime.strptime(dataOneDay[0], '%Y-%m-%d')
        monthDate = thisDate.strftime('%Y-%m')
        if monthDate not in dict_tmp:
            dict_tmp[monthDate] = [int(dataOneDay[5]) * float(dataOneDay[6]), float(dataOneDay[6])]
        else:
            dict_tmp[monthDate][0] += int(dataOneDay[5]) * float(dataOneDay[6])
            dict_tmp[monthDate][1] += float(dataOneDay[6])

    for k, v in dict_tmp.items():
        lMonthlyAvg.append((v[0]/v[1], k))

    return lMonthlyAvg


def printInfo(monthlyAveragesList):
    # 按照平均值（元组的0号元素）降序排序
    lMonthlyAvg = sorted(monthlyAveragesList, key=lambda x: x[0], reverse=True)

    if len(lMonthlyAvg) > 6:
        print('最高六个：')
        print('日期\t\t平均值')
        for data in lMonthlyAvg[:6]:
            print (data[1], '\t\t', str(round(data[0], 2)))

        print('最低六个：')
        for data in lMonthlyAvg[-6:]:
            print(data[1], '\t\t', str(round(data[0], 2)))
    else:
        print('日期\t\t平均值')
        for data in lMonthlyAvg:
            print(data[1], '\t\t', str(round(data[0], 2)))


if __name__ == '__main__':
    printInfo(getMonthlyAverages(getDataList('table.csv')))
