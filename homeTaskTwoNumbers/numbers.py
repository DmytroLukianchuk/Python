print("HomeWork#2: User enters number in range 20 - 99 from keyboard and get correct spelling of this number in console")

dict_numbers = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
                "6": "six", "7": "seven", "8": "eight", "9": "nine", "ten": "ten",
                "twenty": "twenty", "thirty": "thirty", "forty": "forty", "fifty": "fifty", "sixty": "sixty",
                "seventy": "seventy", "eighty": "eighty", "ninety": "ninety"}

user_input = str(input("Enter any number from 20 till 99 to know how it spells: "))

user_num_one, user_num_two = user_input

while user_num_one == '0' or user_num_one == '1':
    user_input = str(input("First entered number was 1. Enter any number from 20 till 99 to know how it spells: "))
    user_num_one, user_num_two = user_input


print("first number was entered:", user_num_one)
print("second number was entered:", user_num_two)

if int(user_num_one) == 1 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['ten'])
    exit()
if int(user_num_one) == 2 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['twenty'])
    exit()
if int(user_num_one) == 3 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['thirty'])
    exit()
if int(user_num_one) == 4 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['forty'])
    exit()
if int(user_num_one) == 5 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['fifty'])
    exit()
if int(user_num_one) == 6 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['sixty'])
    exit()
if int(user_num_one) == 7 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['seventy'])
    exit()
if int(user_num_one) == 8 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['eighty'])
    exit()
if int(user_num_one) == 9 and int(user_num_two) == 0:
    print("spelling of your entered number is:", dict_numbers['ninety'])
    exit()

if int(user_num_one) == 2:
    num_word_one = dict_numbers['twenty']
if int(user_num_one) == 3:
    num_word_one = dict_numbers['thirty']
if int(user_num_one) == 4:
    num_word_one = dict_numbers['forty']
if int(user_num_one) == 5:
    num_word_one = dict_numbers['fifty']
if int(user_num_one) == 6:
    num_word_one = dict_numbers['sixty']
if int(user_num_one) == 7:
    num_word_one = dict_numbers['seventy']
if int(user_num_one) == 8:
    num_word_one = dict_numbers['eighty']
if int(user_num_one) == 9:
    num_word_one = dict_numbers['ninety']

if int(user_num_two) == 1:
    num_word_two = dict_numbers['1']
if int(user_num_two) == 2:
    num_word_two = dict_numbers['2']
if int(user_num_two) == 3:
    num_word_two = dict_numbers['3']
if int(user_num_two) == 4:
    num_word_two = dict_numbers['4']
if int(user_num_two) == 5:
    num_word_two = dict_numbers['5']
if int(user_num_two) == 6:
    num_word_two = dict_numbers['6']
if int(user_num_two) == 7:
    num_word_two = dict_numbers['7']
if int(user_num_two) == 8:
    num_word_two = dict_numbers['8']
if int(user_num_two) == 9:
    num_word_two = dict_numbers['9']

print("spelling of your entered number is:", num_word_one, num_word_two)