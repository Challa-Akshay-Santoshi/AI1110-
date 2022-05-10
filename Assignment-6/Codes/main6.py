# C. Akshay Santoshi
# CS21BTECH11012

# Defining probabilities of various events
A = 0.8
B = 0.5
BgivenA = 0.4

# Probability of A intersection B
AB = BgivenA * A
print(f"Probability of A intersection B is ", AB)

# Probability of A given B
AgivenB = AB/B
print(f"Probability of A given B is ", AgivenB)

# Probability of A union B
AunionB = A + B - AB
print(f"Probability of A union B is ", AunionB)