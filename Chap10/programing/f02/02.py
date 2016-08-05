# -*- coding:utf-8 -*-
# !/usr/bin/python
"""标签云 分析独立宣言"""
import string


def makeHTMLbox(body):
    boxStr = '<div style="width: 560px;' \
             'background-color: rgb(250,250,250);' \
             'border: 1px grey solid; ' \
             'text-align: center">%s</div>'

    return boxStr % body


def makeHTMLword(body, fontsize):
    wordStr = '<span style="font-size: %spx;">%s</span>'
    return wordStr % (str(fontsize), body)


def readStopWords(fileName):
    stopWords = set()
    with open(fileName) as file:
        for line in file:
            line = line.strip('\n')
            stopWords.add(line)

    return stopWords


def getListWordsFromFile(fileNameText, fileNameStopWords):
    """ 读入文本文件，输出单词列表，去除了停用词 """
    words = []
    # 部分在”独立宣言“中的停用词
    stopWords = readStopWords(fileNameStopWords)
    with open(fileNameText, 'r') as file:
        for line in file:
            # 去换行符
            line = line.strip('\n')
            # 去标点
            for ch in line:
                if ch in string.punctuation:
                    line = line.replace(ch, '')
            # 单词分开
            lineWords = line.split(' ')
            # 去掉停用词
            words += [x for x in lineWords if x and x.lower() not in stopWords]
    return words


def getDictCountsFromListWords(listWords):
    wordCounts = {}
    for word in listWords:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
    return wordCounts


def getHTMLFromDictCounts(wordCounts):
    strHTML = ''

    for k, v in wordCounts.items():
        if v >= 3:
            strHTML += makeHTMLword(k, v * 10 + 10)
            strHTML += ' '

    return makeHTMLbox(strHTML)


def makeHTMLFile(strHTML):
    with open('tagCloud.html', 'w') as HTMLFile:
        HTMLFile.write(strHTML)


if __name__ == '__main__':
    makeHTMLFile(
        getHTMLFromDictCounts(
            getDictCountsFromListWords(
                getListWordsFromFile('the Declaration of Independence.txt', 'stop words.txt'))))
