from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, speed, passenger_limit, fuel_type):
        self.speed = speed
        self.passenger_limit = passenger_limit
        self.fuel_type = fuel_type
        self.is_running = False
        self.has_gas = False

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def fill(self):
        pass

    @abstractmethod
    def operate(self):
        pass

    def get_speed(self):
        return self.speed
    
    def passenger_limit(self):
        return self.passenger_limit

    
    def fuel_type(self):
        return self.fuel_type
    
class Car(Vehicle):

    def __init__(self, speed, passenger_limit, fuel_type):
        super().__init__(speed, passenger_limit, fuel_type)

    def operate(self):
        print("You are now operating the [CAR] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the car with {self.fuel_type} gas.")
        else:
            print(f"The car is already filled.")
            
    def start(self):
        if not self.is_running and self.has_gas:
            self.is_running = True
            print("The car is now starting.")
        elif not self.has_gas:
            print("Fill the car with fuel first.")
        else:
            print("The car has already started.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print("The car has now stopped.")
        else:
            print("The car has already stopped.")

    def drive(self):
        if self.is_running and self.has_gas:
            print(f"You are now driving a car at a speed of {self.speed} km/h.")
        elif not self.is_running and not self.has_gas:
            print("Fill the car with gas first and then turn it on.")
        elif not self.is_running:
            print("Turn on the car first.")
        elif not self.has_gas:
            print("Fill the car with gas first.")
            
    def limit(self):
        print(f"The car can only accomodate {self.passenger_limit} people.")
        
class Bus(Vehicle):
    
    def __init__(self, speed, passenger_limit, fuel_type):
        super().__init__(speed, passenger_limit, fuel_type)
    
    def operate(self):
        print("You are now operating the [BUS] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the bus with {self.fuel_type} gas.")
        else:
            print(f"The bus is already filled.")
            
    def start(self):
        if not self.is_running and self.has_gas:
            self.is_running = True
            print("The bus is now starting.")
        elif not self.has_gas:
            print("Fill the bus with fuel first.")
        else:
            print("The bus has already started.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print("The bus has now stopped.")
        else:
            print("The bus has already stopped.")

    def drive(self):
        if self.is_running and self.has_gas:
            print(f"You are now driving a bus at a speed of {self.speed} km/h.")
        elif not self.is_running and not self.has_gas:
            print("Fill the bus with gas first and then turn it on.")
        elif not self.is_running:
            print("Turn on the bus first.")
        elif not self.has_gas:
            print("Fill the bus with gas first.")
            
    def limit(self):
        print(f"The bus can only accomodate {self.passenger_limit} people.")

class Yacht(Vehicle):
    
    def __init__(self, speed, passenger_limit, fuel_type):
        super().__init__(speed, passenger_limit, fuel_type)
    
    def operate(self):
        print("You are now operating the [YACHT] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the yacht with {self.fuel_type} gas.")
        else:
            print(f"The yacht is already filled.")
            
    def start(self):
        if not self.is_running and self.has_gas:
            self.is_running = True
            print("The yacht is now starting.")
        elif not self.has_gas:
            print("Fill the yacht with fuel first.")
        else:
            print("The yacht has already started.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print("The yacht has now stopped.")
        else:
            print("The yacht has already stopped.")

    def drive(self):
        if self.is_running and self.has_gas:
            print(f"You are now cruising a yacht at a speed of {self.speed} km/h.")
        elif not self.is_running and not self.has_gas:
            print("Fill the yacht with gas first and then turn it on.")
        elif not self.is_running:
            print("Turn on the yacht first.")
        elif not self.has_gas:
            print("Fill the yacht with gas first.")
            
    def limit(self):
        print(f"The yacht can only accomodate {self.passenger_limit} people.")

class Truck(Vehicle):
    
    def __init__(self, speed, passenger_limit, fuel_type):
        super().__init__(speed, passenger_limit, fuel_type)
    
    def operate(self):
        print("You are now operating the [TRUCK] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the truck with {self.fuel_type} gas.")
        else:
            print(f"The truck is already filled.")
            
    def start(self):
        if not self.is_running and self.has_gas:
            self.is_running = True
            print("The truck is now starting.")
        elif not self.has_gas:
            print("Fill the truck with fuel first.")
        else:
            print("The truck has already started.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print("The truck has now stopped.")
        else:
            print("The truck has already stopped.")

    def drive(self):
        if self.is_running and self.has_gas:
            print(f"You are now driving a truck at a speed of {self.speed} km/h.")
        elif not self.is_running and not self.has_gas:
            print("Fill the truck with gas first and then turn it on.")
        elif not self.is_running:
            print("Turn on the truck first.")
        elif not self.has_gas:
            print("Fill the truck with gas first.")
            
    def limit(self):
        print(f"The truck can only accomodate {self.passenger_limit} people.")


print("="*80)
print(f"{"Welcome to the [GARAGE]":^80}")
print("="*80)

print()

print("-"*80)
print(f"{"Select your Vehicle":^80}")
print(f"{"[1] Car [2] Bus [3] Yacht [4] Truck":^80}")
print("-"*80)

print()

while True:
    vehicle_choice = int(input("Vehicle Choice: "))

    if vehicle_choice == 1:

        print()
        passenger_limit = int(input("Enter max amount of passengers: "))
        fuel_type = input("Enter your fuel type: ")
        car1 = Car(0, passenger_limit, fuel_type)
        car1.operate()
        car1.limit()       
        print()
        print("Attempting to start the [CAR]...")
        print()
        car1.start()
        car1.fill()
        car1.start()
        print()
            
        while True:
            will_drive = input("Would you like to drive the [CAR]? Y/N: ").lower()
            if will_drive == "y":
                speed = int(input("How fast would you like to go? (in km/h): "))
                car1.speed = speed
                car1.drive()
                car1.stop()
                break
            elif will_drive == "n":
                car1.stop()
                break
            else:
                print("Invalid choice.\n")
        
        break

    elif vehicle_choice == 2:

        print()
        passenger_limit = int(input("Enter max amount of passengers: "))
        fuel_type = input("Enter your fuel type: ")
        bus1 = Bus(0, passenger_limit, fuel_type)
        bus1.operate()
        bus1.limit()       
        print()
        print("Attempting to start the [BUS]...")
        print()
        bus1.start()
        bus1.fill()
        bus1.start()
        print()
            
        while True:
            will_drive = input("Would you like to drive the [BUS]? Y/N: ").lower()
            if will_drive == "y":
                speed = int(input("How fast would you like to go? (in km/h): "))
                bus1.speed = speed
                bus1.drive()
                bus1.stop()
                break
            elif will_drive == "n":
                bus1.stop()
                break
            else:
                print("Invalid choice.\n")
        
        break
    

    elif vehicle_choice == 3:
        print()
        passenger_limit = int(input("Enter max amount of passengers: "))
        fuel_type = input("Enter your fuel type: ")
        yacht1 = Yacht(0, passenger_limit, fuel_type)
        yacht1.operate()
        yacht1.limit()       
        print()
        print("Attempting to start the [YACHT]...")
        print()
        yacht1.start()
        yacht1.fill()
        yacht1.start()
        print()
            
        while True:
            will_drive = input("Would you like to drive the [YACHT]? Y/N: ").lower()
            if will_drive == "y":
                speed = int(input("How fast would you like to go? (in km/h): "))
                yacht1.speed = speed
                yacht1.drive()
                yacht1.stop()
                break
            elif will_drive == "n":
                yacht1.stop()
                break
            else:
                print("Invalid choice.\n")
        
        break

    elif vehicle_choice == 4:
        print()
        passenger_limit = int(input("Enter max amount of passengers: "))
        fuel_type = input("Enter your fuel type: ")
        truck1 = Truck(0, passenger_limit, fuel_type)
        truck1.operate()
        truck1.limit()       
        print()
        print("Attempting to start the [TRUCK]...")
        print()
        truck1.start()
        truck1.fill()
        truck1.start()
        print()
            
        while True:
            will_drive = input("Would you like to drive the [TRUCK]? Y/N: ").lower()
            if will_drive == "y":
                speed = int(input("How fast would you like to go? (in km/h): "))
                truck1.speed = speed
                truck1.drive()
                truck1.stop()
                break
            elif will_drive == "n":
                truck1.stop()
                break
            else:
                print("Invalid choice.\n")
        
        break
    
    else:
        print("Invalid choice.")
        print()

print()
print("="*80)
print(f"{"[GARAGE PROGRAM] Closed":^80}")
print("="*80)