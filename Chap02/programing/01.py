# -*- coding:UTF-8 -*-
"""设麦粒密度为1.2×10^3kg/m3"""

s = 0
for i in range(1, 65):  # 遍历从1到64
    s += 2**((i-1)+2)   # 由题意

kgWeight = s * 50 / 1000000

print('麦粒总数应为', s, '颗。')
print('共重', kgWeight, '千克。')

size = float(input('请输入一个区域的面积，单位平方米：'))
height = kgWeight / 1200 / size
print('假设麦粒密度为1.2×10^3kg/m3，则覆盖在该面积上的小麦平均深度', height, '米')
