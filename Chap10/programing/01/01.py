# -*- coding:utf-8 -*-
# !/usr/bin/python
"""
收入预测分类器
数据来源:
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/
"""
import pandas as pd
import types

def makeDataSet(fileName):
    tSet = pd.read_csv(fileName)
    tSet.columns = [title.strip() for title in tSet.columns]
    # 保留需要的字段
    tSet = tSet[['age', 'workclass', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex',
                 'capital-gain', 'capital-loss', 'hours-per-week', 'income']]
    tSet.columns = ['age', 'workclass', 'educationNum', 'maritalStatus', 'occupation', 'relationship', 'race', 'sex',
                    'capitalGain', 'capitalLoss', 'hoursPerWeek', 'income']

    return tSet


# def sumLists(list1, list2):
#     if len(list1) != len(list2):
#         return None
#
#     listOfSum = [0] * len(list1)
#     for i in range(len(list1)):
#         listOfSum[i] = list1[i] + list2[i]
#
#     return listOfSum
#
#
# def makeAverages(listOfSums, total):
#     avgList = [0] * len(listOfSums)
#     for i in range(len(listOfSums)):
#         avgList[i] = listOfSums[i] / float(total)
#
#     return avgList


def trainClassifier(trainingSet):
    trainingSet = pd.DataFrame(trainingSet)
    # 计算收入类型数量，<=50K 和 >50K
    benignCount = list(trainingSet['income']).count(' <=50K')
    malignCount = list(trainingSet['income']).count(' >50K')



    for person in trainingSet.itertuples():
        print(person)
        # if person[1] == 'b':
        #     benignCount += 1
        #     benignSums = sumLists(benignSums, person[2:])
        # else:
        #     malignCount += 1
        #     malignSums = sumLists(malignSums, person[2:])
    #
    # # print(benignSums, benignCount, malignSums, malignCount)
    #
    # # 计算平均值
    # benignAvg = makeAverages(benignSums, benignCount)
    # malignAvg = makeAverages(malignSums, malignCount)
    #
    # classifier = makeAverages(sumLists(benignAvg, malignAvg), 2)
    # return classifier


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
    trainingFile = 'adult-data.csv'
    trainingSet = makeDataSet(trainingFile)
    classifier = trainClassifier(trainingSet)

    # testFile = 'breast-cancer-test.txt'
    # testSet = makeDataSet(testFile)
    #
    # resultSet = classifyTestSet(testSet, classifier)
    # reportResults(resultSet)
