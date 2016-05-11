promtForUser = "Pls, buy an elephant? Your reply is : "
userMustEnter = "OK"

user_input = input(promtForUser)

while user_input != userMustEnter:
    user_input = input("Everyone say " + user_input + " But you make a choice and " + promtForUser)
