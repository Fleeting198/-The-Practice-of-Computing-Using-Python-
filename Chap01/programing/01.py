# -*- coding:utf-8 -*-
# !/usr/bin/python
"""已知淡水总量22810km^3，占水22%，求北美五大湖淡水体积。设美国国土面积9372614km^2"""

volume = 22810 * 0.22
depth = volume / 9372614 * 1000
print('(1)Volume = %.2f km^3.' % volume)
print('(2)Depth = %.2f m.' % depth)
