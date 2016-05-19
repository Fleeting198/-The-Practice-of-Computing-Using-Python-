# -*- coding:UTF-8 -*-

num = 0.0
while 1:
    try:
        num = float(input('请输入一个数字：'))
    except ValueError:
        print('输入有误。')
    else:
        print()
        break

if 2 <= num <= 20 and num % 3 == 0:
    print('这个数字在2 ~ 20之间，并且能被3整除。')
else:
    print('这个数字不在2 ~ 20之间，或者不能被3整除。')
