# -*- coding:utf-8 -*-
# !/usr/bin/python
""" 古怪的乘法 """


def func(a, b):
    result = 0
    while b != 0:
        if b % 2 != 0:  # 如果是奇数
            result += a
        a *= 2
        b //= 2
    print('\n最终乘积：', result)


if __name__ == '__main__':
    while 1:
        print('将进行“俄国农民”或“古埃及”乘法。\n请输入两个整数。')
        a = b = 0
        while 1:
            try:
                a = int(input('请输入A：'))
                b = int(input('请输入B：'))
            except ValueError:
                print('输入有误：应输入整数。')
            else:
                break

        func(a, b)
        if str(input('是否需要继续计算其他乘积？(y/n) ')).lower() == 'n':
            break
