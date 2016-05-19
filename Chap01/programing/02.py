# -*- coding:UTF-8 -*-
"""20090925: s=166.37 亿英里，v=38241 英里每小时"""

from datetime import *

targetDate = ''
while 1:
    try:
        targetDate = datetime.strptime(input("请输入2009年9月25日后的日期，格式'YYYYMMDD'：\n"), '%Y%m%d')
        print(targetDate)
    except ValueError:
        print('输入不符合格式。')
    else:
        print()
        break

iDiffDay = (targetDate - datetime.strptime('2009/09/25', '%Y/%m/%d')).days

mileDist = iDiffDay * 38241 * 24 + 166.37 * 100000000
kilometerDist = mileDist * 1.609344
auDist = mileDist / 92955887.6
timeRadio = kilometerDist / (299792458 * 3600 / 1000) * 2
print("英里距离 = ", mileDist, "英里。")
print("千米距离 = ", kilometerDist, "千米。")
print("天文单位距离 = ", auDist, "AU。")
print("无线电往返时间 = ", timeRadio, "小时。")
