# -*- coding:utf-8 -*-
# !/usr/bin/python
""" 复制文件 """
import os
import sys


def copytxt(urlFrom, urlTo):

    dirTo = ''
    fileTo = ''

    # 检查是否有指定文件路径
    # 若没有路径，假设在当前文件夹中
    if '/' not in urlFrom:
        urlFrom = sys.path[0] + '/' + urlFrom

    # 检查源路径存在且是合法路径
    if not os.path.exists(urlFrom):
        print('欲复制的文件路径不合法或不存在。')
        return False

    # 检查目标路径存在且是合法路径
    if not os.path.exists(urlTo):
        print('目标路径不合法或不存在。')
        return False

    if os.path.isfile(urlTo):
        dirTo, fileTo = os.path.split(urlTo)
    elif os.path.isdir(urlTo):
        fileTo = os.path.split(urlFrom)[1]
        dirTo = urlTo

    # 检查源文件是否是.txt文件
    if os.path.splitext(urlFrom)[1] != '.txt':
        print('只复制以".txt"为扩展名的文件。')
        return False

    # 开始复制文件
    dataFile = []
    with open(urlFrom, 'r') as srcTextFile:
        for line in srcTextFile:
            dataFile.append(line)

    with open(os.path.join(dirTo, fileTo), 'w') as toTextFile:
        for line in dataFile:
            toTextFile.write(line)


if __name__ == '__main__':
    copytxt('src.txt', 'D:/')
