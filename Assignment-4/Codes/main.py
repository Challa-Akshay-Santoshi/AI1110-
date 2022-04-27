# C. Akshay Santoshi
# CS21BTECH11012

# PROBABILITY

# Defining the number of cards in a deck
# Defining number of cards in a suit in a deck
# Defining number of face cards in each deck
Deck = 52
suit_cards = 13
facecard_suit = 3

# Red coloured cards are Diamonds and spades and equal number of kings, queens and jack
print(f"The probability of getting a king of red colour is ", 2*(facecard_suit/3)/Deck )

# There are 4 suits in a deck
print(f"The probability of getting a face card is ", 4*facecard_suit/Deck )

# Red coloured cards are Diamonds and spades
print(f"The probability of getting a red face card is ", 2*facecard_suit/Deck )

# Jack is a face card
print(f"The probability of getting the jack of hearts is ", (facecard_suit/3)/Deck )

# Spade is a suit in a deck of cards
print(f"The probability of getting a spade is ", suit_cards/Deck )

# Queen is a face card
print(f"The probability of getting the queen of diamonds is ", (facecard_suit/3)/Deck)