__author__ = 'dmytrol'
print(
    "HomeWork#2: User enters number in range 20 - 99 from keyboard and get correct spelling of this number in console")

dict_units = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
              6: "six", 7: "seven", 8: "eight", 9: "nine"}

dict_dozens = {0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
               7: "seventy", 8: "eighty", 9: "ninety"}

user_input = input("Enter any number from 20 till 999 to know how it spells: ")

while not user_input.isdigit():
    user_input = input("You entered not a number. Enter any number from 20 till 99 to know how it spells: ")

while len(user_input) > 3:
    user_input = input("Your number is more than 999. Enter any number from 20 till 99 to know how it spells: ")

user_input = int(user_input)

units_num = user_input % 10
user_input = user_input // 10

dozen_num = user_input % 10
user_input = user_input // 10

hundred_num = user_input % 10

if (hundred_num != 0):
    spell_hundred_num = dict_units[hundred_num] + " hundreds "
else:
    spell_hundred_num = ""

if (hundred_num == 1):
    spell_hundred_num = dict_units[hundred_num] + " hundred "

print(spell_hundred_num + dict_dozens[dozen_num] + " " + dict_units[units_num])



