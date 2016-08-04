# -*- coding:utf-8 -*-
# !/usr/bin/python
"""疯狂Libs"""
import string

story = "Once upon a time in the middle of a ADJECTIVE_ONE NOUN_ONE stood a ADJECTIVE_TWO NOUN_TWO, " \
        "the home of a ADJECTIVE_ONE ADJECTIVE_THREE NOUN_THREE known to everyone as GIRLS_NAME."

if __name__ == "__main__":
    wordsInsert = []

    # 用空格分割段落
    for word in story.split(' '):
        # 若结尾有标点，去除
        if word[-1:] in string.punctuation:
            word = word[:-1]

        # 若除去下划线都是大写，则为要替换的部分
        if word.replace('_', '').isupper():
            if word not in wordsInsert:
                wordsInsert.append(word)

    print("原文：", story)

    for word in wordsInsert:
        replaceWord = input("输入替代的单词 %s：" % word)
        story = story.replace(word, replaceWord)

    print("替换后的版本：", story)
