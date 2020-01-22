now_money = 550
now_water: int = 400
now_milk = 540
now_beans = 120
now_cups: int = 9


def machine_has():
    print("The coffee machine has:")
    print(now_water, "of water")
    print(now_milk, "of milk")
    print(now_beans, "of coffee beans")
    print(now_cups, "of disposable cups")
    print("$" + str(now_money) + " of money\n")
    return


def coffee_by_type(money, water, beans, milk):
    global now_money
    global now_water
    global now_milk
    global now_beans
    global now_cups
    more_cups = min(now_water // water, now_beans // beans, now_milk // (milk if milk > 0 else 1), now_cups)
    if more_cups > 0:
        now_money += money
        now_water -= water
        now_milk -= milk
        now_beans -= beans
        now_cups -= 1
        print("I have enough resources, making you a coffee!\n")
        return now_money, now_water, now_milk, now_beans, now_cups
    else:
        not_enough(more_cups, now_water, now_milk, now_beans, now_cups, water, milk, beans)


def not_enough(more_cups, now_water, now_milk, now_beans, now_cups, water, milk, beans):
    while more_cups < 1:
        if now_water // water == 0:
            resource = "water"
        elif now_milk // (milk if milk > 0 else milk == 1) == 0:
            resource = "milk"
        elif now_beans // beans == 0:
            resource = "coffee beans"
        elif now_cups == 0:
            resource = "cups"
        return print("Sorry, not enough " + resource + "!\n")


def coffee_buy(coffee_choice):
    if coffee_choice == "1":
        coffee_by_type(4, 250, 16, 0)
    elif coffee_choice == "2":
        coffee_by_type(7, 350, 20, 75)
    elif coffee_choice == "3":
        coffee_by_type(6, 200, 12, 100)
    elif coffee_choice == "back":
        return
    return


i = 0
while i < 10:
    action_choice = input(print("Write action (buy, fill, take, remaining, exit): "))
    actions = ["buy", "fill", "take", "remaining", "exit"]
    # while action_choice is not False:  # while action_choice is True:for i in range(len(actions)):
    if action_choice.lower() == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        # coffee_choice = input()
        # coffee_types = ["1", "2", "3", "back"]
        # if coffee_choice in coffee_types:
        coffee_buy(input())
        continue
        # elif coffee_choice == "back":
        #    continue
        # else:
        #    print("Wrong type!")
        # action_choice = input()
    elif action_choice.lower() == "fill":
        # print("Write how many ml of water do you want to add: %f" % (input()))
        now_water += int(input(("Write how many ml of water do you want to add: ")))
        # print("Write how many ml of milk do you want to add: %f" % (input()))
        now_milk += int(input("Write how many ml of milk do you want to add: "))
        # print("Write how many grams of coffee beans do you want to add: %f" % (input()))
        now_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        # print("Write how many disposable cups of coffee do you want to add: %f" % (input()))
        now_cups += int(input("Write how many disposable cups of coffee do you want to add: "))
        pass
    elif action_choice.lower() == "take":
        while now_money != 0:
            print("I gave you $", now_money)
            now_money = 0
            # break
        pass
    elif action_choice.lower() == "remaining":
        machine_has()
        pass
    elif action_choice.lower() == "exit":
        break
    #else:
    #    print("Write action (buy, fill, take, remaining, exit):")
    #    action_choice = input()
    #    actions = ["buy", "fill", "take", "remaining", "exit"]

