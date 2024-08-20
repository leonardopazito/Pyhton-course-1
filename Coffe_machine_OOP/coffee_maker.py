from menu import MenuItem


class CoffeeMaker:
    """It models the machine that makes the coffee"""
    def __init__(self):
        self.resources: dict[str, int | float] = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """It prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem | None):
        """It returns True when order can be made, False if ingredients are
        insufficient."""
        can_make = True
        if drink is not None:
            for item in drink.ingredients:
                if drink.ingredients[item] > self.resources[item]:
                    print(f"Sorry there is not enough {item}.")
                    can_make = False
            return can_make
        else:
            can_make = False
            return can_make

    def make_coffee(self, order: MenuItem):
        """It deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
