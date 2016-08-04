# -*- coding:utf-8 -*-
# !/usr/bin/python
"""导航点路径序列"""
from .NavPos import NavPos


class Route:
    def __init__(self, name):
        self.navPoses = []
        self.name = name

    def __str__(self):
        string = "路径：%s 总长度：%.2f千米：" % (self.name, self.totalLen())
        if self.navPoses:
            for navPos in self.navPoses:
                string += "\n%s" % str(navPos)
        else:
            string += "空路径，无导航点。"
        return string

    def setName(self, name):
        self.name = name

    def distBetween(self, p1, p2):
        if not isinstance(p1, NavPos) or not isinstance(p2, NavPos):
            return False
        return p1.distTo(p2)

    def addNavPos(self, navPos):
        if not isinstance(navPos, NavPos):
            return False
        self.navPoses.append(navPos)
        return True

    def delNavPos(self, navPos):
        del navPos

    def getNavPosByName(self, name):
        """用名字检索导航点，若有返回导航点，若无返回空"""
        for navPos in self.navPoses:
            if name == navPos.name:
                return navPos
        return None

    def totalLen(self):
        length = 0.0
        if len(self.navPoses) < 2:
            return 0
        for i in range(len(self.navPoses)):
            if i == 0: continue
            length += self.distBetween(self.navPoses[i], self.navPoses[i - 1])
        return length

    def clear(self):
        self.navPoses = []
