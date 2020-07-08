#    A programme that produces a number of randomly generated cards
#by: Caleb Otchi


from random import randrange, choice
class playCard:

    def __init__(self, rank , suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def Bjvalue(self):
        if self.rank == 1:
            self.Bj = 1
        elif 1 < self.rank < 10:
            self.Bj = self.rank - 1
        else:
            self.Bj = 10
        return self.Bj

    def __str__(self):
        rank_array = ["Ace", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "King", "Queen"]
        suit_dict = {"d":"Diamonds", "s":"Spades", "h":"Hearts", "c":"Clubs"}
        if 1 <= self.rank <= 13 and self.suit in suit_dict:
            return rank_array[self.rank - 1] + " of " + suit_dict[self.suit]

def main():
    print("This programme prints a number of randomly generated cards and their blackjack values.")
    f = eval(input("Please enter a number: "))
    letters = ["d", "s", "h", "c"]
    for i in range(f):
        card = playCard(randrange(1,14), choice(letters))
        bj = card.Bjvalue()
        print("Your card is", card, "and the blackjack value is", bj)

main()
