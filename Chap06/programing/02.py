# -*- coding:UTF-8 -*-
""" 帕斯卡三角形 """

# 输入三角形的高度
height = 1
while 1:
    try:
        height = int(input('请输入要生成的帕斯卡三角形的高度：'))
    except ValueError:
        print('输入有误：三角形的高度必须是大于0的整数。')
    else:
        if height < 1:
            print('输入有误：三角形的高度必须是大于0的整数。')
        else:
            break

# TODO: 用迭代器生成

rows = [[1]]  # 写入第一行

for i in range(1, height):
    row = [0 for i in range(i+1)]
    row[0] = row[i] = 1
    for j in range(1, i):
        row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
    rows.append(row)

for row in rows:
    print(row)
