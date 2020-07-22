from random import shuffle

class Card:
    suits = ['pik','kier','trefl','karo']
    values = [None, None, '2','3','4','5','6','7','8','9','10','walet','dama','krol','as']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self,other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return False
        return False

    def __repr__(self):
        return self.values[self.value] + " " + self.suits[self.suit]


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None


class Game:
    def __init__(self):
        name1 = input("Podaj imię pierwszego gracza: ")
        name2 = input("Podaj imię drugiego gracza: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = f"Tę rundę wygrał {winner}"
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = f'{p1n} wyciągnął {p1c}, {p2n} wyciągnął {p2c}'
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Start!')
        while len(cards) >= 2:
            m = "Wprowadź 'q', aby zakończyć. Wprowadź dowolny inny przycisk, aby kontynuować: "
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,self.p2)

        print(f"Koniec wojny. Wygrał {win}. Wynik:  {self.p1.wins} : {self.p2.wins}")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        if p1.wins == p2.wins:
            return "Remis!"

game = Game()
game.play_game()

