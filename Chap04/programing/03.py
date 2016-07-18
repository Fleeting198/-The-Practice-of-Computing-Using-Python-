# -*- coding:utf-8 -*-
# !/usr/bin/python
"""儿童黑话 Pig Latin"""
import string


def toPigLatin(word):
    # 元音字母
    vowels = 'aeiou'

    # 如果第一个字母是元音
    if word[0] in vowels:
        word += 'yay'
    else:
        iFirstVowel = 0
        for i in range(len(word)):
            if word[i] in vowels:
                iFirstVowel = i
                break
        word = word[iFirstVowel:] + word[:iFirstVowel] + 'ay'

    return word


def isWord(word):
    wordRange = string.ascii_letters + '-'
    for ch in word:
        if ch not in wordRange:
            return False
    return True


if __name__ == '__main__':
    # words = ['dog','scratch','is','apple']
    # for word in words:
    #     print(toPigLatin(word))

    while 1:
        word = input('请输入英文单词（输入句号‘.’终止程序）：')
        if word == '.':
            print('输入了句号，程序终止。')
            exit()
        if not isWord(word):
            print('输入有误：应输入英语单词。')
            continue
        print(toPigLatin(word))
