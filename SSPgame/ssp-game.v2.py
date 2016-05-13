import random

CHOOSE_ONE = "Scissors (SC), Stone (ST), Paper (P): "
user_won_round = "User Won This Round"
machine_won_round = "Machine Won This Round"
draw = "Draw in This Round"
dict_values = {1: "SC", 2: "ST", 3: "P"}
dict_values_long = {1: "SCISSORS", 2: "STONE", 3: "PAPER"}
dict_win_comb = {"SCISSORS": "PAPER", "STONE": "SCISSORS", "PAPER": "STONE"}

user_score = 0
machine_score = 0
game_round = 1


def who_won(machine_selection, user_selection):
    if machine_selection == user_selection:
        return draw
    elif dict_win_comb[dict_values_long[machine_selection]] == dict_values_long[user_selection]:
        return machine_won_round
    else:
        return user_won_round


def ask_user():
    user_entered = input(CHOOSE_ONE).upper()
    while user_entered not in dict_values.values():
        user_entered = input(CHOOSE_ONE).upper()

    if user_entered == dict_values[1]:
        user_number = 1
    elif user_entered == dict_values[2]:
        user_number = 2
    else:
        user_number = 3
    return user_number


def machine_selection():
    return random.randint(1, 3)


def update_score():
    global machine_score, user_score, game_round
    if winner == machine_won_round:
        machine_score += 1
        game_round += 1
    elif winner == user_won_round:
        user_score += 1
        game_round += 1
    elif winner == draw:
        game_round += 1


def print_results():
    print()
    print("MACHINE:", machine_score, "|", "USER:", user_score)
    print()


def print_round():
    print("ROUND", game_round)

end_of_game = input("Enter End Of Game Score from 1 till 5: ")
while not end_of_game.isdigit():
    end_of_game = input("You entered not a number. Enter End Of Game Score from 1 till 5: ")
end_of_game = int(end_of_game)
print("Let the Game Begin")
print()

while end_of_game != machine_score or end_of_game != user_score:
    print_round()

    machine_select = machine_selection()
    user_select = ask_user()

    print("Machine selected:", dict_values_long[machine_select])
    print("You selected:", dict_values_long[user_select])

    winner = who_won(machine_select, user_select)
    print(winner)

    update_score()
    print_results()
    print("********************")

    if machine_score == end_of_game or user_score == end_of_game:
        print("Game Over, baby!", winner, "from", game_round - 1, "attempt")
        break