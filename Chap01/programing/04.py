# -*- coding:UTF-8 -*-
import time

targetYear = 0
while 1:
    try:
        targetYear = int(input("请输入年份，格式'YYYY'：\n"))
    except ValueError:
        print('输入有误：应输入正确的年份。')
    else:
        print()
        break

# 获取当前年份
curYear = int(time.strftime('%Y', time.localtime(time.time())))
diffSec = (targetYear - curYear) * 31536000

curPop = 307357870
targetPop = int(curPop + diffSec / 7 - diffSec / 13 + diffSec / 35)

print('人口估计值：%d 人。' % targetPop)
