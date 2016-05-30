__author__ = 'dmytrol'
import random

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


def print_field(f):
    line = ' | '
    for row in f:
        print(line.join(row), "|")
        print('*' * 15)


def print_field_for_user(f):
    line = ' | '
    for i in range(len(f)):
        for j in range(len(f)):
            if f[i][j] == BOAT_SIGN:
                f[i][j] = " "

    for row in f:
        print(line.join(row), "|")
        print('*' * 15)

    return f


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
                column = input("Enter a COLUMN (A, B or C): ").upper()
                row = int(input("Enter a ROW (1, 2 or 3): "))
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
    machine_column = random.randint(1, 3)
    machine_row = random.randint(1, 3)

    if f[machine_row][machine_column] == " ":
        f[machine_row][machine_column] = sign
    else:
        f[machine_row][machine_column] += sign

    if machine_column == 1:
        machine_column = 'A'
    elif machine_column == 2:
        machine_column = 'B'
    elif machine_column == 3:
        machine_column = 'C'

    if not sign == BOAT_SIGN:
        print("Machine has chosen: " + machine_column + str(machine_row))

    for row in range(len(f)):
        for item in range(len(f)):
            while f[row][item] == sign * 2:
                f[row][item] = sign
                print("Machine has chosen already occupied spot! NOT GOOD!. Trying again...")
                machine_column = random.randint(1, 3)
                machine_row = random.randint(1, 3)

                if f[machine_row][machine_column] == " ":
                    f[machine_row][machine_column] = sign
                else:
                    f[machine_row][machine_column] += sign

                if machine_column == 1:
                    machine_column = 'A'
                elif machine_column == 2:
                    machine_column = 'B'
                elif machine_column == 3:
                    machine_column = 'C'
                print("Machine has chosen: " + machine_column + str(machine_row))
    return f


def is_hit(f, player):
    for row in range(len(f)):
        for item in range(len(f)):
            if f[row][item] == BOAT_SIGN + MILK_SIGN:
                f[row][item] = HIT_SIGN
                print("BOOM!", player, "has hit")
                print_field_for_user(f)
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
print_field(f_user)
print()

print("Set up a boat: ")
user_set(f_user, BOAT_SIGN)
print_field(f_user)
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
        print_field_for_user(f_machine)

    print()
    print("Enemy shoots you: ")
    game_turn(PLAYER_MACHINE, f_user)

    # print("Check if won: ")
    if not is_hit(f_user, PLAYER_MACHINE):
        print()
        print("MILK! Your field")
        print_field(f_user)
