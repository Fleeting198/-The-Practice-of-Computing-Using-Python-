# -*- coding:utf-8 -*-
# !/usr/bin/python
"""导航点"""
from math import cos, sqrt, asin, sin, pi


class NavPos:
    def __init__(self, longitude, latitude, name='default'):
        if not -180 < longitude < 180:
            longitude = 0
        if not -90 < latitude < 90:
            latitude = 0
        self.longitude = longitude
        self.latitude = latitude
        self.name = name

    def __str__(self):
        return "导航点：%s（%.4f %.4f）" % (self.name, self.longitude, self.latitude)

    def distTo(self, navPoint):
        """计算两个导航点间距离"""
        EARTH_RADIUS = 6378.137

        def rad(d):
            return d * pi / 180.0

        if not isinstance(navPoint, NavPos):
            return False

        radLat1 = rad(self.latitude)
        radLat2 = rad(navPoint.latitude)
        a = radLat1 - radLat2
        b = rad(self.longitude) - rad(navPoint.longitude)
        s = 2 * asin(sqrt(pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * pow(sin(b / 2), 2)))
        s *= EARTH_RADIUS
        s = round(s * 10000) / 10000
        return s
