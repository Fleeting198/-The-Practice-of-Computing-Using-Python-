# -*- coding:utf-8 -*-
# !/usr/bin/python
"""电子表格"""
import csv
from prettytable import PrettyTable


class simpleCSVClient:
    def __init__(self):
        self.titles = []
        self.data = []
        self.sourceFileName = ""

    def readFile(self, fileName, hasTitle=True):
        """读取csv文件"""
        data = []
        try:
            with open(fileName, 'r') as dataFile:
                csvReader = csv.reader(dataFile)
                for line in csvReader:
                    data.append(line)
            self.sourceFileName = fileName
        except FileNotFoundError:
            print('找不到文件：' + fileName)

        if hasTitle:
            self.titles = data[0]
            self.data = data[1:]
        else:
            self.titles = range(len(data[0]) + 1)[1:]
            self.data = data

    def save(self, fileName=''):
        """保存到源文件中"""
        if len(fileName) == 0:
            fileName = self.sourceFileName

        with open(fileName, 'w') as toFile:
            csvWriter = csv.writer(toFile)
            csvWriter.writerow(self.titles)
            for line in self.data:
                csvWriter.writerow(line)

    def printData(self):
        """用PrettyTable显示数据"""
        table = PrettyTable()
        # 设置列名
        table.field_names = self.titles

        # 加入每行数据到PrettyTable中
        for line in self.data:
            table.add_row(line)

        print(table)

    def delRow(self, rowID):
        """删除行，序号从1开始"""
        if self.isWithinTable(rowID=rowID):
            del self.data[rowID - 1]
            return True
        else:
            return False

    def delCol(self, colID):
        """删除列，序号从1开始"""
        if self.isWithinTable(colID=colID):
            del self.titles[colID - 1]
            for line in self.data:
                del line[colID - 1]
            return True
        else:
            return False

    def editCell(self, rowID, colID, content):
        """修改单元格"""
        if self.isWithinTable(rowID=rowID, colID=colID):
            self.data[rowID - 1][colID - 1] = str(content)
            return True
        else:
            return False

    def insertRow(self, rowID):
        """插入空行，序号从1开始，在第i行插入"""
        if self.isWithinTable(rowID=rowID, inserting=True):
            newLine = [''] * len(self.data[0])
            self.data.insert(rowID - 1, newLine)
            return True
        else:
            return False

    def insertCol(self, colID):
        """插入空列，序号从1开始"""
        if self.isWithinTable(colID=colID, inserting=True):
            self.titles.insert(colID - 1, ' ')
            for line in self.data:
                line.insert(colID - 1, '')
            return True
        else:
            return False

    def isWithinTable(self, rowID=1, colID=1, inserting=False):
        """检查行列值是否在表的数据区内，从1开始记"""
        i = 1 if inserting else 0
        if rowID < 1 or rowID > len(self.data) + i:
            print("行超出范围。")
            return False

        if colID < 1 or colID > len(self.data[0]) + i:
            print("列超出范围。")
            return False
        return True


if __name__ == '__main__':

    curCSVFile = simpleCSVClient()
    msgHelp = "usage:\n" \
              "    print this message: -help/-h/-?\n" \
              "    open file: -o/-open <path>\n" \
              "    delete row: -d/-delete -r/-row <rowID>\n" \
              "    delete col: -d/-delete -c/-col <colID>\n" \
              "    insert row: -i/-insert -r/-row <rowID>\n" \
              "    insert col: -i/-insert -c/-col <colID>\n" \
              "    edit cell: -e/-edit <rowID> <colID> <content>\n" \
              "    print table: -p/-print\n" \
              "    save to file: -s/-save [path]\n"

    while 1:
        command = input("请输入操作：")
        allCommands = {'help': ('-help', '-h', '-?'),
                       'open': ('-o', '-open'),
                       'delete': ('-d', '-delete'),
                       'row': ('-r', '-row'),
                       'col': ('-c', '-col'),
                       'insert': ('-i', '-insert'),
                       'edit': ('-e', '-edit'),
                       'save': ('-s', '-save'),
                       'print': ('-p', '-print')
                       }

        commands = command.split(' ')

        if commands[0] in allCommands['help']:
            print(msgHelp)
        elif commands[0] in allCommands['open']:
            fileName = commands[1]
            curCSVFile.readFile(fileName)

        elif commands[0] in allCommands['delete']:
            if commands[1] in allCommands['row']:
                rowID = int(commands[2])
                curCSVFile.delRow(rowID)

            elif commands[1] in allCommands['col']:
                colID = int(commands[2])
                curCSVFile.delCol(colID)

        elif commands[0] in allCommands['insert']:
            if commands[1] in allCommands['row']:
                rowID = int(commands[2])
                print(rowID)
                curCSVFile.insertRow(rowID)

            elif commands[1] in allCommands['col']:
                colID = int(commands[2])
                curCSVFile.insertCol(colID)

        elif commands[0] in allCommands['edit']:
            rowID = int(commands[1])
            colID = int(commands[2])
            content = commands[3]
            curCSVFile.editCell(rowID, colID, content)
        elif commands[0] in allCommands['save']:
            if len(commands) == 1:
                curCSVFile.save()
            else:
                fileName = commands[1]
                curCSVFile.save(fileName)
        elif commands[0] in allCommands['print']:
            curCSVFile.printData()
        else:
            print("Unknown command. Check help by '-help'.\n")
