# -*- coding:UTF-8 -*-

print('将进行“俄国农民”或“古埃及”乘法。\n请输入两个整数。')


def func():
    a = b = 0
    while 1:
        try:
            a = int(input('请输入A：'))
            b = int(input('请输入B：'))
        except ValueError:
            print('输入有误：应输入整数。')
        else:
            break

    result = 0
    while b != 0:
        if b % 2 != 0:  # 如果是奇数
            result += a
        a *= 2
        b //= 2
    print('\n最终乘积：', result)

func()
while str(input('是否需要继续计算其他乘积？(y/n) ')).lower() == 'y':
    func()
