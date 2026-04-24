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

def calc_price(pizza):
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
    options = ["Ginger beer", "Fanta", "Pepsi", "Sprite"]
    question = "What drink would you like? Ginger beer, Fanta, Pepsi or Sprite? (Type the drink you want): "
    choice = input_validation(options, question)
    order.append({'type': "drink", 'name': choice, 'price' : 4.0})

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
        print(f" Price: ${item['price']:.2f}\n")
    else:
        print(f"Can of {item['name']}")
        print(f" Price: ${item['price']:.2f}\n")

def print_total_price(order):
    total_price = 0.0
    for item in order:
        total_price += item['price']
    print(f"Total Price: ${total_price:.2f}")
        

def main_menu():
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
            print("\nCURRENT ORDER:")
            for item in order:
                print_item(item)
            print_total_price(order)
        elif option == "b":
            add_drink(order)
            print("\nCURRENT ORDER:")
            for item in order:
                print_item(item)
            print_total_price(order)
        elif option == "c":
            remove_item(order)
        elif option == "d":
            confirm_order(order)
        else:
            print("Not a valid option. Please re-input your choice.")
    

main_menu()
    


