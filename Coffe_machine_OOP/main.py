from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_of_coffee_machine = Menu()
coffe_machine = CoffeeMaker()
money_of_machine = MoneyMachine()

should_continue = True
off_machine = False

while should_continue:
    input_the_new_choice = True
    while input_the_new_choice:
        choice_of_cliente = input(
            f"What would you like? {menu_of_coffee_machine.get_items()}: "
        ).lower()
        if choice_of_cliente == 'off':
            should_continue, input_the_new_choice, off_machine = (False,
                                                                  False,
                                                                  True)
        elif choice_of_cliente == 'report':
            coffe_machine.report()
            money_of_machine.report()
        else:
            item = menu_of_coffee_machine.find_drink(choice_of_cliente)
            if item is not None:
                input_the_new_choice = False

    if (not off_machine and should_continue
            and item is not None):
        if not coffe_machine.is_resource_sufficient(item):
            print("Sorry there is not enough water")
        else:
            print(f"The {item.name} cost {item.cost}")
            if money_of_machine.make_payment(item.cost):
                coffe_machine.make_coffee(item)

        should_continue = input('Do want other order? (y/n)').lower() == 'y'
