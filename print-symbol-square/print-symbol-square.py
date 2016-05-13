__author__ = 'dmytrol'
CHOOSE_SYMB = "Please enter ONE SYMBOL you wanna print your square with: "
CHOOSE_NUM = "Please enter width of square (NUMBER: 1 - 100): "
CHOOSE_NUM_AGAIN = "You entered not a number! Please enter width of square (NUMBER: 1 - 100): "
MORE_SYMBOLS = "You entered more than ONE symbol, so we've taken first one for u"


def print_symbol_scuare (size, symbol):
    row = size
    while row > 0:
        for i in range(0, size, 1):
            print(symbol, end="|")
        print()
        row -= 1


def ask_user():
    user_symb = input(CHOOSE_SYMB).split()[0][0]
    print(MORE_SYMBOLS)
    print()

    user_num = input(CHOOSE_NUM)
    while not user_num.isdigit():
        user_num = input(CHOOSE_NUM_AGAIN)
    return int(user_num), user_symb


print_symbol_scuare(*ask_user())
