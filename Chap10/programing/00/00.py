# -*- coding:utf-8 -*-
# !/usr/bin/python
"""
乳腺癌研究
数据来源:
https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/
"""


def makeDataSet(fileName):
    tSet = []
    with open(fileName, 'r') as trainingFile:
        for line in trainingFile:

            # 数据集中有'?'表示值未知的项，在这里忽略掉
            if '?' in line:
                continue

            line = line.strip('\n')
            pid, a1, a2, a3, a4, a5, a6, a7, a8, a9, diag = line.split(',')

            if diag == '4':
                diagMorB = 'm'
            elif diag == '2':
                diagMorB = 'b'
            else:
                diagMorB = 'err'

            patientTuple = (
                pid, diagMorB, int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7), int(a8), int(a9))
            tSet.append(patientTuple)

    return tSet


def sumLists(list1, list2):
    if len(list1) != len(list2):
        return None

    listOfSum = [0] * len(list1)
    for i in range(len(list1)):
        listOfSum[i] = list1[i] + list2[i]

    return listOfSum


def makeAverages(listOfSums, total):
    avgList = [0] * len(listOfSums)
    for i in range(len(listOfSums)):
        avgList[i] = listOfSums[i] / float(total)

    return avgList


def trainClassifier(trainingSet):
    # 计算患者类型数量，良性患者数量和恶性患者数量
    benignSums = [0] * 9
    benignCount = 0
    malignSums = [0] * 9
    malignCount = 0

    for patient in trainingSet:
        if patient[1] == 'b':
            benignCount += 1
            benignSums = sumLists(benignSums, patient[2:])
        else:
            malignCount += 1
            malignSums = sumLists(malignSums, patient[2:])

    # print(benignSums, benignCount, malignSums, malignCount)

    # 计算平均值
    benignAvg = makeAverages(benignSums, benignCount)
    malignAvg = makeAverages(malignSums, malignCount)

    classifier = makeAverages(sumLists(benignAvg, malignAvg), 2)
    return classifier


def classifyTestSet(testSet, classifier):
    results = []
    for patient in testSet:
        benignCount = 0
        malignCount = 0
        for i in range(9):
            if patient[i + 2] > classifier[i]:
                malignCount += 1
            else:
                benignCount += 1

        results.append((patient[0], benignCount, malignCount, patient[1]))
    return results


def reportResults(results):
    totalCount = 0
    inaccurateCount = 0

    for r in results:
        totalCount += 1
        # benignCount > malignCount 应该是b
        if r[1] > r[2]:
            if r[3] == 'm':
                inaccurateCount += 1

        # benignCount < malignCount 应该是m
        else:
            if r[3] == 'b':
                inaccurateCount += 1

    rateInaccurate = inaccurateCount / totalCount
    rateAccurate = 1 - rateInaccurate

    print('准确率：%f，测试量：%d' % (rateAccurate, totalCount))
    return rateAccurate


if __name__ == '__main__':
    trainingFile = 'breast-cancer-training.txt'
    trainingSet = makeDataSet(trainingFile)
    classifier = trainClassifier(trainingSet)

    testFile = 'breast-cancer-test.txt'
    testSet = makeDataSet(testFile)

    resultSet = classifyTestSet(testSet, classifier)
    reportResults(resultSet)
