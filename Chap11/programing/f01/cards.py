import random  # needed for shuffling a Deck


class Card(object):
    """Denote a card with rank and suit"""

    # Protocol:
    #   1. 'no card' is represented by BOTH r = 0 and s = ''
    #   2. set_rank and set_suit should be commented out after development and debugging
    #   3  rank is int: 1=Ace, 2-10 face value, 11=Jack, 12=Queen, 13=King
    def __init__(self, r=0, s=''):
        self.__rank = 0
        self.__suit = ''  # create blank card by default unless we fix it later
        self.__hidden = False
        if type(r) == str:
            if r in 'Jj':
                self.__rank = 11  # Jack
            elif r in 'Qq':
                self.__rank = 12  # Queen
            elif r in 'Kk':
                self.__rank = 13  # King
            elif r in 'aA':
                self.__rank = 1  # Ace
                # else str rank not in the approved set, keep the default rank of 0
        elif type(r) == int:
            if 1 <= r <= 13:
                self.__rank = r
                # else int rank not between 1 and 14, keep the default rank of 0
        # else rank not a str or an int, keep the default rank of 0
        if type(s) == str and s:
            if s in 'Cc':
                self.__suit = 'C'
            elif s in 'Hh':
                self.__suit = 'H'
            elif s in 'Dd':
                self.__suit = 'D'
            elif s in 'Ss':
                self.__suit = 'S'
                # else suit not in approved set, keep the default suit of ''
                # else suit not a string, keep the default suit of ''

    def has_same_color(self, other):
        s1 = self.get_suit()
        s2 = other.get_suit()
        if s1 == 'D' or s1 == 'H':
            s1 = 0
        else:
            s1 = 1
        if s2 == 'D' or s2 == 'H':
            s2 = 0
        else:
            s2 = 1
        return s1 == s2

    def set_hidden(self, val=True):
        """Set the card's hidden value, default True"""
        self.__hidden = val

    def get_hidden(self):
        """Retrieve the card's hidden value"""
        return self.__hidden

    def show_card(self):
        """Set the card as a non-hidden card"""
        self.__hidden = False

    def set_rank(self, r):
        """For Development and Debugging only: Set the rank of the card: 0-13"""
        self.__rank = r

    def set_suit(self, s):
        """For Development and Debugging only: Set the suit of the card: C,S,D,H"""
        self.__suit = s

    def get_rank(self):
        """Return rank of the card as int: 0-13"""
        return self.__rank

    def get_suit(self):
        """Return suit of the card as string: C,S,D,H"""
        return self.__suit

    def get_value(self):
        """Get the value on the face card:
           (Jack, Queen, King = 10), Ace = 1, others are face value 2-10"""
        if self.__rank <= 10:
            return self.__rank
        else:
            return 10  # Only Jack, Queen or King remain; their value is 10

    def __str__(self):
        """String representation of card for printing: rank + suit,
           e.g. 7S or JD, 'blk' for 'no card'"""
        if self.__hidden:
            return "XX".rjust(3)
        else:
            nameString = "blk A 2 3 4 5 6 7 8 9 10 J Q K"  # 'blk' for blank, i.e. no card
            nameList = nameString.split()  # create a list of names so we can index into it using rank

            # put name and suit in 3-character-wide field, right-justified
            return (nameList[self.__rank] + self.__suit).rjust(3)

    def __repr__(self):
        """Representation of card: rank + suit"""
        return self.__str__()


class Deck(object):
    """Denote a deck to play cards with"""

    def __init__(self):
        """Initialize deck as a list of all 52 cards: 13 cards in each of 4 suits"""
        self.__deck = [Card(j, i) for i in "CSHD" for j in range(1, 14)]  # list comprehension

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)  # random.shuffle() randomly rearranges a sequence

    def deal(self):
        """Deal a card by returning the card that is removed off the top of the deck"""
        if len(self.__deck) == 0:  # deck is empty
            return None
        else:
            return self.__deck.pop(0)  # remove card (pop it) and then return it

    def discard(self, n):
        """Remove n cards from the top of the deck"""
        del self.__deck[:n]  # delete an n-card slice from the end of the deck list

    def top(self):
        """Return the value of the top card -- do not remove from deck."""
        if len(self.__deck) == 0:  # deck is empty
            return None
        else:
            return self.__deck[0]

    def bottom(self):
        """Return the value of the bottom card -- do not remove from deck."""
        if len(self.__deck) == 0:  # deck is empty
            return None
        else:
            return self.__deck[-1]

    def add_card_top(self, c):
        """Place card c on top of deck"""
        self.__deck = [c] + self.__deck

    def add_card_bottom(self, c):
        """ Place card c on the bottom of the deck"""
        self.__deck.append(c)

    def cards_left(self):
        """Return number of cards in deck"""
        return len(self.__deck)

    def empty(self):
        """Return True if the deck is empty, False otherwise"""
        return len(self.__deck) == 0

    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
        s = ""
        for index, card in enumerate(self.__deck):
            if index % 13 == 0:  # insert newline: print 13 cards per line
                s += "\n"
            s += str(card) + " "
        return s

    def __repr__(self):
        """Representation of deck"""
        return self.__str__()
