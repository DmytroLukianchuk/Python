ASK_USER = "Pls, buy a "
dict_prodcuts = {1: "Book", 2: "Notebook", 3: "Lamp", 4: "Cap"}
YOUR_REPLY_IS_ = " Your reply is (enter OK for buying) : "
userMustEnter = "OK"
userMustEnterList = ["OK", "GOOD"]

def askUserToBuyProduct(product):
    promtForUser = ASK_USER + dict_prodcuts[product] + "?" + YOUR_REPLY_IS_
    user_input = input(promtForUser)
    # while user_input != userMustEnter:
    while user_input not in userMustEnterList:
        user_input = input("Everyone say " + user_input + " But you make a choice and " + promtForUser)
    print("Thanks, you've bought the " + dict_prodcuts[product].upper())
    print("")

for product in dict_prodcuts:
    askUserToBuyProduct(product)


# for product in dict_prodcuts:
#     print("So, you've bought :", dict_prodcuts[product].upper())

products_str = ""
for prod in dict_prodcuts.values():
    products_str += prod + ", "
print(products_str[:-2])

print("So, you've bought :", ", ".join(dict_prodcuts.values()))

