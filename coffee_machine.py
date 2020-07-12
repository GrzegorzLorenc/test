class CoffeeMachine:
    def __init__(self):
        self.water_machine = 400
        self.milk_machine = 540
        self.coffee_machine = 120
        self.disposable_cups = 9
        self.money_machine = 550
        self.machine_state = 'default state'
        self.filling_state = 1
        self.type_of_coffee_chosen = 0
        self.menu()

    def menu(self):  # noinspection PyMethodMayBeStatic
        print('Write action (buy, fill, take, remaining, exit):')

    def main_method(self, user_choice):
        if self.machine_state == 'default state':
            if user_choice == "buy":
                self.machine_state = "buying coffee"
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            elif user_choice == 'fill':
                self.machine_state = 'refilling'
                print("Write how many ml of water do you want to add:")
            elif user_choice == 'take':
                self.take_money()
                self.menu()
            elif user_choice == 'remaining':
                self.show_supplies()
                self.menu()
            elif self.machine_state == 'refilling':
                print("Turning the light on")
                self.machine_state = "on"
        elif self.machine_state == "refilling":
            if self.filling_state == 1:
                self.water_machine += int(user_choice)
                print("Write how many ml of milk do you want to add:")
                self.filling_state = 2
            elif self.filling_state == 2:
                print("Write how many grams of coffee beans do you want to add:")
                self.milk_machine += int(user_choice)
                self.filling_state = 3
            elif self.filling_state == 3:
                print("Write how many disposable cups of coffee do you want to add:")
                self.coffee_machine += int(user_choice)
                self.filling_state = 4
            elif self.filling_state == 4:
                self.disposable_cups += int(user_choice)
                self.filling_state = 1
                self.machine_state = "default state"
                self.menu()
        elif self.machine_state == "buying coffee":
            if user_choice == "back":
                self.machine_state = "default state"
                self.menu()
            elif user_choice == "1" or user_choice == "2" or user_choice == "3":
                self.type_of_coffee_chosen = int(user_choice)
                self.resource_check()

    def show_supplies(self):
        print('The coffee machine has:')
        print(f'{self.water_machine} of water')
        print(f'{self.milk_machine} of milk')
        print(f'{self.coffee_machine} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'{self.money_machine} of money')
        print('')

    def resource_check(self):
        menu = {1: {"water": 250, "milk": 0, "coffee_bean": 16, "cup": 1, "money": 4},
                2: {"water": 350, "milk": 75, "coffee_bean": 20, "cup": 1, "money": 7},
                3: {"water": 200, "milk": 100, "coffee_bean": 12, "cup": 1, "money": 6}, }

        if self.water_machine < menu[self.type_of_coffee_chosen]["water"]:
            print("Sorry, not enough water!")
            self.machine_state = "default state"
            self.menu()
        elif self.milk_machine < menu[self.type_of_coffee_chosen]["milk"]:
            print("Sorry, not enough milk!")
            self.machine_state = "default state"
            self.menu()
        elif self.coffee_machine < menu[self.type_of_coffee_chosen]["coffee_bean"]:
            print("Sorry, not enough coffee beans")
            self.machine_state = "default state"
            self.menu()
        elif self.disposable_cups < menu[self.type_of_coffee_chosen]["cup"]:
            print("Sorry, not enough cup")
            self.machine_state = "default state"
            self.menu()
        else:
            print("I have enough resources, making you a coffee!")
            self.water_machine -= menu[self.type_of_coffee_chosen]["water"]
            self.milk_machine -= menu[self.type_of_coffee_chosen]["milk"]
            self.coffee_machine -= menu[self.type_of_coffee_chosen]["coffee_bean"]
            self.disposable_cups -= menu[self.type_of_coffee_chosen]["cup"]
            self.money_machine += menu[self.type_of_coffee_chosen]["money"]
            self.machine_state = "default state"
            self.menu()

    def take_money(self):
        print(f'I gave you $ {self.money_machine}')
        self.money_machine = 0

    def fill_machine(self):
        print('Write how many ml of water do you want to add:')
        self.water_machine += (int(input()))
        print('Write how many ml of milk do you want to add:')
        self.milk_machine += (int(input()))
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_machine += (int(input()))
        print('Write how disposable cups do you want to add:')
        self.disposable_cups += (int(input()))


cafe = CoffeeMachine()

while True:
    user_input = input()
    cafe.main_method(user_input)
    if user_input == 'exit':
        break
