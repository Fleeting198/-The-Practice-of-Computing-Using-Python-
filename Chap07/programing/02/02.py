# -*- coding:utf-8 -*-
# !/usr/bin/python
"""谁是NBA最佳球员"""

import pandas as pd
import sys
from prettytable import PrettyTable


def getDataList(file_name):
    """从csv中读取数据"""
    try:
        dataList = pd.read_csv(sys.path[0] + '/' + file_name)
        return dataList
    except OSError:
        print('没有在.py文件的同文件夹内找到' + file_name + '，代码退出。')
        exit()


def calEfficiency(dataList):
    """计算效率值，写回dataList 中并返回"""
    dataList['efficiency'] = ((dataList['pts'] + dataList['reb'] + dataList['asts'] + dataList['stl'] + dataList[
        'blk']) - ((dataList['fga'] - dataList['fgm']) + (dataList['fta'] - dataList['ftm']) + dataList['turnover'])) / \
                             dataList['gp']
    return dataList


def rankList(dataList, by, length=50):
    """按照某列名排序，返回前数行，默认50行"""
    dataList.sort_values(by=by, ascending=False, inplace=True)
    dataList = dataList[[by, 'firstname', 'lastname', 'year', 'team']]
    return dataList[:length]


def prettyTableFromDF(DF):
    """将DataFrame 写入prettytable 并返回，在这里去掉了第一列序号，所以没有通用性"""
    table = PrettyTable()
    table.field_names = list(pd.DataFrame(DF).columns)
    for line in pd.DataFrame(DF).itertuples():
        table.add_row(list(line)[1:])

    table.align = 'l'
    return table


if __name__ == '__main__':
    dataList = calEfficiency(getDataList('player_regular_season.csv'))
    tmp_dataList = rankList(dataList, 'efficiency')
    print(prettyTableFromDF(tmp_dataList))
    # 因所使用数据区分年份和队伍，所以会出现同一人有多行记录的情况
