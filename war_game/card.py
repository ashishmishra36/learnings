

# create a tuple(immovable)
suit = ('Club', 'Diamond', 'Spade', 'Hearts')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Ninth' , 'Tenth', 'Jack', 'Queen', 'King', 'Ace' )
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Ninth':9 , 'Tenth':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    def __init__(self,suit,rank ):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]


