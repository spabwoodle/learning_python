# Asks user if they want to buy a coffee from the machine, 
# fill machine with items or take cash out

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

def coffee_machine_buy(request):
    buy_request = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if buy_request == 1:
        hot_drink = espresso
    elif buy_request == 2:
        hot_drink = latte
    elif buy_request == 3:
        hot_drink = cappuccino
    
    print("""The coffee machine has:")
    %d of water
    %d of milk
    %d of coffee beans
    %d of disposable cups
    %d of money""" % 
    (water - hot_drink[1], 
    milk - hot_drink[2], 
    coffee_beans - hot_drink[3], 
    disposable_cups - 1, 
    cash_float + hot_drink[0]))

def coffee_machine_fill(request):
    water_request = int(input("Write how many ml of water do you want to add:"))
    milk_request = int(input("Write how many ml of milk do you want to add:"))
    coffee_request = int(input("Write how many grams of coffee beans do you want to add:"))
    cup_request = int(input("Write how many disposable cups of coffee do you want to add:"))

    print("""The coffee machine has:
    %d of water
    %d of milk
    %d of coffee beans
    %d of disposable cups
    %d of money""" %
    (water + water_request,
    milk + milk_request,
    coffee_beans + coffee_request,
    disposable_cups + cup_request,
    cash_float))

def coffee_machine_take(request):
    print("""I gave you $%d" % (cash_float))
    \nThe coffee machine has:
    %d of water
    %d of milk
    %d of coffee beans
    %d of disposable cups
    %d of money""" % 
    (water, milk, coffee_beans, disposable_cups, int(cash_float - cash_float)))

#start of program:

print("The coffee machine has:")
print(str(water) + " of water")
print(str(milk) + " of milk")
print(str(coffee_beans) + " of coffee beans")
print(str(disposable_cups) + " of disposable cups")
print(str(cash_float) + " of money\n")
request = input("Write action (buy, fill, take): ")

if request == "buy":
    coffee_machine_buy(request)
elif request == "fill":
    coffee_machine_fill(request)
elif request == "take":
    coffee_machine_take(request)
