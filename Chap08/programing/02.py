# -*- coding:utf-8 -*-
# !/usr/bin/python
"""元数据：组织iTunes"""
from prettytable import PrettyTable


def getDataFromFile(fileName):
    dictSongs = {}
    with open(fileName, 'r') as sourceFile:
        for line in sourceFile:
            try:
                name, time, artist, album, genre, plays = line.strip().split('\t')
            except ValueError:
                continue
            dictSongs[name] = {'time': time,
                               'artist': artist,
                               'album': album,
                               'genre': genre,
                               'plays': int(plays)}
    return dictSongs


def printSongs(songs, listName=()):
    table = PrettyTable()
    table.field_names = ['Name', 'Time', 'Artist', 'Album', 'Genre', 'Plays']

    if len(listName) == 0:
        listName = songs.keys()

    for name in listName:
        table.add_row((name, songs[name]['time'], songs[name]['artist'], songs[name]['album'], songs[name]['genre'],
                       songs[name]['plays']))
    print(table)


def minToSec(strMin):
    """把分钟格式的时间描述改为秒数"""
    strMin = str(strMin)
    iSemi = strMin.find(':')
    iSec = int(strMin[:iSemi]) * 60 + int(strMin[iSemi + 1:])

    return iSec


if __name__ == '__main__':
    songs = getDataFromFile('itunesSongs.txt')
    printSongs(songs)

    while 1:
        command = input("请选择操作（数字）：\n"
                        "1.名字：列出指定艺术家的所有曲目。\n"
                        "2.专辑：列出所有指定专辑的曲目。\n"
                        "3.类型：列出所有指定流派的曲目。\n"
                        "4.添加：添加一个曲目。\n"
                        "5.删除：删除指定的乐曲（给出其名称）。\n"
                        "6.流行：找到收藏中曲目最多的艺术家。\n"
                        "7.最长：找到收藏中最长的曲目。")
        if command == '1':
            artist = input("请输入艺术家的名字：")
            listName = []
            for k, v in songs.items():
                if v['artist'] == artist:
                    listName.append(k)
            printSongs(songs, listName)

        elif command == '2':
            album = input("请输入专辑名：")
            listName = []
            for k, v in songs.items():
                if v['album'] == album:
                    listName.append(k)
            printSongs(songs, listName)

        elif command == '3':
            genre = input("请输入类型：")
            listName = []
            for k, v in songs.items():
                if v['genre'] == genre:
                    listName.append(k)
            printSongs(songs, listName)

        elif command == '4':
            name = input("请输入要加入的曲目名字：")
            if name in songs:
                print("列表中已有此曲目。")
                continue

            artist = input("请输入艺术家的名字：")
            album = input("请输入专辑名：")
            genre = input("请输入类型：")

            songs[name] = {'time': '', 'artist': artist, 'album': album, 'genre': genre, 'plays': 0}

        elif command == '5':
            name = input("请输入要删除的曲目的名称：")
            del songs[name]

        elif command == '6':
            dictArtists = {}
            for k, v in songs.items():
                if v['artist'] in dictArtists:
                    dictArtists[v['artist']] += 1
                else:
                    dictArtists[v['artist']] = 0

            maxNum = 0
            maxKey = ''
            for k, v in dictArtists.items():
                if v > maxNum:
                    maxNum = v
                    maxKey = k

            print("收藏中曲目最多的艺术家是：", maxKey)

        elif command == '7':
            listTime = []
            for k, v in songs.items():
                listTime.append([k, minToSec(v['time'])])
                listTime.sort(key=lambda x: x[1], reverse=True)

            for i in range(len(listTime)):
                name = listTime[i][0]
                del listTime[i]
                listTime.insert(i,name)

            printSongs(songs,[listTime[0]])

        else:
            print("不存在的指令。")
