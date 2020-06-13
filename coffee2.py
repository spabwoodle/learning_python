# Asks for quantities of water, milk and coffee beans 
# in coffee machine, then says how 
# many cups of coffee you can make

water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups_coffee = int(input("Write how many cups of coffee you will need: "))

sufficient_water = water >= (cups_coffee * 200) # one cup coffee needs 200ml water
sufficient_milk = milk >= (cups_coffee * 50) # needs 50ml milk
sufficient_coffee = coffee_beans >= (cups_coffee * 15) # needs 15g coffee beans

# cup_quantifier tells how many cups you can make with ingredients available
def cup_quantifier(ingredient, divider):
    number_of_cups = ingredient / divider
    return int(number_of_cups)

available_water = cup_quantifier(water, 200)
available_milk = cup_quantifier(milk, 50)
available_beans = cup_quantifier(coffee_beans, 15)

def lowest_number(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c 

def coffee_machine(water, milk, coffee_beans, cups_coffee):
    if sufficient_water is False or sufficient_milk is False or sufficient_coffee is False:
        number_of_cups = lowest_number(available_water, available_milk, available_beans)
        return("No, I can make only " + str(number_of_cups) + " cups of coffee")      
    elif available_water >= 2 and available_milk >= 2 and available_beans >= 2:
        number_of_cups = lowest_number(available_water, available_milk, available_beans) - cups_coffee          
        return("Yes, I can make that amount of coffee (and even " + str(number_of_cups) + " more than that)")
    else:
        return("Yes, I can make that amount of coffee")

print(coffee_machine(water, milk, coffee_beans, cups_coffee))
