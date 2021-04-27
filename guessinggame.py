import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin)

    Function will continue looping, and prompting the user, until a valid 'int' is entered.

    :param prompt: The String that the user sees when they're prompted to
        enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Invalid entry. Please enter a number.")


highest = 1000
answer = random.randint(1, highest)
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        print("Game over. You have quit.")
        break
    elif guess < answer:
        print("Please guess higher: ")
    else:
        print("Please guess lower")
if guess == answer:
    print("Congrats, you got it!")



