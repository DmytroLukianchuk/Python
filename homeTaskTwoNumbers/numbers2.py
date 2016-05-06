__author__ = 'dmytrol'
print(
    "HomeWork#2: User enters number in range 20 - 99 from keyboard and get correct spelling of this number in console")

dict_units = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
              6: "six", 7: "seven", 8: "eight", 9: "nine"}

dict_dozens = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
               7: "seventy", 8: "eighty", 9: "ninety"}

user_input = input("Enter any number from 20 till 99 to know how it spells: ")

while not user_input.isdigit():
    user_input = input("You entered not a number. Enter any number from 20 till 99 to know how it spells: ")

while len(user_input) > 2:
    user_input = input("Your number is more than 99. Enter any number from 20 till 99 to know how it spells: ")

num_str_one, num_str_two = user_input

while num_str_one == '0' or num_str_one == '1':
    user_input = input("First entered number was 1 or 0. Enter any number from 20 till 99 to know how it spells: ")

if num_str_two == '0':
    spell_num = dict_dozens[int(num_str_one)]
else:
    spell_num = dict_dozens[int(num_str_one)] + " " + dict_units[int(num_str_two)]

print(spell_num)
