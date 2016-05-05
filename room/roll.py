__author__ = 'dmytrol'
import math


room_w = float(input("room_w = "))
room_l = float(input("room_l = "))
room_h = float(input("room_w = "))

roll_w = float(input("roll_w = "))
roll_l = float(input("roll_l = "))

roll_count = 0

room_for_roll = room_w * room_h * 2 + room_l * room_h * 2

roll_count = room_for_roll // (roll_l * roll_w)

# roll_count = math.ceil(roll_count)

if roll_count % 1 == 0:
    pass
else:
    roll_count = int(roll_count) + 1

print("You need to buy", int(roll_count), "rolls!")


