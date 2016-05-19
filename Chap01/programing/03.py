# -*- coding:UTF-8 -*-
""" 1加仑(美)=3.785 412升 """

gallonPetrol = 0.0
while 1:
    try:
        gallonPetrol = float(input("请输入汽油量，单位：加仑："))
    except ValueError:
        print('输入有误：应输入大于0的整数或小数。')
    else:
        if gallonPetrol < 0:
            print('输入有误：应输入大于0的整数或小数。')
        else:
            print()
            break

print("以", gallonPetrol, "加仑汽油计算以下值：")

litrePetrol = gallonPetrol * 3.785412
barrelOil = int(gallonPetrol / 19.5)
poundCO2 = gallonPetrol * 20
gallonAlcohol = gallonPetrol * 115000 / 75700
price = gallonPetrol * 3

print("以公升计量的数量：%.2f" % litrePetrol, "。")
print("生产这些汽油需要的石油的桶数：", barrelOil, "桶。")
print("产生二氧化碳数量：%.2f" % poundCO2, "磅。")
print("能量等效的乙醇：%.2f" % gallonAlcohol, "加仑。")
print("价格：%.2f" % price, "美元。")
