
while True:

    try:

        my_num = int(input("Enter an integer"))
        print("Your number is ", my_num)

    except ValueError:
        print("Please enter an integer")