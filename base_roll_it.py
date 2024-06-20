# checks users enter yes (y) or no (n)

def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

def instruction():
    print('''
    
    **** Instructions ****
    
    To begin, decide on a score goal (eg: The first one to get a score of 50 wins).
    
    For each round of the game, you win points by rolling dice. 
    The winner of the round is the one who gets 13 (or slightly less.)
    
    If you win the round, then your score will increase by the
    number of points that you earned. If your first roll of two
    dice is a double (eg: both dice show a three), then your score will be DOUBLE the number of points.
    
    If you lose the round
    Do something
    and then do something else
    etc
    
    ''')



# Checks that users enter an integer
# that is more than 13
def int_check():

    while True:

        error = "Please enter an integer that is 13 or more"

        try:

            response = int(input("Enter an integer"))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


print("🎲🎲 Roll it 13 🎲🎲")

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

print()
target_score = int_check()