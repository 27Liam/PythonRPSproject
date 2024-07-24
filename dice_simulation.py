import random

# generates an integer between 0 and 6
# to simulate a roll of a die

def roll_die():
    result = random.randint(1, 6)
    return result

# Main Routine starts here

user_score = 0
double_score="no"

# roll two dice
roll_1 = roll_die()
roll_2 = roll_die()

# check if we have a double score opportunity