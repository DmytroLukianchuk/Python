__author__ = 'dmytrol'
print(
    "HomeWork#2: User enters number in range 1 - 999 from keyboard and get correct spelling of this number in console")

dict_units = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
              6: "six", 7: "seven", 8: "eight", 9: "nine"}

dict_dozens = {0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
               7: "seventy", 8: "eighty", 9: "ninety"}

dict_bad = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
            17: "seventeen", 18: "eighteen", 19: "nineteen"}

user_input = input("Enter any number from 1 till 999 to know how it spells: ")

while not user_input.isdigit():
    user_input = input("You entered not a number. Enter any number from 1 till 999 to know how it spells: ")

while len(user_input) > 3:
    user_input = input("Your number is more than 999. Enter any number from 1 till 999 to know how it spells: ")

user_input = int(user_input)

lastTwo = user_input % 100

units_num = dict_units[user_input % 10]
user_input //= 10

dozen_num = dict_dozens[user_input % 10]
user_input //= 10

hundred_num = dict_units[user_input % 10]

if hundred_num == "one":
    spell_hundred_num = hundred_num + " hundred "
elif hundred_num == "":
    spell_hundred_num = ""
else:
    spell_hundred_num = hundred_num + " hundreds "

if 10 < lastTwo < 20:
    print(spell_hundred_num + dict_bad[lastTwo])
else:
    print("Spelling of entered number is: " + spell_hundred_num + dozen_num + " " + units_num)