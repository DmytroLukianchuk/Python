__author__ = 'dmytrol'
import random
import re

BOAT_SIGN = '#'
MILK_SIGN = 'O'
HIT_SIGN = 'X'
PLAYER_USER = 'user'
PLAYER_MACHINE = 'machine'


def field_gen():
    field = [[" ", "A", "B", "C"],
             ["1", " ", " ", " "],
             ["2", " ", " ", " "],
             ["3", " ", " ", " "],
    ]
    return field


def print_field(f, boat_hidden):
    line = ' | '
    for row in f:
        line_join = line.join(row)
        if BOAT_SIGN in line_join and boat_hidden:
            line_join = re.sub(BOAT_SIGN, ' ', line_join)
        print(line_join, "|")
        print('*' * 15)


def user_set(f, sign):
    column = input("Enter a COLUMN (A, B or C): ").upper()
    while not column in ("A", "B", "C"):
        column = input("Enter a COLUMN (A, B or C): ").upper()
    row = input("Enter a ROW (1, 2 or 3): ")
    while not (row in ('1', '2', '3') and row.isnumeric()):
        row = input("Enter a ROW (1, 2 or 3): ")
    row = int(row)
    print()

    if column == 'A':
        column = 1
    elif column == 'B':
        column = 2
    elif column == "C":
        column = 3

    if f[row][column] == " ":
        f[row][column] = sign
    else:
        f[row][column] += sign

    for row in range(len(f)):
        for item in range(len(f)):
            while f[row][item] == sign * 2:
                f[row][item] = sign
                print("You've chosen already occupied spot! NOT GOOD!")
                while not column in ("A", "B", "C"):
                    column = input("Enter a COLUMN (A, B or C): ").upper()
                    row = input("Enter a ROW (1, 2 or 3): ")
                while not (row in ('1', '2', '3') and row.isnumeric()):
                    row = input("Enter a ROW (1, 2 or 3): ")
                row = int(row)
                print()

                if column == 'A':
                    column = 1
                elif column == 'B':
                    column = 2
                elif column == "C":
                    column = 3

                if f[row][column] == " ":
                    f[row][column] = sign
                else:
                    f[row][column] += sign
    return f


def machine_set(f, sign):
    machine_row = random.randint(1, 3)
    machine_column = random.randint(1, 3)

    while f[machine_row][machine_column] == MILK_SIGN:
        machine_row = random.randint(1, 3)
        machine_column = random.randint(1, 3)

    if f[machine_row][machine_column] == BOAT_SIGN:
        f[machine_row][machine_column] = HIT_SIGN

        if machine_column == 1:
            machine_column = 'A'
        elif machine_column == 2:
            machine_column = 'B'
        elif machine_column == 3:
            machine_column = 'C'

        print("Machine has chosen: " + machine_column + str(machine_row))
        print("BOOM! Machine has won!!!")
        print_field(f, False)
        exit()

    f[machine_row][machine_column] = sign

    if machine_column == 1:
        machine_column = 'A'
    elif machine_column == 2:
        machine_column = 'B'
    elif machine_column == 3:
        machine_column = 'C'

    if not sign == BOAT_SIGN:
        print("Machine has chosen: " + machine_column + str(machine_row))

    return f


def is_hit(f, player):
    for row in range(len(f)):
        for item in range(len(f)):
            if f[row][item] == BOAT_SIGN + MILK_SIGN:
                f[row][item] = HIT_SIGN
                print("BOOM!", player, "has hit")
                # print_field(f, True)
                print_field(f, False)
                quit()
            if f[row][item] == MILK_SIGN * 2:
                f[row][item] = MILK_SIGN
                return False
    return False


def game_turn(player, f_player):
    if player == PLAYER_USER:
        user_set(f_player, MILK_SIGN)
    else:
        machine_set(f_player, MILK_SIGN)

print("User's field: ")
f_user = field_gen()
print_field(f_user, False)
print()

print("Set up a boat: ")
user_set(f_user, BOAT_SIGN)
print_field(f_user, False)
print()

print("Machine has set up the boat. Try to guess where it is! :) ")
f_machine = field_gen()
machine_set(f_machine, BOAT_SIGN)
print()

print("Game Began!")
print("*" * 15)

while True:
    print("Shoot the enemy: ")
    game_turn(PLAYER_USER, f_machine)

    if not is_hit(f_machine, PLAYER_USER):
        print("MILK! Machine's field")
        # print_field(f_machine, True)
        print_field(f_machine, False)

    print()
    print("Enemy shoots you: ")
    game_turn(PLAYER_MACHINE, f_user)

    # print("Check if won: ")
    if not is_hit(f_user, PLAYER_MACHINE):
        print()
        print("MILK! Your field")
        print_field(f_user, False)
