# -*- coding:utf-8 -*-
# !/usr/bin/python
"""折纸有多厚"""
# 假设纸的厚度为1/200 cm

print('现欲将一张厚度为 1/200 厘米的纸折叠。')

n = 0
while 1:
    try:
        n = int(input('请输入折叠次数：'))
    except ValueError:
        print('输入有误：应输入大于0的整数。')
    else:
        if n < 0:
            print('输入有误：应输入大于0的整数。')
        else:
            break

# thickness = 0.005 * 2**n / 100    # 次方运算的方法

thickness = 5e-05  # 循环的方法 纸张厚度 1/200/100 米
for i in range(1, n + 1):
    thickness *= 2

print('将一张纸折叠 %d 次后，厚度为 %.2f 米。' % (n, thickness))
