#REFERNCE


sandwich1 = {
    'Name': 'Normal Chicken Sandwich',
    'Price': 20.99,
    'Tag': 1,
}
sandwich2 = {
    'Name': 'Egg Sandwich',
    'Price': 15.99,
    'Tag': 2,
}
sandwich3 = {
    'Name': 'Fish Sandwich',
    'Price': 17.99,
    'Tag': 3,
}
sandwich4 = {
    'Name': 'Grilled Cheese Sandwich',
    'Price': 25.99,
    'Tag': 4,
}
sandwich5 = {
    'Name': 'Grilled Chicken Sandwich',
    'Price': 23.99,
    'Tag': 5,
}
sandwich6 = {
    'Name': 'Ham Sandwich',
    'Price': 21.99,
    'Tag': 6,
}
sandwich7 = {
    'Name': 'Roast Beef Sandwich',
    'Price': 25.99,
    'Tag': 7,
}
topping1 = {
    'Name': 'Sliced egg with chili sauce',
    'Price': 5.99,
    'Tag': 8,
}
topping2 = {
    'Name': 'Beef with wasabi mayonnaise',
    'Price': 6.99,
    'Tag': 9,
}
topping3 = {
    'Name': 'Reduced fat ricotta, peas & mint',
    'Price': 4.99,
    'Tag': 10,
}
topping4 = {
    'Name': 'Turkey, cranberry & avocado',
    'Price': 8.99,
    'Tag': 11,
}
sandwiches = [sandwich1, sandwich2, sandwich3, sandwich4, sandwich5, sandwich6,sandwich7]
toppings = [topping1, topping2, topping3, topping4]
ordered_sandwiches = []
counter = 0
def instructions():
    print("========================")
    print("S --> Show Menu")
    print("P --> Place Order")
    print("O --> Order Summary")
    print("R --> Remove Item From Order")
    print("T --> Submit Your Order")
    print("quit --> Quit The Program")
    print("========================")
def show_menu(sandwiches_list, toppings_list):
    print("==========Menu==========")
    print("\n=======Sandwiches=======")
    for sandwich in sandwiches_list:
        print(f"- {sandwich['Name']} ---> ${sandwich['Price']} --> Tag:{sandwich['Tag']}")
    print("\n========Toppings========")
    for topping in toppings_list:
        print(f"- {topping['Name']} ---> ${topping['Price']} --> Tag:{topping['Tag']}")
def place_order(sandwiches_list, toppings_list, ordered_sandwiches_list):
    while True:
        print("Type 666 To Quit Ordering...")
        choice2 = int(input("Please Type The Sandwich Tag Number: "))
        if choice2 == 666:
            break
        elif choice2 > 7 or choice2 < 1:
            print("Unknown Tag Number -- Please Try Again!")
            continue
        for sandwich in sandwiches_list:
            if choice2 == sandwich['Tag']:
                ordered_sandwiches_list.append(sandwich)
        choice3 = input("Do You Want To Order Special Topping With It?(y/n): ")
        if choice3 == 'y' or choice3 == 'Y':
            for topping in toppings_list:
                print(f"- {topping['Name']} ---> ${topping['Price']} -->"
                f" Tag:{topping['Tag']}")
            choice4 = int(input("Please Type The Topping Tag Number: "))
            for topping in toppings_list:
                if choice4 == topping['Tag']:
                    for sandwich in ordered_sandwiches_list:
                        if choice2 == sandwich['Tag']:
                            sandwich['Topping'] = topping['Name']
                            sandwich['Price'] += topping['Price']
                            break
        elif choice3 == 'N' or choice3 == 'n':
            continue
def order_summary(ordered_sandwiches_list):
    Price = 0
    print("========================")
    for sandwich in ordered_sandwiches_list:
        Price += sandwich['Price']
        print("------------------------")
        for key, info in sandwich.items():
            print(f"{key}: {info}")
        print("------------------------")
    print("========================")
    print(f"Overall Price: ${Price}")
def order_remove(ordered_sandwiches_list):
    order_summary(ordered_sandwiches)
    print("Which Item Do You Want To Remove From Your Order?")
    print("Type 666 To Cancel")
    while True:
        choice5 = int(input("Please Type The Tag Number: "))
        if choice5 == 666:
            break
        for sandwich in ordered_sandwiches_list:
            if choice5 == sandwich['Tag']:
                ordered_sandwiches_list.remove(sandwich)
                break
def order_submit(ordered_sandwiches_list):
    choice6 = input("Are You Sure You Want To Submit Your Order?(y/n): ")
    if choice6 == 'Y' or choice6 == 'y':
        order_summary(ordered_sandwiches)
        while len(ordered_sandwiches_list) != 0:
            del ordered_sandwiches_list[counter]
def sandwich_order():
    print("Welcome To Our Restaurant!")
    while True:
        instructions()
        choice = input("Please Type The Corresponding letter for certain actions: ")
        if choice == 'S' or choice == 's':
            show_menu(sandwiches, toppings)
        elif choice == 'P' or choice == 'p':
            place_order(sandwiches, toppings, ordered_sandwiches)
        elif choice == 'O' or choice == 'o':
            order_summary(ordered_sandwiches)
        elif choice == 'R' or choice == 'r':
            order_remove(ordered_sandwiches)
        elif choice == 'T' or choice == 't':
            order_submit(ordered_sandwiches)
        elif choice == 'quit':
            break
        else:
            print("Unknown Selection --- Please Try Again")
sandwich_order()