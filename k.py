import random

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print("Invalid number")
        name = None
    return name

def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print("Invalid option")
        number = -1
    return number

def rpsls(name):

    player_number = name_to_number(name)
    computer_numer = random.randrange(0, 5)
    difference = (player_number - computer_numer) % 5
    if (player_number == -1):
        winner = "Error"
    else:
        if difference == 0:
            winner = "It's a tie"
        elif difference == 1 or difference == 2:
            winner = "Player wins."
        elif difference == 3 or difference == 4:
            winner = "Computer wins."
    computer_name = number_to_name(computer_numer)
    print("Player chooses: %s" % name.title())
    print("Computer chooses: %s" % computer_name.title())
    print(winner)

rpsls(input("Choose Rock, Paper, Scissors, Lizard, or Spock: ").lower())