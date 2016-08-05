# -*- coding:utf-8 -*-
# !/usr/bin/python
"""
标准普尔500预测
数据来源：http://finance.yahoo.com/q/hp?s=%5EGSP
"""


def makeDataSet(fileName):
    differList = []
    changeList = []
    slopeList = []
    latestSeason = []

    with open(fileName, 'r') as sourseData:
        interval = 13
        intervalCount = 0
        dataGroup = []

        # 跳过文件中的第一行列标题
        for line in sourseData:
            break

        for line in sourseData:
            if intervalCount < interval:
                intervalCount += 1
                dataGroup.append(float(line.split(',')[-1]))
                if intervalCount == 12 and len(latestSeason) == 0:
                    latestSeason.append(line.split(',')[0])
            else:
                # calculate
                differ = max(dataGroup) - min(dataGroup)
                change = dataGroup[-1] - dataGroup[0]

                p = q = r = s = 0
                for i in range(13):
                    p += i
                    q += dataGroup[i]
                    r += i ** 2
                    s += i * dataGroup[i]
                slope = (interval * s - p * q) / (interval * r - p ** 2)

                differList.append(differ)
                changeList.append(change)
                slopeList.append(slope)

                if len(latestSeason) == 1:
                    latestSeason += [differ, change, slope]

                # clear for new group
                intervalCount = 0
                dataGroup.clear()

    return differList, changeList, slopeList, latestSeason


if __name__ == '__main__':
    differList, changeList, slopeList, latestSeason = makeDataSet("S&P500.csv")
    print("在任意13周中，"
          "最大值和最小值之间的最大差值是%.2f，最小差值是%.2f。"
          % (max(differList), min(differList)))
    print("在任意13周中，"
          "第一个值和最后一个值之间的最大变化值是%.2f，最小变化值是%.2f。"
          % (max(changeList), min(changeList)))
    print("在任意13周中，斜率最大的是%.2f，斜率最小的是%.2f。"
          % (max(slopeList), min(slopeList)))
    print("上一个13周（%s起）的差值%.2f，变化值%.2f，斜率%.2f"
          % (latestSeason[0], latestSeason[1], latestSeason[2], latestSeason[3]))
