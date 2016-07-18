# -*- coding:utf-8 -*-
# !/usr/bin/python

"""在Turtle Graphics中绘制美国国旗"""
from turtle import *


def drawStar(tur, size, fcolor):
    tur.up()
    tur.left(90)
    tur.forward(size / 2)
    tur.right(18)
    tur.down()

    tur.color(fcolor, fcolor)
    tur.begin_fill()
    for i in range(5):
        tur.right(144)
        tur.forward(size)
    tur.end_fill()

    tur.up()
    tur.right(162)
    tur.forward(size / 2)
    tur.left(90)
    tur.down()


def drawRectangle(tur, w, h, fcolor):
    """初始画笔朝向右"""

    tur.color(fcolor, fcolor)
    tur.begin_fill()
    for i in range(2):
        tur.forward(w)
        tur.right(90)
        tur.forward(h)
        tur.right(90)
    tur.end_fill()

    return True


def drawFiftyStarsInRectangle(tur, w, h, fcolor):
    tur.speed(8000)
    H = w / 12  # 水平间距
    V = h / 10  # 垂直间距
    x, y = tur.pos()

    for i in range(9):

        tur.up()
        tur.setpos(x, y)
        tur.right(90)
        tur.forward(V)
        tur.left(90)
        tur.down()

        x, y = tur.pos()

        if i % 2 == 0:
            n = 6
            tur.up()
            tur.forward(H)
            tur.down()

        else:
            n = 5
            tur.up()
            tur.forward(2 * H)
            tur.down()

        for i in range(n):
            drawStar(tur, H / 2, fcolor)
            tur.up()
            tur.forward(2 * H)
            tur.down()


def drawFlag(tur, w):
    h = w / 19 * 10

    # 白底
    # tur.up()
    # tur.goto(-w / 2, h / 2)
    # tur.down()
    # drawRectangle(tur, w, h, 'white')

    # 红条
    for i in range(7):
        tur.up()
        tur.goto(-w / 2, h / 2 - i * h * 2 / 13)
        tur.down()
        drawRectangle(tur, w, h / 13, 'red')

    # 左上角蓝矩形
    tur.up()
    tur.goto(-w / 2, h / 2)
    tur.down()
    drawRectangle(tur, w / 2, h / 13 * 7, 'blue')

    # 50个星星
    tur.up()
    tur.goto(-w / 2, h / 2)
    tur.down()
    drawFiftyStarsInRectangle(tur, w / 2, h / 13 * 7, 'white')


if __name__ == "__main__":
    tur = Turtle()
    tur.speed(800)
    drawFlag(tur, 500)
    done()
