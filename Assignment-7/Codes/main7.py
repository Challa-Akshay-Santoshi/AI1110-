# C. Akshay Santoshi
# CS21BTECH11012

# Deck contains 52 cards.
Deck = 52
spades =13
hearts = 13
clubs = 13
diamonds = 13
Kings = 4
Queen = 4
Jack = 4
Ace = 4

# Probability that the card drawn is a spade
E1 = spades/Deck

# Probbility that the card drawn is an ace
F1 = Ace/Deck

# Probability of the card drawn being an ace of a spade
E1F1 = 1/Deck

# To check whether the events are independent
if ( E1F1 == E1*F1): print("E and F are independent events")
else: print("E and F are dependent events")

# Probability that the card drawn is black
E2 = (clubs + hearts)/Deck

# Probability that the card drawn is a king
F2 = Kings/Deck

# Probability that the card drawn is a king belonging to a black card
E2F2 = 1/Deck + 1/Deck

# To check whether the events are independent
if ( E2F2 == E2*F2): print("E and F are independent events")
else: print("E and F are dependent events")

# Probability that the card drawn is king or queen
E3 = (Kings + Queen)/Deck

# Probability that the card drawn is queen or Jack
F3 = (Queen + Jack)/Deck

# Probability that the card drawn is queen
E3F3 = Queen/Deck

# To check whether the events are independent
if ( E3F3 == E3*F3): print("E and F are independent events")
else: print("E and F are dependent events")