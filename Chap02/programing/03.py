# -*- coding:utf-8 -*-
# !/usr/bin/python
"""海龟绘图：多边形"""

from turtle import *

brush = Turtle()

n = 3
fillColor = ''
while 1:
    try:
        n = int(input('请输入多边形的边数：'))
        fillColor = input('可输入填充颜色，空输入即不填充：')
        brush.color('black', fillColor)
    except ValueError:
        print('输入有误：应输入大于2的整数。')
    except TurtleGraphicsError:
        print('输入有误：不可用或不存在的颜色。')
    else:
        if n < 3:
            print('输入有误：应输入大于2的整数。')
        else:
            break

angel = 180 - ((n - 2) * 180 / n)
brush.begin_fill()
for i in range(n):
    brush.forward(600/n)
    brush.right(angel)
brush.end_fill()
done()
