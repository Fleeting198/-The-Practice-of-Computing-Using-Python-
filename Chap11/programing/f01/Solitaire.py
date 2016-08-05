# -*- coding: utf-8 -*-

from Chap11.programing.f01.cards import *


def main():
    printIntroMessage()
    solitaire = Solitaire()
    while 1:
        solitaire.play()
        choice = input('是否要重新开始游戏? (y/n)')
        if choice.lower() == 'n':
            break


def printIntroMessage():
    print("游戏说明：\n"
          "目标：移动所有牌到Foundation牌组\n"
          "细节：\n"
          "  Foundation：\n"
          "    1. 每一组为从A到K顺序的同一花色\n"
          "    2. 可以移动顶层牌\n"
          "  Tableau：\n"
          "    1. 从K到A降序，颜色间隔排列\n"
          "    2. 可以移动顶层牌\n"
          "    3. 可以移动顺序正确或部分正确的牌组\n"
          "    4. 空牌位可以放任何牌或顺序正确的牌组\n"
          "  Stock：\n"
          "    1. 主牌堆\n"
          "操作：\n"
          "  1. 移动，格式：m <'t'/'f'><num>,<idFrom> <'t'/'f'><idTo>\n"
          "           't'代表tableau，'f'代表foundation，num为移动牌数，idFrom为来源牌组序号，idTo为目标牌组序号\n"
          "           例如：'m t2,3 f4' 从第三列tableau 移动两张顶牌到第四列foundaton\n"
          "                 'm t7,2 t4' 从第二列tableau 移动七张顶牌到第四列tableau\n"
          "  2. 发牌，输入'g'\n"
          "  3. 重新开始游戏，输入'r'\n")


class Solitaire():
    def __init__(self):
        self.mainDeck = Deck()
        self.foundation = [[] for i in range(5)]
        self.tableau = [[] for i in range(8)]

    def gameInit(self):
        self.mainDeck = Deck()
        self.mainDeck.shuffle()
        self.foundation = [[] for i in range(5)]
        self.tableau = [[] for i in range(8)]

        # 每个tableau发三张。牌堆最上，也就是队列最后的牌可见，其他所有隐藏
        for i in range(1, 8):
            stack = []
            for j in range(3):
                card = self.mainDeck.deal()
                # 前两张隐藏
                if j != 2:
                    card.set_hidden()
                stack.append(card)
            self.tableau[i] = stack

    def play(self):
        print('\n开始新游戏\n')
        self.gameInit()
        self.display()
        while 1:
            ipt = input('\n输入命令，m-移动，g-发牌，r-重新开始：')
            cmdID = self.getcmdID(ipt)
            if cmdID == 3:
                break
            if cmdID == 1:
                if not self.mainDeck.empty():
                    self.drawFromDeck()
                self.display()
            elif cmdID == 2:
                try:
                    move = self.Move(ipt)
                except self.Move.MoveInitError:
                    print("输入参数不符合格式，需要重新输入。")
                    continue

                if (move.type == 1 and self.moveBetweenTableau(move)) \
                        or (move.type == 2 and self.moveTableauToFoundation(move)) \
                        or (move.type == 3 and self.moveFoundationToTableau(move)) \
                        or (move.type == 4 and self.moveBetweenFoundation(move)):
                    self.display()
                    if self.checkIfWon():
                        print("恭喜！你赢了！游戏结束。")
                        break
                else:
                    print("移动错误，可能是参数超过了牌组数量，或者不满足移动要求。")
            else:
                print("没有该命令")

    def drawFromDeck(self):
        """从主牌堆中抽7张牌，各发一张到tableau最后，默认显示"""
        for i in range(1, 8):
            if self.mainDeck.empty():
                break
            self.tableau[i].append(self.mainDeck.deal())

    def tableauPrint(self):
        """输出 tableau中所有牌，隐藏以xx显示，否则显示牌号和花色"""
        maxTableauLen = max([len(cards) for cards in self.tableau])
        for i in range(0, maxTableauLen):
            print()
            for cardList in self.tableau:
                length = len(cardList)
                if length < i + 1:
                    print("    ", end='')
                else:
                    card = cardList[i]
                    print(str(" ") + card.__str__(), end='')

    def foundationString(self):
        """输出foundation，只显示顶部牌的信息"""
        foun = ""
        for found in self.foundation:
            if len(found) < 1:
                x = "  "
            else:
                x = found[-1].__str__()
            foun += str('  ') + x
        return foun

    def deckString(self):
        """返回牌堆字符串"""
        return "  " if self.mainDeck.empty() else "XX"

    def display(self):
        """输出牌局"""
        f = self.foundationString()
        d = self.deckString()
        print(d + str("  ") + str("   ") + f)
        self.tableauPrint()

    def checkIfWon(self):
        """判断胜利：所有foundation满"""
        for lst in self.foundation:
            if len(lst) != 13:
                return False
        return True

    def getcmdID(self, userInput):
        """返回用户输入对应的操作号，非法则为0"""
        dictUserIpt = {'g': 1, 'm': 2, 'r': 3}
        if not userInput or userInput[0] not in dictUserIpt:
            return 0
        userInput = userInput[0]
        x = dictUserIpt[userInput]
        return x

    def checkLegalPermutation(self, cards):
        """
        检查一组牌是否是正确的排列，要求底牌到顶牌颜色交错，级别逐一递减
        输入：一个数组，成员全是Card类
        输出：Ture，False
        """
        if len(cards) == 1: return True
        for i, card in enumerate(cards):
            if i == 0: continue
            if card.has_same_color(cards[i - 1]) or card.get_rank() != cards[i - 1].get_rank() - 1:
                return False
        return True

    def moveBetweenTableau(self, move):
        """从第 j 牌组移动 i 张牌到第 k 牌组"""
        if not self.checkBetweenTableau(move):
            return False

        i = move.numFrom
        j = move.colFrom
        k = move.colTo

        lst = self.tableau[j]
        lst2 = self.tableau[k]
        cardsToMove = lst[-i:]
        lst2.extend(cardsToMove)
        lst = lst[:-i]
        if lst:
            uncoveredCard = lst[-1]
            uncoveredCard.show_card()
        self.tableau[j] = lst

        return True

    def checkBetweenTableau(self, move):
        """检测：从第 j 牌组移动 i 张牌到第 k 牌组，若目标牌组栏空则只能放13，若不空则颜色须不同且值小一号"""
        i = move.numFrom
        j = move.colFrom
        k = move.colTo

        # 检查参数合法
        if j not in range(1, 8) or k not in range(1, 8) or i > len(self.tableau[j]) or not self.tableau[j]:
            return False

        cardsToMove = self.tableau[j][-i:]
        # 检查牌序正确
        if not self.checkLegalPermutation(cardsToMove):
            return False

        # 不能移动隐藏的牌
        for c in cardsToMove:
            if c.get_hidden():
                return False

        c = cardsToMove[0]
        rank = c.get_rank()
        if not self.tableau[k]:
            return True if rank == 13 else False
        else:
            receivingCard = self.tableau[k][-1]
            desiredRank = receivingCard.get_rank() - 1
            return True if not receivingCard.has_same_color(c) and rank == desiredRank else False

    def moveTableauToFoundation(self, move):
        """移动第 i 个tableau 最顶部的牌到第 j 个foundation"""
        if not self.checkTableauToFoundation(move):
            return False

        i = move.colFrom
        j = move.colTo

        lst = self.tableau[i]
        lst2 = self.foundation[j]
        movedCard = lst[-1]
        lst2.append(movedCard)
        lst = lst[:-1]
        if lst:
            uncoveredCard = lst[-1]
            uncoveredCard.show_card()
        self.tableau[i] = lst

        return True

    def checkTableauToFoundation(self, move):
        """检测：移动第 i 个tableau 最顶部的牌到第 j 个foundation，若空须为A，若不空必须同花色且级别大一级"""
        i = move.colFrom
        j = move.colTo

        if i not in range(1, 8) or j not in range(1, 5) or not self.tableau[i]:
            return False

        card = self.tableau[i][-1]
        rank = card.get_rank()
        suit = card.get_suit()

        # 若foundation 空，只能放A
        if not self.foundation[j]:
            return True if rank == 1 else False
        else:
            foundationCard = self.foundation[j][-1]
            desiredRank = foundationCard.get_rank() + 1

            return True if foundationCard.get_suit() == suit and desiredRank == rank else False

    def moveFoundationToTableau(self, move):
        """从第 i 个foundation 拿顶牌到第 j 个tableau"""
        if not self.checkFoundationToTableau(move):
            return False

        i = move.colFrom
        j = move.colTo

        lst = self.foundation[i]
        cardToMove = lst[-1]
        lst2 = self.tableau[j]
        lst2.append(cardToMove)
        lst = lst[:-1]
        self.foundation[i] = lst

        return True

    def checkFoundationToTableau(self, move):
        """检测：从第 i 个foundation 拿顶牌到第 j 个tableau，若目标牌组栏空则只能放13，若不空则颜色须不同且值小一号"""
        i = move.colFrom
        j = move.colTo

        # 检查参数合法
        if j not in range(1, 8) or i not in range(1, 5) or not self.foundation[i]:
            return False
        card = self.foundation[i][-1]
        rank = card.get_rank()

        if not self.tableau[j]:
            return True if rank == 13 else False
        else:
            receivingCard = self.tableau[j][-1]
            desiredRank = receivingCard.get_rank() - 1
            return True if not receivingCard.has_same_color(card) and rank == desiredRank else False

    def moveBetweenFoundation(self, move):
        """从第 i 个foundation 拿顶牌到第 j 个foundation"""
        if not self.checkBetweenFoundation(move):
            return False

        i = move.colFrom
        j = move.colTo

        lst = self.foundation[i]
        lst2 = self.foundation[j]
        cardToMove = lst[-1]
        lst2.append(cardToMove)
        lst = lst[:-1]
        self.foundation[i] = lst

        return True

    def checkBetweenFoundation(self, move):
        """从第 i 个foundation 拿顶牌到第 j 个foundation，若空只能放A，若不空不能放"""
        i = move.colFrom
        j = move.colTo

        if i not in range(1, 5) or j not in range(1, 5) or not self.foundation[i]:
            return False
        rank = self.foundation[i][-1].get_rank()
        # 若foundation 空，只能放A
        return True if self.foundation[j] and rank == 1 else False


    class Move:
        """移动指令类"""
        class MoveInitError(Exception):
            def __init__(self, args):
                self.args = args

        def __init__(self, string):
            try:
                m, f, t = str(string).strip().split(' ')
            except ValueError:
                raise self.MoveInitError("移动操作输入格式错误，例子'm t2,3 f1'。")

            if f[0] in "tf":
                self.posFrom = f[0]
            else:
                raise self.MoveInitError("移动来源错误，必须是 t(tableau) 或 f(foundation)。")

            if t[0] in "tf":
                self.posTo = t[0]
            else:
                raise self.MoveInitError("移动目标错误，必须是 t(tableau) 或 f(foundation)。")

            f = f[1:].split(',')
            t = t[1:]

            if len(f) == 2:
                try:
                    self.numFrom = int(f[0])
                    self.colFrom = int(f[1])
                except ValueError:
                    raise self.MoveInitError("移动来源错误，牌数量和牌组号必须为数字。")
            else:
                raise self.MoveInitError("移动来源错误，应用一个','隔开牌数量和牌组号这两个数字。")

            if len(t) == 1:
                try:
                    self.colTo = int(t)
                except ValueError:
                    self.MoveInitError("移动目标错误，牌组号必须为数字。")
            else:
                raise self.MoveInitError("移动目标错误，应只有一个数字代表牌组号。")

            # 判断类型
            if self.posFrom == 't' and self.posTo == 't':
                self.type = 1
            elif self.posFrom == 't' and self.posTo == 'f':
                self.type = 2
            elif self.posFrom == 'f' and self.posTo == 't':
                self.type = 3
            elif self.posTo == 'f' and self.posTo == 'f':
                self.type = 4
            else:
                self.type = 0

        def __str__(self):
            return str(self.posFrom) + str(self.numFrom) + str(self.colFrom) + str(self.posTo) + str(self.colTo)


if __name__ == '__main__':
    main()
