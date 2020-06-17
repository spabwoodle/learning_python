# Updates coffee3.py, asks user if they want to buy coffee, fill the machine, 
# take cash, ask for levels or exit. Runs on loop and updates levels throughout.

# Coffee machine contents at start:
# [dollars cash, ml water, ml milk, grams coffee beans, disposable cups]
contents = [550, 400, 540, 120, 9] 

#quantities per drink (price, ml water, ml milk, grams coffee)
espresso = [4, 250, 0, 16]
latte = [7, 350, 75, 20]
cappuccino = [6, 200, 100, 12]
hot_drink = []


def coffee_machine_status(water, milk, coffee_beans, disposable_cups, cash):    
    print("""\nThe coffee machine has:
%d of water
%d of milk
%d of coffee beans
%d of disposable cups
$%d of money""" % 
    (contents[1], contents[2], contents[3], contents[4], contents[0]))
    

def update_stock(water_needed, milk_needed, coffee_needed, cash_needed):
    if (contents[1] < water_needed):
        print("Sorry, not enough water!")
    else:
        if contents[2] < milk_needed:
            print("Sorry, not enough milk!\n")
        else:
            if contents[3] < coffee_needed:
                print("Sorry, not enough coffee!\n")
            else:
                contents[1] = contents[1] - water_needed
                contents[2] = contents[2] - milk_needed
                contents[3] = contents[3] - coffee_needed
                contents[4] = contents[4] - 1
                contents[0] = contents[0] + cash_needed
                print("I have enough resources, making you a coffee!")


def coffee_machine_buy():
    buy_request = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if buy_request == "1":
        update_stock(espresso[1], espresso[2], espresso[3], espresso[0])
    elif buy_request == "2":
        update_stock(latte[1], latte[2], latte[3], latte[0])
    elif buy_request == "3":
        update_stock(cappuccino[1], cappuccino[2], cappuccino[3], cappuccino[0])
    elif buy_request == "back":
        pass


def coffee_machine_fill():
    water_request = int(input("\nWrite how many ml of water do you want to add:\n"))
    milk_request = int(input("Write how many ml of milk do you want to add:\n"))
    coffee_request = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cup_request = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    
    contents[1] = contents[1] + water_request
    contents[2] = contents[2] + milk_request
    contents[3] = contents[3] + coffee_request
    contents[4] = contents[4] + cup_request


def coffee_machine_take():
    global contents
    print("\nI gave you $%d" % (contents[0]))
    contents[0] = 0


def coffee_machine_request():
        if request == "fill":
            coffee_machine_fill()
        elif request == "buy":
            coffee_machine_buy()
        elif request == "take":
            coffee_machine_take()
        elif request == "remaining":
            coffee_machine_status(contents[1], contents[2], contents[3], contents[4], contents[0])

#start of program:

while True:
    request = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    if request != "exit":
        coffee_machine_request()
    else:
        exit()
