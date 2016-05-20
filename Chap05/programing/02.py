# -*- coding:utf-8 -*-
""" DNA排序 """

def find(someString, substring, start=0, end=None):
    """ 自实现的字符串find方法，与str类型的find方法作用相同 """
    # 输入验证
    result = -1
    if end is None:
        end = len(someString) - 1
    someString = someString[start: end]

    len_mainStr = len(someString)
    len_subStr = len(substring)
    len_diff = len_mainStr - len_subStr

    if len_diff > 0:
        for i in range(len_diff):
            if someString[i: i+len(substring)] == substring:
                result = i + start
                break

    return result


def multiFind(someString, substring, start, end):
    """ 查找字符串中所有子串位置，返回用字符串包含逗号分隔的零个或多个索引位置字符串，
     若没有找到，返回空串
     """
    len_mainStr = len(someString)
    resultStr = ''
    i = find(someString, substring, start, end)
    while -1 < i < len_mainStr:
        resultStr += str(i) + ', '
        i = find(someString, substring, start+i+1, end)

    # 去掉最后一个逗号
    if resultStr:
        resultStr = resultStr[0:-2]

    return resultStr

if __name__ == '__main__':
    S = 'AACCTTTGGAATCCTGCAAA'
    substring = 'CTG'
    start = 0
    end = len(S)

    print('目标序列为%s\n在其中查找%s。' % (S, substring))
    resultFind = multiFind(S, substring, start, end)
    if resultFind:
        print('位置下标序列：%s。' % resultFind)
    else:
        print('没有找到。')
