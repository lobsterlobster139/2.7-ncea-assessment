def input_validation(option_list, prompt):
    while True:
        option = input(prompt).capitalize()
        if option in option_list:
            return option
        else:
            print("That is not a valid option. Please re-input your choice.")

def set_size():
    options = ["Small", "Medium", "Large"]
    question = "Would like a small, medium or large pizza? (Type the size you want): "
    choice = input_validation(options, question)
    return choice

def set_dough():
    pass

def set_crust():
    pass

def add_topping():
    pass

def add_pizza(order):
    pizza = {
        'size' : "",
        'dough' : "",
        'crust' : "",
        'toppings' : []
    }
    pizza['size'] = set_size()
    print(pizza)
    set_dough()
    set_crust()

def add_drink(order):
    print("adding drink")

def remove_item(order):
    print("removing item")

def confirm_order(order):
    print("confirming order")

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
    elif option == "b":
        add_drink(order)
    elif option == "c":
        remove_item(order)
    elif option == "d":
        confirm_order(order)
    else:
        print("Not a valid option. Please re-input your choice.")
    

main_menu()
    


