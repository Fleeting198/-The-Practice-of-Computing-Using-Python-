# -*- coding:utf-8 -*-

# dict格式： {'电影1': ('演员1','演员2', ...), '电影2': (...), ...}

def getDictData(file_name):
    # TODO: 找到书上要求的数据文件
    dict_data = {}
    return dict_data


def actOfAll(dict_data, movie1, movie2):
    """ 两部电影中所有演员 """
    return set(dict_data[movie1]).union(set(dict_data[movie2]))


def actOfBoth(dict_data, movie1, movie2):
    """ 参演两部电影的演员 """
    return set(dict_data[movie1]).intersection(set(dict_data[movie2]))


def actOfOne(dict_data, movie1, movie2):
    """ 只参演了其中一部电影的演员 """
    return set(dict_data[movie1]).symmetric_difference(set(dict_data[movie2]))


def jointAct(dict_data, act):
    jointActs = ()
    for v in dict(dict_data).values():
        if act in v:
            jointActs += v

    return jointActs


def checkActIpt(dict_data, ipt):
    jointActs = jointAct(dict_data, ipt)
    if jointActs:
        print('输入的是演员，所有与他合演的演员如下：')
        print(jointActs)
    else:
        print('输入的不是电影也不是演员。')


if __name__ == '__main__':
    dict_data = getDictData("")
    while 1:
        ipt1 = input("请输入电影名或演员名称（输入'#'退出）：")
        if ipt1 == '#':
            exit()
        # 若是电影名
        if ipt1 in dict_data:
            ipt2 = input('输入的是电影名，请再输入一个电影名，或输入演员名查询所有与他合演的演员：')
            # 如果第二次输入是电影名
            if ipt2 in dict_data:
                while 1:
                    print("对这两部电影%s、%s，可选操作有(输入'#'退出电影操作)：")
                    print("输入'&'：找出两部电影中所有演员；")
                    print("输入'|'：找出参演两部电影的演员；")
                    print("输入'-'：找出只参演其中一部电影的演员。")
                    op = input('请输入要进行的操作')
                    if op == '&':
                        print(actOfAll(dict_data, ipt1, ipt2))
                    elif op == '|':
                        print(actOfBoth(dict_data, ipt1, ipt2))
                    elif op == '-':
                        print(actOfOne(dict_data, ipt1, ipt2))
                    elif op == '#':
                        break
                    else:
                        print("输入有误：只允许输入'&','|','-','#'中的一个。")
            else:  # 如果第二次输入了电影名
                checkActIpt(dict_data, ipt2)
        else:  # 如果第一次输入了电影名
            checkActIpt(dict_data, ipt1)
