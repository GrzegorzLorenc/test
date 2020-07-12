class CoffeeMachine:
    def __init__(self):
        self.water_machine = 400
        self.milk_machine = 540
        self.coffee_machine = 120
        self.disposable_cups = 9
        self.money_machine = 550
        self.machine_state = 'default state'
        self.menu()

    def menu(self):  # noinspection PyMethodMayBeStatic
        print('Write action (buy, fill, take, remaining, exit):')

    def main_method(self, user_choice):
        if self.machine_state == 'default state':
            if user_choice == "menu":
                if user_choice == "buy":
                    self.machine_state = "buying_coffee"
                    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino, back - to main menu:')
                elif user_choice == 'fill':
                    self.machine_state = 'refilling'
                elif user_choice == 'take':
                    self.machine_state = 'taking'
                elif user_choice == 'remaining':
                    self.show_supplies()
                    self.menu()
            elif self.machine_state == "off":
                print("Turning the light on")
                self.machine_state = "on"

    def show_supplies(self):
        print('The coffee machine has:')
        print(f'{self.water_machine} of water')
        print(f'{self.milk_machine} of milk')
        print(f'{self.coffee_machine} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'{self.money_machine} of money')
        print('')

    def check_resources_espresso(self):
        if self.water_machine < 250:
            print('Sorry, not enough water')
            self.menu()
        elif self.coffee_machine < 16:
            print('Sorry, not enough coffee')
            self.menu()
        elif self.disposable_cups < 1:
            print('Sorry, not enough cups')
            self.menu()
        else:
            print('I have enough resources, making you a coffee!')
            self.water_machine -= 250
            self.coffee_machine -= 16
            self.disposable_cups -= 1
            self.money_machine += 4
            self.menu()

    def check_resources_latte(self):
        if self.water_machine < 350:
            print('Sorry, not enough water')
            self.menu()
        elif self.milk_machine < 75:
            print('Sorry, not enough milk')
            self.menu()
        elif self.coffee_machine < 20:
            print('Sorry, not enough coffee')
            self.menu()
        elif self.disposable_cups < 1:
            print('Sorry, not enough cups')
            self.menu()
        else:
            print('I have enough resources, making you a coffee!')
            self.water_machine -= 350
            self.milk_machine -= 75
            self.coffee_machine -= 20
            self.disposable_cups -= 1
            self.money_machine += 7
            self.menu()

    def check_resources_cappuccino(self):
        if self.water_machine < 350:
            print('Sorry, not enough water')
            self.menu()
        elif self.milk_machine < 75:
            print('Sorry, not enough milk')
            self.menu()
        elif self.coffee_machine < 20:
            print('Sorry, not enough coffee')
            self.menu()
        elif self.disposable_cups < 1:
            print('Sorry, not enough cups')
            self.menu()
        else:
            print('I have enough resources, making you a coffee!')
            self.water_machine -= 200
            self.milk_machine -= 100
            self.coffee_machine -= 12
            self.disposable_cups -= 1
            self.money_machine += 6
            self.menu()

    def take_money(self):
        print(f'I gave you $ {self.money_machine}')
        self.money_machine = 0
        self.menu()

    def fill_machine(self):
        print('Write how many ml of water do you want to add:')
        self.water_machine += (int(input()))
        print('Write how many ml of milk do you want to add:')
        self.milk_machine += (int(input()))
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_machine += (int(input()))
        print('Write how disposable cups do you want to add:')
        self.disposable_cups += (int(input()))


CoffeeMachine()
user_input = input()
while True:
    if user_input == 'exit':
        break


# menu()
# while True:
#     if choice == 'buy':
#         print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
#         choice = input()
#         if choice == '1':
#             check_resources_espresso()
#         elif choice == '2':
#             check_resources_latte()
#         elif choice == '3':
#             check_resources_cappuccino()
#         elif choice == 'back':
#             menu()
#     elif choice == 'fill':
#         fill_machine()
#         menu()
#     elif choice == 'take':
#         take_money()
#         show_supplies()
#         menu()
#     elif choice == 'remaining':
#         show_supplies()
#         menu()
#     elif choice == 'exit':
#         break
