# Basta Fazoolin' project

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill

    def __repr__(self):
        return self.name + " is available from " + str(self.start_time) +  " - " + str(self.end_time)

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu

    def __repr__(self):
        return self.address

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items , 1100, 1600)

early_bird_items =  {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
early_bird = Menu("Early-bird", early_bird_items, 1500,1800)

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner = Menu("Dinner",dinner_items , 1700, 2300)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", kids_items, 1100, 2100)

arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepa = Menu("Take a arepa", arepa_items, 1000, 2000)

#print(brunch.calculate_bill(['pancakes','home fries','coffee']))
#print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))
menus = [brunch, early_bird, dinner, kids]
loc1 = Franchise("1232 West End Road", menus)
loc2 = Franchise("12 East Mulberry Street", menus)
loc3 = Franchise("189 Fitzgerald Avenue", [arepa])
#print(loc1.available_menus(1200))

b1 = Business("Basta Fazoolin'", [loc1, loc2, loc3])
