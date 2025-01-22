#Dictionary for Menu
starter1 = {
    'Name' : 'Starter 1',
    'Price' : 100,
    'Tag' : 1,
}
starter2 = {
    'Name' : 'Starter 2',
    'Price' : 100,
    'Tag' : 2,
}
course1 = {
    'Name' : 'Main Course 1',
    'Price' : 100,
    'Tag' : 3,
}
course2 = {
    'Name' : 'Main Course 2',
    'Price' : 100,
    'Tag' : 4,
}
desert1 = {
    'Name' : 'Desert 1',
    'Price' : 100,
    'Tag' : 5,
}
desert2 = {
    'Name' : 'Desert 2',
    'Price' : 100,
    'Tag' : 6,
}


#List for Menu Items
starters = [starter1,starter2]
courses = [course1,course2]
deserts = [desert1,desert2]
orders = []
counter = 0


def instructions():
    print("\nWelcome!\nHow May I Be of Assitance?")
    print("========================")
    print("S --> Show Menu")
    print("P --> Place Order")
    print("O --> Order Summary")
    print("R --> Remove Item From Order")
    print("T --> Submit Your Order")
    print("quit --> Quit The Program")
    print("========================")


def show_menu(starters,courses,deserts):
    print("==========Menu==========")
    print("\n=======Starters=======")
    for starter in starters:
        print(f"{starter['Name']} ---> {starter['Price']}::{starter['Tag']}")
    print("\n========Main Course========")
    for course in courses:
        print(f"{course['Name']} ---> {course['Price']}::{course['Tag']}")
    print("\n========Desert========")
    for desert in deserts:
        print(f"{desert['Name']} ---> {desert['Price']}::{desert['Tag']}")


def place_order(starters,courses,deserts,order):
    while True:
        print("\nType 666 to Quit Ordering...")
        choice = int(input("Please Input the Tag Number of your food item: "))
        if choice == 666:
            break
        elif choice >= 7 or choice < 1:
            print("Unknown Tag Number ---- Please Try Again!")
            continue
        for starter in starters:
            if choice == starter['Tag']:
                order.append(starter)

        choice2 = input("Do You Want to Order Something Else?(y/n): ")
        if choice2 == 'y' or choice2 == 'Y':
            menu_choice = input("What would you like to order from?(S:Starters,M:Course,D:Desert): ")
            if menu_choice == 's' or menu_choice == 'S':
                print("==========Menu==========")
                print("\n=======Starters=======")
                for starter in starters:
                    print(f"{starter['Name']} ---> {starter['Price']}::{starter['Tag']}")
            if menu_choice == 'm' or menu_choice == 'M':
                print("\n========Main Course========")
                for course in courses:
                    print(f"{course['Name']} ---> {course['Price']}::{course['Tag']}")
            if menu_choice == 'd' or menu_choice == 'd':
                print("\n========Desert========")
                for desert in deserts:
                    print(f"{desert['Name']} ---> {desert['Price']}::{desert['Tag']}")
        
        print("\nType 666 to Quit Ordering...")
        choice3 = int(input("Please Input the Tag Number of your food item: "))
        if choice3 == 666:
            break
        elif choice3 >= 7 or choice3 < 1:
            print("Unknown Tag Number ---- Please Try Again!")
            continue
        for course in courses:
            if choice3 == course['Tag']:
                order.append(course)

        choice4 = input("Do You Want to Order Something Else?(y/n): ")
        if choice4 == 'y' or choice4 == 'Y':
            menu_choice = input("What would you like to order from?(S:Starters,M:Course,D:Desert): ")
            if menu_choice == 's' or menu_choice == 'S':
                print("==========Menu==========")
                print("\n=======Starters=======")
                for starter in starters:
                    print(f"{starter['Name']} ---> {starter['Price']}::{starter['Tag']}")
            if menu_choice == 'm' or menu_choice == 'M':
                print("\n========Main Course========")
                for course in courses:
                    print(f"{course['Name']} ---> {course['Price']}::{course['Tag']}")
            if menu_choice == 'd' or menu_choice == 'd':
                print("\n========Desert========")
                for desert in deserts:
                    print(f"{desert['Name']} ---> {desert['Price']}::{desert['Tag']}")
                    
        print("\nType 666 to Quit Ordering...")
        choice5 = int(input("Please Input the Tag Number of your food item: "))
        if choice5 == 666:
            break
        elif choice5 >= 7 or choice3 < 1:
            print("Unknown Tag Number ---- Please Try Again!")
            continue
        for desert in deserts:
            if choice5 == desert['Tag']:
                order.append(desert)


def order_summary(orders):
    Price = 0
    print("============Your Order============")
    for order in orders:
        Price += order['Price']
        print("------------------------")
        for key, info in order.items():
            print(f"{key}: {info}")
        print("------------------------")
    print("========================")
    print(f"Overall Price: ${Price}")


def order_remove(orders):
    order_summary(orders)
    print("Which Item Do You Want To Remove From Your Order?")
    print("Type 666 To Cancel")
    while True:
        choice6 = int(input("Please Type The Tag Number: "))
        if choice6 == 666:
            break
        for starter in orders:
            if choice6 == starter['Tag']:
                starter.remove(starter)
                break
        for course in orders:
            if choice6 == course['Tag']:
                course.remove(course)
                break
        for desert in orders:
            if choice6 == desert['Tag']:
                desert.remove(desert)
                break


def order_submit(orders):
    choice7 = input("Are You Sure You Want To Submit Your Order?(y/n): ")
    if choice7 == 'Y' or choice7 == 'y':
        order_summary(orders)
        while len(orders) != 0:
            del orders[counter]


def restaurant_order():
    print("\nWelcome To Our Restaurant!")
    while True:
        instructions()
        choice8 = input("Please Type The Corresponding letter for certain actions: ")
        if choice8 == 'S' or choice8 == 's':
            show_menu(starters,courses,deserts)
        elif choice8 == 'P' or choice8 == 'p':
            place_order(starters,courses,deserts,orders)
        elif choice8 == 'O' or choice8 == 'o':
            order_summary(orders)
        elif choice8 == 'R' or choice8 == 'r':
            order_remove(orders)
        elif choice8 == 'T' or choice8 == 't':
            order_submit(orders)
        elif choice8 == 'quit':
            break
        else:
            print("Unknown Selection --- Please Try Again")

restaurant_order()