def input_validation(option_list, prompt):
    while True:
        option = input(prompt).capitalize()
        if option in option_list:
            return option
        else:
            print("That is not a valid option. Please re-input your choice.")

def set_size():
    options = ["Small", "Medium", "Large"]
    question = "Would like a small, medium, or large pizza? (Type the size you want): "
    choice = input_validation(options, question)
    return choice

def set_dough():
    options = ["Thin", "Thick", "Extra thick"]
    question = "Would like the dough to be thin, thick, or extra thick? (Type the dough you want): "
    choice = input_validation(options, question)
    return choice

def set_crust():
    options = ["Normal", "Crispy thin", "Cheesy"]
    question = "Would like the crust to be normal, crispy thin, or cheesy? (Type the crust you want): "
    choice = input_validation(options, question)
    return choice

def add_topping(current_pizza):
    topping_options = ["Cheese", "Tomato sauce", "Pepperoni", "Sausage", "Cream cheese", "Chicken", "Olives", "Pineapple", "Onion", "Apricot sauce", "Barbecue sauce", "Aioli", "Finish"]
    print("Add some toppings by inputting their name, or type 'Finish' to complete your pizza. (We reccomend atleast cheese and tomato sauce!)")
    for topping in topping_options:
        print(topping)
    print("\n")
    while True:
        choice = input_validation(topping_options, "")
        if choice == "Finish":
            break
        current_pizza['toppings'].append(choice)

def add_pizza(order):
    pizza = {
        'type' : "pizza",
        'size' : "",
        'dough' : "",
        'crust' : "",
        'toppings' : []
    }
    pizza['size'] = set_size()
    pizza['dough'] = set_dough()
    pizza['crust'] = set_crust()
    add_topping(pizza)
    order.append(pizza)

def add_drink(order):
    print("adding drink")

def remove_item(order):
    print("removing item")

def confirm_order(order):
    print("confirming order")

def print_item(item):
    if item['type'] == "pizza":
        print(f"Pizza:")
        print(f" Size: {item['size']}")
        print(f" Dough: {item['dough']}")
        print(f" Crust: {item['crust']}")
        print(f" Toppings: ")
        for topping in item['toppings']:
            print(f"     {topping}")

def main_menu():
    order = []
    print("Hello! What would you like to add to your order?\nPlease type the letter corresponding to the action you would like to do.")
    option = input("""
a) Add a pizza
b) Add a drink
c) Remove an item from your order
d) Confirm order
""").lower()
    if option == "a":
        add_pizza(order)
        print("CURRENT ORDER:\n")
        for item in order:
            print_item(item)
    elif option == "b":
        add_drink(order)
    elif option == "c":
        remove_item(order)
    elif option == "d":
        confirm_order(order)
    else:
        print("Not a valid option. Please re-input your choice.")
    

main_menu()
    


