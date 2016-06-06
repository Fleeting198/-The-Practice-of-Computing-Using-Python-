# -*- coding:utf-8 -*-
# !/usr/bin/python

""" 海龟绘图：多边形 """
from turtle import *

n = 3
col = 'black'
while 1:
    try:
        n = int(input('请输入多边形的边数：'))
        col = input('可输入填充颜色，空输入即不填充：')
        color('black', col)
    except ValueError:
        print('输入有误：应输入大于2的整数。')
    except TurtleGraphicsError:
        print('输入有误：不可用或不存在的颜色。')
    else:
        if n < 3:
            print('输入有误：应输入大于2的整数。')
        else:
            break

a = 180-((n-2) * 180 / n)
begin_fill()
for i in range(n):
    forward(100)
    right(a)
end_fill()
done()
