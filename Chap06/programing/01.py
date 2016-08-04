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
    return listAnswer


def puzzle_e(wordList):
    listAnswer = list(filter(
        lambda x: x.islower() and len(x) == 7 and 's' not in x
                  and x.count('a') + x.count('e') + x.count('i') + x.count('o') + x.count('u') == 1,
        wordList))
    return listAnswer


def puzzle_f(wordList):
    """包含所有字母至少一次即为包含"""
    listAnswer = wordList[:]
    strExam = "memphis"
    for word in wordList:
        for ch in strExam:
            if ch not in word:
                listAnswer.remove(word)
                break

    return listAnswer


def puzzle_g(wordList):
    """包含字符串'tantan'"""
    listAnswer = [word for word in wordList if "tantan" in word]
    return listAnswer


def puzzle_h(wordList):
    abbreviations = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                     'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
                     'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
                     'WI', 'WY')
    listAnswer = wordList[:]

    for word in wordList:
        for i in range(len(word) - 1):
            if word[i:i + 2].upper() not in abbreviations:
                listAnswer.remove(word)
                break

    return listAnswer


def puzzle_i(wordList):
    """查找使用'i','j','t','x'仅一次的单词"""
    listAnswer = list(filter(lambda x: x.count('i') + x.count('j') + x.count('t') + x.count('x') == 1, wordList))
    return listAnswer


def puzzle_j(wordList):
    """查找包含连续字母'nacl'的4个单词"""
    listAnswer = [word for word in wordList if "nacl" in word]
    listAnswer = listAnswer[:4]  # 只输出前四个
    return listAnswer


def puzzle_k(wordList):
    """按顺序包含元音字母"""
    listAnswer = []
    vowels = "aeiou"
    for word in wordList:
        # 去掉非元音字母
        for ch in word:
            if ch not in vowels:
                word = word.replace(ch, '')

        # 是否成为元音字符串序列，元音字符重复的不算
        if word.lower() == vowels:
            listAnswer.append(''.join(word))

    return listAnswer


def puzzle_l(wordList):
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

        # 若同时存在三个单词，它们的前缀不同，其余部分相同，加入答案列表
        if targetWords[0] in wordList and targetWords[1] in wordList and targetWords[2] in wordList:
            listAnswer.append(targetWords)

            # 将已选出单词从候选列表中去掉，避免重复
            wordList = [word for word in wordList if word not in targetWords]

    return listAnswer


def puzzle_n():
    def check(word):
        for month in months:
            if month in word:
                return True
        return False

    # 所有美国州首府的名称
    listAnswer = [
        'Montgomery', 'Juneau', 'Phoenix', 'Littlerock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee',
        'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'DesMoines', 'Topeka', 'Frankfort', 'BatonRouge',
        'Augusta', 'Annapolis', 'Boston', 'Lansing', 'St.Paul', 'Jackson', 'JeffersonCity', 'Helena', 'Lincoln',
        'CarsonCity', 'Concord', 'Trenton', 'SantaFe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'OklahomaCity',
        'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'SaltLakeCity', 'Montpelier',
        'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']

    months = (
        'January''February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
        'December')

    listAnswer = list(filter(lambda x: check(x), listAnswer))
    return listAnswer
