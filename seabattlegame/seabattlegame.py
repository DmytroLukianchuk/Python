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


def machine_set(f, sign):
    machine_row = random.randint(1, 3)
    machine_column = random.randint(1, 3)

    while f[machine_row][machine_column] == MILK_SIGN:
        if machine_column == 1:
            machine_column = 'A'
        elif machine_column == 2:
            machine_column = 'B'
        elif machine_column == 3:
            machine_column = 'C'
        print("Machine has chosen: " + machine_column + str(machine_row))
        print("ALERT! OCCUPIED SPOT! NOT GOOD! TRY AGAIN!")
        print()
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
    
    while f[row][column] == MILK_SIGN:
        if column == 1:
            column = 'A'
        elif column == 2:
            column = 'B'
        elif column == 3:
            column = 'C'
        print("ALERT! OCCUPIED SPOT! NOT GOOD! TRY AGAIN!")
        column = input("Enter a COLUMN (A, B or C): ").upper()
        while not column in ("A", "B", "C"):
            column = input("Enter a COLUMN (A, B or C): ").upper()
            if column == 'A':
                column = 1
            elif column == 'B':
                column = 2
            elif column == "C":
                column = 3
        row = input("Enter a ROW (1, 2 or 3): ")
        while not (row in ('1', '2', '3') and row.isnumeric()):
            row = input("Enter a ROW (1, 2 or 3): ")
        row = int(row)
        if column == 'A':
            column = 1
        elif column == 'B':
            column = 2
        elif column == "C":
            column = 3

        print()

    if f[row][column] == BOAT_SIGN:
        f[row][column] = HIT_SIGN

        if column == 1:
            column = 'A'
        elif column == 2:
            column = 'B'
        elif column == 3:
            column = 'C'

        print("BOOM! YOU have just won!!!")
        print_field(f, False)
        exit()

    f[row][column] = sign

    return f

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
    user_set(f_machine, MILK_SIGN)
    print("MACHINE FIELD")
    print_field(f_machine, True)
    print("MILK!!!")

    print()
    print("Enemy shoots you: ")
    machine_set(f_user, MILK_SIGN)
    print("MILK!!!")

    print()
    print("USER FIELD")

    print_field(f_user, False)
