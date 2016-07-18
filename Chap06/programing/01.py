# -*- coding:utf-8 -*-
# !/usr/bin/python
"""填字游戏"""


def getWordList(fileName='wordLost.txt'):
    wordList = []
    with open(fileName, 'r') as dataFile:
        for word in dataFile:
            wordList.append(word.strip().lower())
    return wordList


def puzzle_a(wordList):
    """寻找存在的(word, word + 'er', word + 'est')三元组"""
    listAnswer = []
    for word in wordList:
        worder = word + 'er'
        wordest = word + 'est'
        if worder in wordList and wordest in wordList:
            listAnswer.append((word, worder, wordest))

    return listAnswer


def puzzle_b(wordList):
    strExam = "lmnopqrstuv"
    wordList = list(filter(lambda x: x.islower() and '-' not in x, wordList))  # 初步筛选
    listAnswer = wordList[:]

    # 进一步筛选
    for word in wordList:
        for ch in strExam:
            if ch not in word:
                listAnswer.remove(word)
                break

    return listAnswer


def puzzle_c(wordList):
    listAnswer = []
    pronouns = (
        'thou', 'thee', 'thine', 'thy', 'i', 'me', 'mine', 'my', 'we', 'us', 'ours', 'our', 'you', 'yours', 'your',
        'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them', 'theirs', 'their')
    for pre in pronouns:
        for lat in pronouns:
            w = pre + lat  # 两个连续代词组成的单词
            if w in wordList and w not in listAnswer:
                listAnswer.append(w)

    return listAnswer


def puzzle_d(wordList):
    listAnswer = [(word, 'H' + word[1:]) for word in filter(lambda x: len(x) == 6 and x[0] == 'C', wordList)]

    # listAnswer = []
    # for word in wordList:
    #     if len(word) == 6 and word[0] == 'C':
    #         listAnswer.append((word, 'C'+word[1:]))

    return listAnswer


def puzzle_e(wordList):
    wordList = list(filter(lambda x: x.islower() and len(x) == 7 and 's' not in x, wordList))
    listAnswer = wordList[:]
    vowels = 'aeiou'
    for word in wordList:
        countVowel = 0
        for ch in vowels:
            countVowel += word.count(ch)
            if countVowel > 0:
                listAnswer.remove(word)
                break

    return listAnswer


def puzzle_f(wordList):
    """ 包含所有字母至少一次即为包含 """
    listAnswer = wordList[:]
    strExam = "memphis"
    for word in wordList:
        for ch in strExam:
            if ch not in word:
                listAnswer.remove(word)
                break

    return listAnswer


def puzzle_g(wordList):
    # TODO
    """包含字符串是指上题中的包含所有字母还是包含连续字符串？"""
    listAnswer = list(filter(lambda x: "tantan" in x, wordList))

    return listAnswer


def puzzle_h(wordList):
    # TODO
    listAnswer = []
    pass


def puzzle_i(wordList):
    """ 查找使用'i','j','t','x'仅一次的单词 """
    listAnswer = []
    tupleExam = 'ijtx'
    for word in wordList:
        count_ch = 0
        isGood = True
        for ch in tupleExam:
            count_ch += word.count(ch)
            if count_ch > 1:
                isGood = False
                break
        if isGood:
            listAnswer.append(word)

    return listAnswer


def puzzle_j(wordList):
    """ 查找包含连续字母的四个单词 """
    listAnswer = [word for word in wordList if "nacl" in word]
    return listAnswer


def puzzle_k(wordList):
    """ 按顺序包含元音字母 """
    # 测试完成
    listAnswer = []
    vowels = 'aeiou'
    for word in wordList:
        # 去掉非元音字母
        for ch in word:
            if ch not in vowels:
                word = word.replace(ch, '')

        # 将字符串转为元组来比较，之后转回字符串返回
        word = tuple(word)
        if word == vowels:
            listAnswer.append(''.join(word))

    return listAnswer


def puzzle_l(wordList):
    # 测试完成
    listAnswer = []
    strExam = "rate"
    for word in wordList:
        if len(word) == 8:
            # 去掉"rate"中字母各一次
            for ch in strExam:
                word = word.replace(ch, '', 1)

            # 检查剩余的字符串是否由两对连续字母组成
            if word[0] == word[1] and word[2] == word[3]:
                listAnswer.append(word)

    return listAnswer


def puzzle_m(wordList):
    listAnswer = []
    affix = ('sw', 'tw', 'wh')  # 前两个字母限定
    # 长度至少大于2才能比较其余部分
    wordList = list(filter(lambda x: len(x) > 2 and x[:2] in affix, wordList))

    for word in wordList:
        targetWords = [a + word[2:] for a in affix]
        # 若同时存在三个单词，它们的前缀不同，其余部分相同，加入答案数组
        if targetWords[0] in wordList and targetWords[1] in wordList and targetWords[2] in wordList:
            listAnswer.append(targetWords)
            # 将已选出单词从候选列表中去掉，避免重复
            wordList = [word for word in wordList if word not in targetWords]

    return listAnswer


def puzzle_n(wordList):
    # TODO
    pass


if __name__ == '__main__':
    pass
    # print(puzzle_d(["Chhhhh", "Fwqwqw", "Cfff","Cjgkik"]))
    # print(puzzle_k(["afferrissotupp"]))
    # print(puzzle_l(["ssrattte"]))
    # print(puzzle_m(['swat', 'twat', 'twat', 'what', 'what', 'swat']))
