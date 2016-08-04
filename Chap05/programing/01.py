# -*- coding:utf-8 -*-
# !/usr/bin/python
"""在Turtle Graphics中绘制美国国旗"""
from turtle import *


def drawStar(tur, size, fcolor):
    """画五角星。传入的画笔需要朝右"""
    # 到五角星的上顶点
    tur.up()
    tur.left(90)
    tur.forward(size / 2)
    tur.right(18)
    tur.down()

    # 开始画星
    tur.color(fcolor, fcolor)
    tur.begin_fill()
    for i in range(5):
        tur.right(144)
        tur.forward(size)
    tur.end_fill()

    # 将画笔回到五角星中心，朝向右
    tur.up()
    tur.right(162)
    tur.forward(size / 2)
    tur.left(90)
    tur.down()


def drawRectangle(tur, w, h, fcolor):
    """画矩形。传入的画笔需要朝右"""
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
    """在一个矩形范围中绘制50颗星星"""
    tur.speed(1000)
    H = w / 12  # 水平间距
    V = h / 10  # 垂直间距
    x, y = tur.pos()  # 初始保存画笔位置

    for i in range(9):
        # 画笔移动到下一行，朝向右
        tur.up()
        tur.setpos(x, y)
        tur.right(90)
        tur.forward(V)
        tur.left(90)
        tur.down()

        # 保存画笔位置以供画完一行后将画笔归位到行首
        x, y = tur.pos()

        # 准备
        n = 6 - (i % 2)
        startPadding = H * (i % 2 + 1)
        tur.up()
        tur.forward(startPadding)
        tur.down()

        # 开始向右逐个画星
        for j in range(n):
            drawStar(tur, H / 2, fcolor)
            tur.up()
            tur.forward(2 * H)
            tur.down()


def drawFlag(tur, w):
    """画旗主函数"""
    h = w / 19 * 10

    XleftTop = -w / 2
    YleftTop = h / 2

    # 白底
    # tur.up()
    # tur.goto(XleftTop, YleftTop)
    # tur.down()
    # drawRectangle(tur, w, h, 'white')

    # 红条
    for i in range(7):
        tur.up()
        tur.goto(XleftTop, YleftTop - i * h * 2 / 13)
        tur.down()
        drawRectangle(tur, w, h / 13, 'red')

    # 左上角蓝矩形
    tur.up()
    tur.goto(XleftTop, YleftTop)
    tur.down()
    drawRectangle(tur, w / 2.2, h / 13 * 7, 'blue')

    # 50个星星
    tur.up()
    tur.goto(XleftTop, YleftTop)
    tur.down()
    drawFiftyStarsInRectangle(tur, w / 2.2, h / 13 * 7, 'white')


if __name__ == "__main__":
    tur = Turtle()
    tur.speed(800)
    drawFlag(tur, 500)
    done()
