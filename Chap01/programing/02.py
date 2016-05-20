# -*- coding:UTF-8 -*-
"""20090925: s=166.37 亿英里，v=38241 英里每小时"""

from datetime import *

targetDate = ''
iDiffDay = 0
while 1:
    try:
        targetDate = datetime.strptime(input("请输入2009年9月25日后的日期，格式'YYYYMMDD'：\n"), '%Y%m%d')
        print(targetDate)
    except ValueError:
        print('输入有误：不符合格式。')
    else:
        iDiffDay = (targetDate - datetime.strptime('2009/09/25', '%Y/%m/%d')).days
        if iDiffDay > 0:
            print()
            break
        else:
            print('输入有误：应为2009年9月25日后的日期。')

mileDist = iDiffDay * 38241 * 24 + 166.37 * 100000000
kilometerDist = mileDist * 1.609344
auDist = mileDist / 92955887.6
timeRadio = kilometerDist / (299792458 * 3600 / 1000) * 2

print("英里距离 = %.2f 英里。" % mileDist)
print("千米距离 = %.2f 千米。" % kilometerDist)
print("天文单位距离 = %.2f AU。" % auDist)
print("无线电往返时间 = %.2f 小时。" % timeRadio)
