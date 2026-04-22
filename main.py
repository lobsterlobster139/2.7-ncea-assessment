def input_validation():
    pass

def set_size():
    pass

def set_dough():
    pass

def set_crust():
    pass

def add_topping():
    pass

def add_pizza():
    print("adding pizza")

def add_drink():
    print("adding drink")

def remove_item():
    print("removing item")

def add_to_order():
    pass

def confirm_order():
    print("confirming order")

def main_menu():
    print("Hello! What would you like to add to your order?\nPlease type the letter corresponding to the action you would like to do.")
    option = input("""
a) Add a pizza
b) Add a drink
c) Remove an item from your order
d) Confirm order
""").lower()
    if option == "a":
        add_pizza()
    elif option == "b":
        add_drink()
    elif option == "c":
        remove_item()
    elif option == "d":
        confirm_order()
    else:
        print("Not a valid option. Please re-input your choice.")
    

main_menu()
    


