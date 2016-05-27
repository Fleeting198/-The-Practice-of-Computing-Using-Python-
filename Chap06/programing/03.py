# -*- coding:UTF-8 -*-
""" 杂乱的英语。对句子中的每个单词，保持头尾字母不变，随机打乱中间字母顺序. """

from random import shuffle
import string


def getWordList(fileName = 'wordList.txt'):
    with open(fileName, 'r') as dataFile:
        wordList = []
        for word in dataFile:
            wordList.append(word.strip().lower())
        return wordList


def messWithSentence(text):
    words = text.split(' ')
    messText = ''
    for word in words:
        punct = ''  # 若单词末尾字符为标点，分离单词和标点，打乱单词后附加标点
        if word[-1] in string.punctuation:
            punct = word[-1]
            word = word[:-1]

        # 不搅乱少于4个字符长的单词
        if len(word) > 3:
            body = list(word[1:-1])
            shuffle(body)
            body = ''.join(body)
            word = word[0] + body + word[-1]

        messText += word + punct + ' '

    return messText


if __name__ == '__main__':
    text = "Four score and seven years ago, " \
           "our fathers brought forth " \
           "on this continent a new nation."
    try:  # 如果没读到文件，就直接采用默认字符串。
        text = getWordList()
    except FileNotFoundError:
        pass

    print('打乱前：', text)
    print('打乱后：', messWithSentence(text))
