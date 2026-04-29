"""This program is used for ordering from a pizza store. You can customise your pizza, order drinks, and remove items from your order before confirming."""


def input_validation(option_list, prompt):
    """Validate input by checking if the answer matches something from a list of options."""
    while True:
        option = input(prompt).capitalize()
        if option in option_list:
            return option
        else:
            print("That is not a valid option. Please re-input your choice.")


def int_validation(question):
    """Validate input by checking if it is an integer or not."""
    while True:
        try:
            option = int(input(question))
            print(option)
            return option
        except ValueError:
            print("Please enter only integers.")


def set_size():
    """Child function of add_pizza that makes you choose the size of the pizza."""
    options = ["Small", "Medium", "Large"]
    question = "Would like a small, medium, or large pizza? (Type the size you want): "
    choice = input_validation(options, question)
    return choice


def set_dough():
    """Child function of add_pizza that makes you choose the dough of the pizza."""
    options = ["Thin", "Thick", "Extra thick"]
    question = "Would like the dough to be thin, thick, or extra thick? (Type the dough you want): "
    choice = input_validation(options, question)
    return choice


def set_crust():
    """Child function of add_pizza that makes you choose the crust type of the pizza."""
    options = ["Normal", "Crispy thin", "Cheesy"]
    question = "Would like the crust to be normal, crispy thin, or cheesy? (Type the crust you want): "
    choice = input_validation(options, question)
    return choice


def add_topping(current_pizza):
    """Child function of add_pizza that makes you choose the toppings of the pizza."""
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


def calc_price(pizza):
    """Calculate the price of a pizza based on size."""
    small_price = 9.0
    medium_price = 10.0
    large_price = 12.0
    if pizza['size'] == "Small":
        pizza['price'] = small_price
    elif pizza['size'] == "Medium":
        pizza['price'] = medium_price
    elif pizza['size'] == "Large":
        pizza['price'] = large_price


def add_pizza(order):
    """Add a customised pizza to the order in the form of a dictionary using other smaller functions."""
    pizza = {
        'type' : "pizza",
        'size' : "",
        'dough' : "",
        'crust' : "",
        'toppings' : [],
        'price' : 0.0,
    }
    pizza['size'] = set_size()
    pizza['dough'] = set_dough()
    pizza['crust'] = set_crust()
    calc_price(pizza)
    add_topping(pizza)
    order.append(pizza)


def add_drink(order):
    """Add a drink to the order of the customers choice."""
    options = ["Ginger beer", "Fanta", "Pepsi", "Sprite"]
    question = "What drink would you like? Ginger beer, Fanta, Pepsi or Sprite? (Type the drink you want): "
    choice = input_validation(options, question)
    order.append({'type': "drink", 'name': choice, 'price' : 4.0})


def remove_item(order):
    """Remove any item in the order that the customer specifies."""
    number = 0
    for item in order:
        number += 1
        print(f"{number}. ")
        print_item(item)
    choice = int_validation("Which item in the order would you like to remove? Please enter the corresponding number: ")
    removing_item = order[choice-1]
    order.remove(removing_item)
    print("Item removed!")


def confirm_order():
    """Confirm that the customer has finished their order and is ready for it to be processed."""
    options = ["Y", "N"]
    choice = input_validation(options, "Are you sure you want to confirm your order? Y/N: ")
    if choice == "Y":
        print("Thank you for ordering with us! Your order will be ready shortly. Please leave a good review to support our business!")
        exit()
    elif choice == "N":
        print("Returning to main menu...")


def print_item(item):
    """Print an order item in the correct format."""
    if item['type'] == "pizza":
        print("Pizza:")
        print(f" Size: {item['size']}")
        print(f" Dough: {item['dough']}")
        print(f" Crust: {item['crust']}")
        print(" Toppings: ")
        for topping in item['toppings']:
            print(f"     {topping}")
        print(f" Price: ${item['price']:.2f}\n")
    else:
        print(f"Can of {item['name']}")
        print(f" Price: ${item['price']:.2f}\n")


def print_total_price(order):
    """Print the total price of the order."""
    total_price = 0.0
    for item in order:
        total_price += item['price']
    print(f"Total Price: ${total_price:.2f}")


def print_current_order(order):
    """Print all the items currently in the order."""
    print("\nCURRENT ORDER:")
    for item in order:
        print_item(item)
    print_total_price(order)


def main_menu():
    """Control the cycle of the program."""
    order = []
    print("Hello! What would you like to add to your order?\nPlease type the letter corresponding to the action you would like to do.")
    while True:
        option = input("""
a) Add a pizza
b) Add a drink
c) Remove an item from your order
d) Confirm order
""").lower()
        if option == "a":
            add_pizza(order)
            print_current_order(order)
        elif option == "b":
            add_drink(order)
            print_current_order(order)
        elif option == "c":
            if len(order) == 0:
                print("No items in your order.")
            else:
                remove_item(order)
                print_current_order(order)
        elif option == "d":
            print_current_order(order)
            confirm_order()
        else:
            print("Not a valid option. Please re-input your choice.")


main_menu()
