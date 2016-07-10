# -*- coding:utf-8 -*-
# !/usr/bin/python
"""
国旗分析
數據來源：
https://archive.ics.uci.edu/ml/machine-learning-databases/flags/
"""
import copy

lenFlag = 0
sumTemplate = {'bars': 0, 'stripes': 0, 'colours': 0, 'red': 0, 'green': 0, 'blue': 0, 'gold': 0, 'white': 0,
               'black': 0, 'orange': 0, 'circles': 0, 'crosses': 0, 'saltires': 0, 'quarters': 0, 'sunstars': 0,
               'crescent': 0, 'triangle': 0, 'icon': 0, 'animate': 0, 'text': 0,
               'mainhue': {}, 'topleft': {}, 'botright': {}}
keyContinuous = ('bars', 'stripes', 'colours', 'red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'circles',
                 'crosses', 'saltires', 'quarters', 'sunstars', 'crescent', 'triangle', 'icon', 'animate', 'text',)
keyDiscrete = ('mainhue', 'topleft', 'botright')
listOfHigh = []


def makeDataSet(fileName):
    dataSet = []
    with open(fileName, 'r') as sourceFile:
        for line in sourceFile:
            name, landmass, zone, area, population, language, religion, bars, stripes, \
            colours, red, green, blue, gold, white, black, orange, mainhue, \
            circles, crosses, saltires, quarters, sunstars, crescent, triangle, icon, \
            animate, text, topleft, botright = line.strip().split(',')

            # 只判定主导宗教是基督教或不是基督教
            religion = 1 if int(religion) == 0 or int(religion) == 1 else 0

            flag = {'name': name, 'religion': religion, 'bars': int(bars), 'stripes': int(stripes),
                    'colours': int(colours), 'red': int(red), 'green': int(green), 'blue': int(blue), 'gold': int(gold),
                    'white': int(white), 'black': int(black), 'orange': int(orange), 'mainhue': mainhue,
                    'circles': int(circles), 'crosses': int(crosses), 'saltires': int(saltires),
                    'quarters': int(quarters), 'sunstars': int(sunstars), 'crescent': int(crescent),
                    'triangle': int(triangle), 'icon': int(icon), 'animate': int(animate), 'text': int(text),
                    'topleft': topleft, 'botright': botright}

            # 将离散值加入到累加字典模版的键值
            for key in keyDiscrete:
                sumTemplate[key][flag[key]] = 0

            dataSet.append(flag)

    lenFlag = len(dataSet[0])
    return dataSet


def sumDictIndividual2Sum(dictSum, dictIndividual):
    """ 将个体的信息字典累加到累计字典中 """

    def countStrToDict(dict, str):
        """ 将str计数到dict中 """
        if str in dict:
            dict[str] += 1
        else:
            dict[str] = 1
        return dict

    dictOfSum = {}
    for key in keyContinuous:
        dictOfSum[key] = dictSum[key] + dictIndividual[key]
    for key in keyDiscrete:
        dictOfSum[key] = countStrToDict(dictSum[key], dictIndividual[key])

    return dictOfSum


def sumDicts(dict1, dict2):
    """ 将两个累计字典累加 """

    def countDictToDict(dict1, dict2):
        """ 将两个dict的计数合并 """
        for k, v in dict2.items():
            if k in dict1:
                dict1[k] += v
            else:
                dict1[k] = 1
        return dict1

    dictOfSum = {}
    for key in keyContinuous:
        dictOfSum[key] = dict1[key] + dict2[key]
    for key in keyDiscrete:
        dictOfSum[key] = countDictToDict(dict1[key], dict2[key])

    return dictOfSum


def makeAverages(dictOfSums, total):
    """ 对累计字典取平均值 """

    def avgCountDict(dict1):
        for k, v in dict1.items():
            dict1[k] /= total
        return dict1

    avgList = {}
    for key in keyContinuous:
        avgList[key] = dictOfSums[key] / total
    for key in keyDiscrete:
        avgList[key] = avgCountDict(dictOfSums[key])

    return avgList


def trainClassifier(trainingSet):
    """ 训练分类器 """
    if len(trainingSet) == 0:
        return None

    ChristSums = copy.deepcopy(sumTemplate)
    noChristSums = copy.deepcopy(sumTemplate)
    ChristCount = 0
    noChristCount = 0

    for flag in trainingSet:
        if flag['religion']:
            ChristCount += 1
            ChristSums = sumDictIndividual2Sum(ChristSums, flag)
        elif not flag['religion']:
            noChristCount += 1
            noChristSums = sumDictIndividual2Sum(noChristSums, flag)

    # 计算平均值
    ChristAvg = makeAverages(ChristSums, ChristCount)
    noChristAvg = makeAverages(noChristSums, noChristCount)

    # 比较数值并记录，为分类阶段准备规则，记录应分类为基督教主导的属性
    for key in keyContinuous:
        if ChristAvg[key] > noChristAvg[key]:
            listOfHigh.append(key)
    for key in keyDiscrete:
        for k in ChristAvg[key].keys():
            if ChristAvg[key][k] > noChristAvg[key][k]:
                listOfHigh.append(key + k)

    classifier = makeAverages(sumDicts(ChristAvg, noChristAvg), 2)
    return classifier


def classifyTestSet(testSet, classifier):
    results = {}
    for flag in testSet:
        ChristCount = 0
        noChristCount = 0

        for k, v in flag.items():
            if k == 'salary':
                continue
            elif k in keyContinuous:
                if k in listOfHigh:
                    if flag[k] > classifier[k]:
                        ChristCount += 1
                    else:
                        noChristCount += 1
                else:
                    if flag[k] > classifier[k]:
                        noChristCount += 1
                    else:
                        ChristCount += 1
            elif k in keyDiscrete:
                if k + flag[k] in listOfHigh:
                    ChristCount += 1
                else:
                    noChristCount += 1

        results[flag['name']] = (ChristCount, noChristCount, flag['religion'])
    return results


def reportResults(results):
    totalCount = 0
    inaccurateCount = 0

    for v in results.values():
        totalCount += 1
        # ChirstCount > noChirstCount 应该是1
        if v[0] > v[1]:
            if v[2] == 0:
                inaccurateCount += 1

        # ChirstCount < noChirstCount 应该是0
        else:
            if v[2] == 1:
                inaccurateCount += 1

    rateInaccurate = inaccurateCount / totalCount
    rateAccurate = 1 - rateInaccurate

    print('准确率：%f，测试量：%d' % (rateAccurate, totalCount))
    return rateAccurate


if __name__ == '__main__':
    trainingFile = 'flags.txt'
    trainingSet = makeDataSet(trainingFile)
    classifier = trainClassifier(trainingSet)

    testFile = 'flags.txt'
    testSet = makeDataSet(testFile)

    resultSet = classifyTestSet(testSet, classifier)
    reportResults(resultSet)

    while 1:
        name = input("请输入一个国家的名字：")
        if name.lower() == 'done':
            break
        try:
            religion = resultSet[name][2]
        except KeyError:
            print("没有%s的信息。"%name)
        else:
            if religion:
                print("%s是一个基督教国家。" % name)
            else:
                print("%s不是一个基督教国家。" % name)
