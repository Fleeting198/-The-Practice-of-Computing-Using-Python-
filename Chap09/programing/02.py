# -*- coding:utf-8 -*-
# !/usr/bin/python
"""复制文件"""
import os
import sys


def addCurrentPath(path):
    """若路径没有斜杠，看作是单个文件名，加上当前目录"""
    if '/' not in path and '\\' not in path:
        path = sys.path[0] + '\\' + path
    return path


def copyFile(pathFrom, pathTo):
    # 若源路径只有文件名，加上当前目录
    pathFrom = addCurrentPath(pathFrom)

    # 判断源路径存在
    if not os.path.exists(pathFrom):
        print("源路径不存在。")
        return False

    # 判断源路径指向文件
    if not os.path.isfile(pathFrom):
        print("源路径不指向文件。")
        return False

    # 判断源路径文件为.txt文件
    if os.path.splitext(pathFrom)[1] != '.txt':
        print('只能复制扩展名为".txt"的文件。')
        return False

    # 拆分源文件名
    dirFrom, fileFrom = os.path.split(pathFrom)

    # 若目标路径只有文件名，加上当前目录
    pathTo = addCurrentPath(pathTo)

    print(pathTo)
    print(os.path.isdir(pathTo))
    print(os.path.isfile(pathTo))

    # 拆分目标路径
    if os.path.isdir(pathTo):
        dirTo = pathTo
        fileTo = fileFrom
    # elif os.path.isfile(pathTo):
    #     dirTo, fileTo = os.path.split(pathTo)
    else:
        dirTo, fileTo = os.path.split(pathTo)

    # 判断目标路径的目录部分是否存在
    if not os.path.exists(dirTo):
        print("目标路径不存在。")
        return False

    # 判断目标目录是否已经存在同文件名的文件
    if os.path.exists(os.path.join(dirTo, fileTo)):
        replace = input("目标目录存在相同文件名的文件，是否替换？(Y/N)")
        if str(replace).lower() == 'n':
            print("不替换。")
            return False

    # 开始复制文件
    dataFile = []
    with open(pathFrom, 'r') as srcTextFile:
        for line in srcTextFile:
            dataFile.append(line)

    with open(os.path.join(dirTo, fileTo), 'w') as toTextFile:
        for line in dataFile:
            toTextFile.write(line)

    print("复制完成。")
    return True


if __name__ == '__main__':

    pathFrom = ""
    pathTo = ""
    while 1:
        print("输入时输入'exit'退出。")
        pathFrom = input("请输入欲复制的文件路径：")
        if pathFrom == 'exit' or pathFrom == 'e':
            exit("用户退出程序。")

        pathTo = input("请输入目标路径：")
        if pathTo == 'exit' or pathTo == 'e':
            exit("用户退出程序。")

        if copyFile(pathFrom, pathTo):
            break

    # pathFrom = "d:/a.txt"
    # pathTo = "d:/n/b.txt"
    copyFile(pathFrom, pathTo)
