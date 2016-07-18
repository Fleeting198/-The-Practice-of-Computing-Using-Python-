# -*- coding:utf-8 -*-
# !/usr/bin/python
"""智多星"""

import random


def inputCode(msg):
    code = ""
    while 1:
        try:
            code = str(input(msg)).upper()
        except ValueError:
            print("输入有误：应输入4个英文字母（A~F）。")
        else:
            if len(code) != 4:
                print("输入有误：应输入4个英文字母（A~F）。")

            # 检查输入字母
            else:
                # 去除范围外的字符
                code = ''.join(list(filter(lambda x: x in "ABCDEF", code)))

                # 再次检测输入长度，这里转成集合后再转回列表，可以去除重复字符
                if len(list(set(code))) != 4:
                    print("输入有误：应输入4个英文字母（A~F）。")

                # 检查通过的情况
                else:
                    break
    return code


def reportProgress(length, guessCode, guessResult):
    print("目前的棋盘：")
    for i in range(length + 1):
        print(' '.join(guessCode[i]))
        print(' '.join(guessResult[i]))
        print()


if __name__ == "__main__":

    while 1:
        print("开始新的一局。")

        # code = inputCode("请输入密码序列，4个英文字母（A~F）：")
        code = ''.join(random.sample('ABCDEF', 4))

        guessCode = [""] * 12
        guessResult = guessCode[:]
        bWin = False
        # 猜测12次
        for i in range(12):
            print("现在猜测第%d次，剩余%d次。" % (i + 1, 12 - i - 1))
            guessCode[i] = inputCode("请输入猜测密码序列：")
            guessResult[i] = ""
            correctCount = 0

            for j in range(4):
                # 颜色和位置都正确
                if guessCode[i][j] == code[j]:
                    guessResult[i] += 'b'  # 黑色计分钉子
                    correctCount += 1

                # 颜色正确位置不正确
                elif guessCode[i][j] in code:
                    guessResult[i] += 'w'  # 白色计分钉子

                # 颜色不正确
                else:
                    guessResult[i] += ' '  # 无计分钉子

            reportProgress(i, guessCode, guessResult)

            # 若都是黑色，宣布胜利
            if correctCount == 4:
                print("胜利！共用了%d次全部猜测正确。" % (i + 1))
                bWin = True
                break

        if not bWin:
            print("失败，猜测次数用尽。")

        ifAgain = input("是否开始一局新的游戏？(Y/N)")
        if ifAgain.upper() == 'N':
            break
