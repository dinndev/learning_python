import string

my_list = ["test","ing"]
statement = "UCLA is the best UC in southern california"
excessive = "!!! test $ @ , !!!!"
too_much = "!!! test $ @ , !!!!"

#---------------------------------------------------------------------------------------
# Q1 STRING METHODS

# (a) join
joined_string = "*".join(my_list)

# (b) Replace
statement = statement.replace("UCLA","UCSD")

# (c) Replace for dropping characters
fixed = excessive.replace("!","")

# (d) Clearing all punctuation with replace

for character in string.punctuation:
     too_much = too_much.replace(character,"")

#---------------------------------------------------------------------------------------
# Q2 DEFAULT FUNCTIONS

# (a) Sort Keys
def sort_keys(dictonary, reverse_it = False):
    sorted_keys = sorted(dictonary.keys())
    if reverse_it :
        sorted_keys.reverse()
        return sorted_keys
    else :
        return sorted_keys


# (b) List Powers
def list_powers(collection, power = 2):
    power_list = []
    for number in collection :
       power_list.append(number ** power)
    return power_list
#---------------------------------------------------------------------------------------
  
# Q3 FUNCTIONS FOR LATER

# (a) Add lists

def add_lists(list1, list2) :
    zipped_lists = zip(list1,list2)
    output = []
    for (item1, item2) in zipped_lists :
        output.append(item1 + item2)
    return output

# (b) Check bounds

def check_bounds(position, size) :
    for element in position :
        if element < 0 or element >= size :
            return False
    return True

#---------------------------------------------------------------------------------------

# Q4 CREATING CLASS

class OfficeHours:
    def __init__(self,name, day, time, place):
        self.course = "COGS 18"
        self.name = name
        self.day = day
        self.time = time
        self.place = place
    def check(self):
        return "Prof " + self.name + "'s " + "office hours are on " + self.day + " at " + self.time + " at " + self.place
        # return "Prof {}'s office hours are on {} at {} at {}.".format(self.name, self.day, self.time, self.place)

Sam = OfficeHours("Sam", "Monday", "11:00", "Zoom")
Shivani = OfficeHours("Shivani", "Monday", "12:00", "Zoom")
Ethan = OfficeHours("Ethan", "Monday", "3:00", "CSB 114")
Holly = OfficeHours("Holly", "Tuesday", "10:00", "Mandeville")
Suzy = OfficeHours("Suzy", "Tuesday", "3:00", "CSB 114")
Prof = OfficeHours("Prof", "Wednesday", "9:30", "CSB Courtyard")
Matthew = OfficeHours("Matthew", "Wednesday", "1:00", "Zoom")
Donovan_and_Andrina = OfficeHours("Donovan_and_Andrina", "Thursday", "10:00", "Zoom")
Andrew = OfficeHours("Andrew", "Thursday", "2:00", "Zoom")

all_office_hours = [Sam, Shivani, Ethan, Holly, Suzy, Prof, Matthew, Donovan_and_Andrina, Andrew]


# (b) check_all

def check_all(list) :
    for office_hour in list :
        print(office_hour.check())


check_all(all_office_hours)  

#---------------------------------------------------------------------------------------

# Q5 CAR INVENTORY

class CarInventory :
    def __init__(self) :
        self.n_cars = 0
        self.cars = []
    
    def add_car(self, manufacturer, model, year, mpg) :
        car = {
            "manufacturer": manufacturer,
            "model": model,
            "year": year,
            "mpg": mpg
        }
        self.n_cars += 1
        self.cars.append(car)
    
    def compare(self, attribute, direction = 'highest') :
        highest = self.cars[0]
        lowest = self.cars[0]
        
        for car in self.cars :
            if car[attribute] < lowest[attribute] :
              lowest = car
            elif car[attribute] > highest[attribute] :
              highest = car
        if direction == "highest" :
            output = highest
            return output
        elif direction == "lowest" :
            output = lowest
            return output
    

# Using our class

inventory = CarInventory()
inventory.add_car("Ford", "Mustang",2004,20)
inventory.add_car("Honda", "Civic", 2014, 40)
inventory.add_car("Toyota", "Corolla", 2010, 50)
inventory.add_car("Tesla", "S", 2017, 1000)

highest_mpg = inventory.compare("mpg")["model"]
oldest_car = inventory.compare("year","lowest")["manufacturer"]

#---------------------------------------------------------------------------------------
