# -*- coding:utf-8 -*-
# !/usr/bin/python
"""
收入预测分类器
数据来源:
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/
"""
import copy

emptyPerson = {'age': 0, 'education_num': 0, 'capital_gain': 0, 'capital_loss': 0, 'hours_per_week': 0,
               'workClass': {}, 'marital_status': {}, 'occupation': {}, 'relationShip': {}, 'race': {}, 'sex': {}}
keyContinuous = ('age', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week')
keyDiscrete = ('workClass', 'marital_status', 'occupation', 'relationShip', 'race', 'sex')
listOfHigh = []


def makeDataSet(fileName):
    """ 从文件读取生成数据 """
    tSet = []
    with open(fileName, 'r') as trainingFile:
        for line in trainingFile:
            if '?' in line:
                continue

            line = line.replace(' ', '').strip().strip('.')

            age, workClass, fnlwgt, education, education_num, marital_status, occupation, relationShip, race, sex, \
            capital_gain, capital_loss, hours_per_week, native_country, salary = line.split(',')

            # 初步处理字段
            if salary == '<=50K':
                salary = 'lt'
            elif salary == '>50K':
                salary = 'mt'
            else:
                salary = 'err'

            personDict = {'salary': salary,
                          'age': int(age),
                          'education_num': int(education_num),
                          'capital_gain': int(capital_gain),
                          'capital_loss': int(capital_loss),
                          'hours_per_week': int(hours_per_week),
                          'workClass': workClass,
                          'marital_status': marital_status,
                          'occupation': occupation,
                          'relationShip': relationShip,
                          'race': race,
                          'sex': sex
                          }

            tSet.append(personDict)

    return tSet


def sumDictIndividual2Sum(dictSum, dictIndividual):
    """ 将个人的信息字典累加到累计字典中 """

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

    mtSums = copy.deepcopy(emptyPerson)
    ltSums = copy.deepcopy(emptyPerson)
    mtCount = 0
    ltCount = 0

    for person in trainingSet:
        if person['salary'] == 'mt':
            mtCount += 1
            mtSums = sumDictIndividual2Sum(mtSums, person)
        elif person['salary'] == 'lt':
            ltCount += 1
            ltSums = sumDictIndividual2Sum(ltSums, person)

    # 计算平均值
    mtAvg = makeAverages(mtSums, mtCount)
    ltAvg = makeAverages(ltSums, ltCount)

    # 比较数值并记录，为分类阶段准备规则，记录应分类为>50K的属性
    for key in keyContinuous:
        if mtAvg[key] > ltAvg[key]:
            listOfHigh.append(key)
    for key in keyDiscrete:
        for k in mtAvg[key].keys():
            if mtAvg[key][k] > ltAvg[key][k]:
                listOfHigh.append(k)

    classifier = makeAverages(sumDicts(mtAvg, ltAvg), 2)
    return classifier


def classifyTestSet(testSet, classifier):
    """ 对测试数据进行分类 """
    results = []
    for person in testSet:
        mtCount = 0
        ltCount = 0

        for k, v in person.items():
            if k == 'salary':
                continue
            elif k in keyContinuous:
                if person[k] > classifier[k] and k in listOfHigh:
                    mtCount += 1
                else:
                    ltCount += 1
            elif k in keyDiscrete:
                if person[k] in listOfHigh:
                    mtCount += 1
                else:
                    ltCount += 1

        results.append((person['salary'], mtCount, ltCount))
    return results


def reportResults(results):
    """ 统计结果 """
    totalCount = 0
    inaccurateCount = 0

    for r in results:
        totalCount += 1

        # mtCount > ltCount 应该是mt
        if r[1] > r[2]:
            if r[0] == 'lt':
                inaccurateCount += 1

        # mtCount < ltCount 应该是lt
        else:
            if r[0] == 'mt':
                inaccurateCount += 1

    rateInaccurate = inaccurateCount / totalCount
    rateAccurate = 1 - rateInaccurate

    print('准确率：%f，测试量：%d' % (rateAccurate, totalCount))
    return rateAccurate


if __name__ == '__main__':
    trainingFile = 'adult-data.txt'
    trainingSet = makeDataSet(trainingFile)
    classifier = trainClassifier(trainingSet)

    testFile = 'adult-test.txt'
    testSet = makeDataSet(testFile)

    resultSet = classifyTestSet(testSet, classifier)
    reportResults(resultSet)
