deck = ["AC", "AD", "AH", "AS", "2C", "2D", "2H", "2S", "3C", "3D", "3H", "3S", "4C", "4D", "4H", "4S",
        "5C", "5D", "5H", "5S", "6C", "6D", "6H", "6S", "7C", "7D", "7H", "7S", "8C", "8D", "8H", "8S",
        "9C", "9D", "9H", "9S", "TC", "TD", "TH", "TS", "JC", "JD", "JH", "JS", "QC", "QD", "QH", "QS",
        "KC", "KD", "KH", "KS"]


def shuffle():
    """shuffles deck"""
    print("deck shuffled")


def take_cards():
    """removes cards from deck and returns ten cards - five to hand and five to 'change'"""
    print("took five cards and five to change")


def analyze(cards):
    """analyzes cards and prints result of analysis"""
    print("analyzed and this is output: Hand: xxx Deck: yyy Best hand: zzz")
