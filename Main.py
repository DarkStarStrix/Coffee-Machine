def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.10
    nickels = float(input("How many nickels? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


class CoffeeMachine:
    def __init__(self):
        self.resources = {"water": 1000, "milk": 1000, "coffee": 500}
        self.prices = {"espresso": 1.5, "latte": 2.5, "cappuccino": 3.0}
        self.money = 0
        self.on = True

    def off(self):
        self.on = False

    def check_resources(self, coffee_type):
        if coffee_type == "espresso":
            if self.resources["water"] < 50:
                return False
            if self.resources["coffee"] < 18:
                return False
            return True
        elif coffee_type == "latte":
            if self.resources["water"] < 200:
                return False
            if self.resources["milk"] < 150:
                return False
            if self.resources["coffee"] < 24:
                return False
            return True
        elif coffee_type == "cappuccino":
            if self.resources["water"] < 250:
                return False
            if self.resources["milk"] < 100:
                return False
            if self.resources["coffee"] < 24:
                return False
            return True

    def make_coffee(self, coffee_type):
        if not self.check_resources(coffee_type):
            print("Sorry, not enough resources.")
            return

        print(f"The price of {coffee_type} is ${self.prices[coffee_type]}")
        money_inserted = process_coins()
        if money_inserted < self.prices[coffee_type]:
            print("Sorry, not enough money. Money refunded.")
            return

        change = round(money_inserted - self.prices[coffee_type], 2)
        print(f"Here is ${change} in change.")
        self.money += self.prices[coffee_type]

        if coffee_type == "espresso":
            self.resources["water"] -= 50
            self.resources["coffee"] -= 18
        elif coffee_type == "latte":
            self.resources["water"] -= 200
            self.resources["milk"] -= 150
            self.resources["coffee"] -= 24
        elif coffee_type == "cappuccino":
            self.resources["water"] -= 250
            self.resources["milk"] -= 100
            self.resources["coffee"] -= 24

        print(f"Here is your {coffee_type}. Enjoy!")

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")


machine = CoffeeMachine()
while machine.on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine.off()
    elif choice == "report":
        machine.report()
    else:
        machine.make_coffee(choice)
