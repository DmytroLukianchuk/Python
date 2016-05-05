# a = float(input("Enter first number a = "))
# b = float(input("Enter second number b = "))
print("Home Work #1 - calc")

input_a = input("Enter first number a = ")

while not input_a.isdigit():
    print("a is not a number")
    input_a = input("Enter first number a = ")
else:
    a = float(input_a)

input_b = input("Enter second number b = ")
while not input_b.isdigit():
    print("b is not a number")
    input_b = input("Enter first number b = ")
else:
    b = float(input_b)

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
exponent = a ** b
floor_division = a // b
modulus = a % b


print("Calc operations: ")
print("a + b =", addition)
print("a - b =", subtraction)
print("a * b =", multiplication)
print("a / b =", division)
print("a ** b =", exponent)
print("a // b =", floor_division)
print("a % b =", modulus)
