# Updates coffee3.py, asks user if they want to buy coffee, fill the machine, 
# take cash, ask for levels or exit. 
# Runs on loop and updates levels throughout.

#quantities available at start
cash_float = 550 #dollars
water = 400 #millilitres
milk = 540 #millilitres
coffee_beans = 120 #grams
disposable_cups = 9

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
    (water, milk, coffee_beans, disposable_cups, cash))
    
def update_stock(water_needed, milk_needed, coffee_needed, cash_needed):
    global water
    global milk
    global coffee_beans 
    global disposable_cups
    global cash_float
    if (water < water_needed):
        print("Sorry, not enough water!")
    else:
        if milk < milk_needed:
            print("Sorry, not enough milk!\n")
        else:
            if coffee_beans < coffee_needed:
                print("Sorry, not enough coffee!\n")
            else:
                water = water - water_needed
                milk = milk - milk_needed
                coffee_beans = coffee_beans - coffee_needed
                disposable_cups = disposable_cups - 1
                cash_float = cash_float + cash_needed
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
    
    global water
    global milk
    global coffee_beans 
    global disposable_cups
    global cash_float
    water = water + water_request
    milk = milk + milk_request
    coffee_beans = coffee_beans + coffee_request
    disposable_cups = disposable_cups + cup_request

def coffee_machine_take():
    global cash_float
    print("\nI gave you $%d" % (cash_float))
    cash_float = 0

def coffee_machine_request():
        if request == "fill":
            coffee_machine_fill()
        if request == "buy":
            coffee_machine_buy()
        elif request == "take":
            coffee_machine_take()
        elif request == "remaining":
            coffee_machine_status(water, milk, coffee_beans, disposable_cups, cash_float)

#start of program:

while True:
    request = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    if request != "exit":
        coffee_machine_request()
    else:
        exit()
