# -*- coding:utf-8 -*-
# !/usr/bin/python
"""  电子表格 """
import csv
import sys


def getDataFromFile(fileName):
    """ 读取csv文件 """
    data = []
    try:
        with open(sys.path[0] + '/' + fileName, 'r') as dataFile:
            csvReader = csv.reader(dataFile)
            for line in csvReader:
                data.append(line)
    except FileNotFoundError:
        print('找不到文件：' + fileName)

    return data


def toCSV(fileName, data):
    """ 输出CSV格式的数据 """
    with open(sys.path[0] + '/' + fileName, 'w') as toFile:
        csvWriter = csv.writer(toFile)
        for line in data:
            csvWriter.writerow(line)


def printData(data):
    """ 显示数据 """
    for line in data:
        for col in data:
            print(col+'\t')
        print('\n')


def delRow(data, rowID):
    """ 删除行 """
    del data[rowID]
    return data

def delCol(data, colID):
    """ 删除列 """
    for line in data:
        del line[colID]
    return data


def editCell(data, content, rowID, colID):
    """ 修改单元格 """
    data[rowID][colID] = str(content)
    return data


def insertRow(data, rowID):
    """ 插入行 """
    # 创建长度为
    line = ['' for i in range(len(data[0]))]
    data = data[:rowID] + line + data[rowID:]
    return data


def insertCol(data, colID):
    """ 插入列 """
    for line in data:
        line = line[:colID] + ''+ line[colID:]
    return data


if __name__ == '__main__':
    data = getDataFromFile('csv.csv')
    printData(data)

    delRow(data, 3)
    printData(data)

    delCol(data, 3)
    printData(data)

    insertRow(data, 2)
    printData(data)

    insertCol(data, 4)
    printData(data)

    editCell(data, '插入数据', 2, 3)
    printData(data)
