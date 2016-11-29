import random

class Crops(object):
    def __init__(self, growth_rate, light_need, water_need):
        # set attribute to the initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        return {'light need': self._light_need, 'water need': self._water_need}  # Return dict of 'needs'

    def report(self):
        return {'type': self._type, 'status': self._status, 'growth': self._growth, 'days growing': self._days_growing}

    def update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
            self._days_growing += 1
            self.update_status()


def auto_grow_crops(crops, days):
    for day in range(days):
        light = random.randint(1, 10)
        water = random.randint(1, 10)
        crops.grow(light, water)


def manual_grow_crops(crops):
    valid = False
    while not valid:
        try:
            light = int(raw_input("Enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Entered value is not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Entered value is not valid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(raw_input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a vlue between 1 and 10")
    crops.grow(light, water)


def display_menu():
    print("1. Grown manually for 1 day")
    print("2. Grown automatically for the 30 days")
    print("3. Report status")
    print("4. Exit menu program")
    print()
    print("Select menu option ")


def get_menu_choice():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Select option: "))
            if 1 <= choice <= 4:
                valid_option = True
            else:
                print("Please enter a value from 1 to 4")
        except ValueError:
            print("Please enter a valid option from 1 to 4")
    return choice

def manage_crops(crop):
    print("Crop management")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow_crops(crop)
            print()
        elif option == 2:
            auto_grow_crops(crop, 30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 4:
            noexit = False
            print()
    print("Crop management is going to close")



if __name__ == '__main__':
    crop = Crops(1, 4, 3)
    manage_crops(crop)