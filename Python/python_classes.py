class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{name} menu available from {start} to {end}".format(name=self.name, start=self.start_time, end=self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for i, j in self.items.items():
      for k in range(len(purchased_items)):
        if i == purchased_items[k]:
          bill += j
    return bill

brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, "11am", "4pm")

early_bird = Menu("early bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, "3pm", "6pm")

dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, "5pm", "11pm")

kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, "11am", "9pm")

print(kids)

total_bill1 = brunch.calculate_bill(["pancakes", "home fries", "coffee"])

total_bill2 = early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])

print(total_bill2)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def available_menus(self, time):
    real_time = 0
    if time.find("pm") > 0:
      real_time = int(time.strip("pm")) + 12
    else:
      real_time = int(time.strip("am"))

    for i in self.menus:
      start = 0
      if i.start_time.find("pm") > 0:
        start = int(i.start_time.strip("pm")) + 12
      else:
        start = int(i.start_time.strip("am"))

      end = 0
      if i.end_time.find("pm") > 0:
        end = int(i.end_time.strip("pm")) + 12
      else:
        end = int(i.end_time.strip("am"))
      
      if real_time >= start and real_time <= end:
        print(i.name)
      


flagship_store = Franchise("1232 West End Road",[brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street",[brunch, early_bird, dinner, kids])

flagship_store.available_menus("5pm")

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

new_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Take a’ Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10am", "8pm")

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepa_businees = Business("Take a' Arepa", [arepas_place])
