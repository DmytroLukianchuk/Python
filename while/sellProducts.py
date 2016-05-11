YOUR_REPLY_IS_ = " Your reply is (enter OK for buying) : "
dict_prodcuts = {1: "Book", 2: "Notebook", 3: "Lamp"}

promtForUser = "Pls, buy an " + dict_prodcuts[1] + "?" + YOUR_REPLY_IS_
userMustEnter = "OK"

user_input = input(promtForUser)

while user_input != userMustEnter:
    user_input = input("Everyone say " + user_input + " But you make a choice and " + promtForUser)
print("Thanks, you've bought the " + dict_prodcuts[1])

promtForUser = "Pls, buy an " + dict_prodcuts[2] + "?" + YOUR_REPLY_IS_
user_input = input(promtForUser)

while user_input != userMustEnter:
    user_input = input("Everyone say " + user_input + " But you make a choice and " + promtForUser)
print("Thanks, you've bought the " + dict_prodcuts[2])

promtForUser = "Pls, buy an " + dict_prodcuts[3] + "?" + YOUR_REPLY_IS_
user_input = input(promtForUser)

while user_input != userMustEnter:
    user_input = input("Everyone say " + user_input + " But you make a choice and " + promtForUser)
print("Thanks, you've bought the " + dict_prodcuts[3])

print("So, you've bought :", dict_prodcuts[1], dict_prodcuts[2], dict_prodcuts[3])

