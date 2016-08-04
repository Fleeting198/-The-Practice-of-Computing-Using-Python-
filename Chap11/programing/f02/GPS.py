# -*- coding:utf-8 -*-
# !/usr/bin/python
"""GPS主程序"""
from random import *
from .NavPos import NavPos
from .Route import Route


class GPS:
    def __init__(self):
        self.routes = [Route('Default route')]
        self.curRouteKey = 0

    def addRoute(self, route=None, name=None):
        """新增一条路径，若未指定路径，生成空路径附加，若不指定键值，自动生成大于0的最小可用键值"""
        if not route:
            route = Route('New route')
        if not isinstance(route, Route):
            return False
        if name:
            route.name = name
        self.routes.append(route)
        return True

    def delRoute(self, i):
        if i >= len(self.routes):
            return False
        # 删除当前路径的情况，切换至第一个路径若存在，设为-1若不存在
        if i == self.curRouteKey:
            self.curRouteKey = 0 if len(self.routes) > 1 else -1
        del self.routes[i]
        return True

    def set_curRouteKey(self, i):
        # 序号为-1时表示当前不在任何路径上
        if i >= len(self.routes) or i < -1:
            return False
        self.curRouteKey = i
        return True

    def showCurRoute(self):
        if self.curRouteKey == -1:
            print("没有选中当前路径。")
        else:
            print("当前路经：%d %s" % (self.curRouteKey, self.routes[self.curRouteKey].name))

    def getRouteByName(self, name=None):
        """用名字检索路径，返回路径列表，若名字为空返回所有路径"""
        routes = []
        if not name:
            for i, route in enumerate(self.routes):
                if not name or route.name == name:
                    routes.append((i, self.routes[i]))
        return routes

    def getNavPosByName(self, name=None):
        """用名字检索导航点，返回导航点列表，若名字为空返回所有导航点"""
        pList = []
        for route in self.routes:
            for navPos in route.navPoses:
                if not name or navPos.name == name:
                    pList.append(navPos)
        return pList

    def gpsGetLongLat(self):
        """随机生成经纬坐标作为当前坐标返回"""
        # 经度 -180 ~ 180
        # 纬度 -90 ~ 90
        longitude = random() * 360 - 180
        latitude = random() * 180 - 90
        return longitude, latitude

    def curNavPos(self):
        """获取当前导航点"""
        longitude, latitude = self.gpsGetLongLat()
        p = NavPos(longitude, latitude, 'Current navPos')
        return p

    def saveNavPos(self, route, navPos):
        """保存导航点"""
        if not isinstance(navPos, NavPos) or not isinstance(route, Route):
            return False
        route.addNavPos(navPos)
        return True

    def saveCurNavPos(self, name=None):
        """保存当前导航点"""
        p = self.curNavPos()
        # 若指定名称，改变名称
        if name:
            p.name = name
        self.saveNavPos(self.routes[self.curRouteKey], p)
        return p

    def userInterface(self):
        def showCurPos():
            print("当前坐标：（%.4f %.4f）" % (self.gpsGetLongLat()))

        def showAllRoutes():
            print("所有路径信息：")
            routes = self.getRouteByName()
            if routes:
                for route in routes:
                    print("%d：%s" % (route[0], route[1]))
            else:
                print("没有匹配结果。")

        def searchNavPos():
            name = input("搜索导航点：")
            navPoses = self.getNavPosByName(name)
            if navPoses:
                for navPos in navPoses:
                    print(navPos)
            else:
                print("没有匹配结果。")

        def searchRoute():
            name = input("搜索路径：")
            routes = self.getRouteByName(name)
            if routes:
                for route in routes:
                    print("%d：%s" % (route[0], route[1]))
            else:
                print("没有匹配结果。")

        def saveCurNavPos():
            print("保存当前位置为导航点（到当前路径）")
            name = input("输入名字（空为默认Current navPos）：")
            p = self.saveCurNavPos(name)
            print("保存完成：%s" % p)

        def curDistTo():
            print("获得当前位置到指定导航点的距离：")
            name = input("输入目标导航点名字：")
            # 获取当前导航点
            curNavPos = self.curNavPos()
            navPoses = self.getNavPosByName(name)
            if navPoses:
                print("当前位置：%s" % curNavPos)
                for navPos in navPoses:
                    print("距离导航点：%s %.4f千米" % (navPos, curNavPos.distTo(navPos)))
            else:
                print("没有匹配结果。")

        def switchCurRoute():
            try:
                newID = int(input("输入要切换到的路径序号："))
                if self.set_curRouteKey(newID):
                    print("切换成功。")
                else:
                    print("切换失败。")
            except ValueError:
                print("切换取消。")

        def clearCurRoute():
            y = str(input("是否清空当前路径？(Y/N)"))
            if y.lower() == 'y':
                self.routes[self.curRouteKey].clear()
                print("已清空。")
            else:
                print("取消清空。")

        def delRouteByName():
            """删除路径，输入名字返回队列中的序号和路径，输入对应序号删除"""
            try:
                name = input("输入要删除的路径名字：")
                routes = self.getRouteByName(name)
                if not routes:
                    print("没有找到路径，删除取消。")
                    return
                for route in routes:
                    print("%d：%s" % (route[0], route[1]))
                i = int(input("输入要删除的路径序号（输入即删除，输入字母取消）："))
                if self.delRoute(i):
                    print("删除成功。")
                else:
                    print("删除失败。")
            except ValueError:
                print("删除取消")

        def newRoute():
            name = input("输入新路径名字（默认‘New route’）：")
            if self.addRoute(name=name):
                print("新建成功。")
            else:
                print("新建失败。")

        dictCommands = {1: showCurPos, 2: saveCurNavPos, 3: curDistTo, 4: searchRoute, 5: searchNavPos,
                        6: showAllRoutes, 7: switchCurRoute, 8: clearCurRoute, 9: delRouteByName, 10: newRoute}
        while 1:
            try:
                self.showCurRoute()
                command = int(input("1：显示当前位置坐标\n"
                                    "2：保存当前位置为导航点（到当前路径）\n"
                                    "3：当前坐标距指定导航点的距离\n"
                                    "4：搜索路径\n"
                                    "5：搜索导航点\n"
                                    "6：显示所有路径（及导航点信息）\n"
                                    "7：切换当前路径\n"
                                    "8：清空当前路径\n"
                                    "9：删除路径\n"
                                    "10：新建路径"))
                dictCommands[command]()
                print("=========================")
            except ValueError:
                print("请输入正确的命令序号")
            except KeyError:
                print("请输入正确的命令序号")
            else:
                break
