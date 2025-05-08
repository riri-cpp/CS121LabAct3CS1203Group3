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
    def __init__(self, speed, passenger_limit, fuel_type, trunk_capacity, convertible_roof, gps_enabled):
        super().__init__(speed, passenger_limit, fuel_type)
        self.trunk_capacity = trunk_capacity
        self.convertible_roof = convertible_roof
        self.gps_enabled = False

    def operate(self):
        print("You are now operating the [CAR] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the car with {self.fuel_type} gas.")
        else:
            print("The car is already filled.")
            
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
        print(f"The car can only accommodate {self.passenger_limit} people.")
    

    def show_trunk_capacity(self):
        print(f"The car has a trunk capacity of {self.trunk_capacity} liters.")

    def toggle_roof(self):
        if self.convertible_roof:
            print("The roof is already convertible. Toggling roof state...")
        else:
            print("This car does not have a convertible roof.")
    
    def is_roof_convertible(self):
        if self.convertible_roof:
            print("The car has a convertible roof.")
        else:
            print("The car does not have a convertible roof.")   
        

    def enable_gps(self):
        if not self.gps_enabled:
            self.gps_enabled = True
            print("GPS system enabled.")
        else:
            print("GPS system is already enabled.")

class Bus(Vehicle):
    def __init__(self, speed, passenger_limit, fuel_type, number_of_doors, wifi_enabled, route_number):
        super().__init__(speed, passenger_limit, fuel_type)
        self.number_of_doors = number_of_doors  
        self.wifi_enabled = wifi_enabled        
        self.route_number = route_number

    def operate(self):
        print("You are now operating the [BUS] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the bus with {self.fuel_type} gas.")
        else:
            print("The bus is already filled.")
            
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
        print(f"The bus can only accommodate {self.passenger_limit} people.")
    

    def door_info(self):
        print(f"The bus has {self.number_of_doors} doors.")


    def toggle_wifi(self):
        if self.wifi_enabled:
            self.wifi_enabled = False
            print("WiFi has been turned OFF.")
        else:
            self.wifi_enabled = True
            print("WiFi has been turned ON.")


    def change_route(self, new_route):
        print(f"Changing the route from {self.route_number} to {new_route}.")
        self.route_number = new_route
    
    def current_route(self):
        print(f"The bus is currently on route {self.route_number}.")
        
class Yacht(Vehicle):
    def __init__(self, speed, passenger_limit, fuel_type, length, number_of_cabins, radar_enabled):
        super().__init__(speed, passenger_limit, fuel_type)
        self.length = length                  
        self.number_of_cabins = number_of_cabins  
        self.radar_enabled = radar_enabled          

    def operate(self):
        print("You are now operating the [YACHT] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the yacht with {self.fuel_type} gas.")
        else:
            print("The yacht is already filled.")
            
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
        print(f"The yacht can only accommodate {self.passenger_limit} people.")
    

    def show_length(self):
        print(f"The yacht is {self.length} meters long.")


    def cabin_info(self):
        print(f"The yacht has {self.number_of_cabins} cabins onboard.")
    

    def toggle_radar(self):
        if not self.radar_enabled:
            self.radar_enabled = True
            print("RADAR has been activated.")
        else:
            print("RADAR is already activated.")

class Truck(Vehicle):
    def __init__(self, speed, passenger_limit, fuel_type, max_load, trailer_type, number_of_wheels):
        super().__init__(speed, passenger_limit, fuel_type)
        self.max_load = max_load
        self.trailer_type = trailer_type
        self.number_of_wheels = number_of_wheels

    def operate(self):
        print("You are now operating the [TRUCK] subclass.")

    def fill(self):
        if not self.has_gas:
            self.has_gas = True
            print(f"You filled the truck with {self.fuel_type} gas.")
        else:
            print("The truck is already filled.")
            
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
        print(f"The truck can only accommodate {self.passenger_limit} people.")
    
    def load_capacity(self):
        print(f"The truck can carry a maximum load of {self.max_load} kg.")

    def trailer_info(self):
        print(f"The truck is using a {self.trailer_type} trailer.")
    
    def change_trailer(self, new_trailer_type):
        print(f"Changing trailer from {self.trailer_type} to {new_trailer_type}.")
        self.trailer_type = new_trailer_type

    def show_wheels(self):
        print(f"The truck is a {self.number_of_wheels} wheeler.")

def main():        
    print("="*80)
    print(f"{"Welcome to the [GARAGE]":^80}")
    print("="*80)

    print()

    print(f"{"Select your Vehicle":^80}")
    print(f"{"[1] Car [2] Bus [3] Yacht [4] Truck":^80}")


    while True:
        print()
        vehicle_choice = input("Vehicle Choice (Q to quit): ").lower()

        if vehicle_choice == "1":

            print()
            passenger_limit = int(input("Enter max amount of passengers: "))
            fuel_type = input("Enter your fuel type: ")
            trunk_capacity = int(input("Enter the trunk capacity in liters: "))
            
            while True:
                is_convertible = input("Is the car a convertible? (Y/N): ").lower()
                if is_convertible == "y":
                    is_convertible = True
                    break
                elif is_convertible == "n":
                    is_convertible = False
                    break
                else:
                    print("Invalid input.")

            car1 = Car(0, passenger_limit, fuel_type, trunk_capacity, is_convertible, False)

            print()

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
                    print()
                    car1.drive()

                    while True:
                        print()
                        toggle_gps = input("Would you like to enable GPS? (Y/N): ").lower()
                        print()
                        if toggle_gps == "y":
                            car1.enable_gps()
                            break
                        elif toggle_gps == "n":
                            print("GPS is not enabled.")
                            break
                        else:
                            print("Invalid input.")
                    
                    while True:
                        print()
                        toggle_roof = input("Would you like to toggle the roof? (Y/N): ").lower()
                        print()
                        if toggle_roof == "y":
                            car1.toggle_roof()
                            break
                        elif toggle_roof == "n":
                            print("The car's roof is not toggled.")
                            break
                        else:
                            print("Invalid input.")
                    
                    while True:
                        print()
                        will_stop = input("Would you like to stop the car? (Y/N): ").lower()
                        print()
                        if will_stop == "y":
                            car1.stop()
                            break
                        elif will_stop == "n":
                            print("You are still driving the car.")
                        else:
                            print("Invalid input.")
                    
                    break

                elif will_drive == "n":
                    print()
                    car1.stop()
                    break
                else:
                    print("Invalid choice.\n")
            

        elif vehicle_choice == "2":

            print()
            passenger_limit = int(input("Enter max amount of passengers: "))
            fuel_type = input("Enter your fuel type: ")
            doors = int(input("Enter number of doors: "))
            route = int(input("Enter route number: "))

            bus1 = Bus(0, passenger_limit, fuel_type, doors, False, route)

            print()

            bus1.operate()
            bus1.limit()  
            bus1.door_info()     
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
                    print()
                    bus1.drive()

                    while True:
                        print()
                        toggle_wifi = input("Would you like to toggle the WiFi? (Y/N): ")
                        print()
                        if toggle_wifi == "y":
                            bus1.toggle_wifi()
                            break
                        elif toggle_wifi == "n":
                            print("Wifi has not been turned on.")
                            break
                        else:
                            print("Invalid input.")
                    
                    while True:
                        print()
                        change_route = input("Would you like to change the route? (Y/N): ")
                        print()
                        if change_route == "y":
                            new_route = input("Enter the new route to take: ")
                            print()
                            bus1.change_route(new_route)
                            break
                        elif change_route == "n":
                            print("Route has not been changed.")
                            break
                        else:
                            print("Invalid input.")

                    while True:
                        print()
                        will_stop = input("Would you like to stop the bus?: ")
                        print()
                        if will_stop == "y":
                            bus1.stop()
                            break    
                        elif will_stop == "n":
                            print("You are still driving the bus.")
                        else:
                            print("Invalid input.")
                    
                    break
                
                elif will_drive == "n":
                    bus1.stop()
                    break
                else:
                    print("Invalid choice.\n")
            
        
        elif vehicle_choice == "3":
            print()
            passenger_limit = int(input("Enter max amount of passengers: "))
            fuel_type = input("Enter your fuel type: ")
            length = int(input("Enter the yacht's length in meters: "))
            cabins = int(input("Enter number of cabins: "))
            
            yacht1 = Yacht(0, passenger_limit, fuel_type, length, cabins, False)
            
            print()

            yacht1.operate()
            yacht1.show_length()
            yacht1.cabin_info()
            yacht1.limit()
            print()
            print("Attempting to start the [YACHT]...")
            print()
            yacht1.start()
            yacht1.fill()
            yacht1.start()
            print()
                
            while True:
                will_drive = input("Would you like to drive the [YACHT]? (Y/N): ").lower()
                if will_drive == "y":
                    speed = int(input("How fast would you like to go? (in km/h): "))
                    yacht1.speed = speed
                    print()
                    yacht1.drive()
                    
                    while True:
                        print()
                        activate_radar = input("Would you like to activate the RADAR? (Y/N): ").lower()
                        print()
                        if activate_radar == "y":
                            yacht1.toggle_radar()
                            break
                        elif activate_radar == "n":
                            print("RADAR has not been enabled.")
                            break
                        else:
                            print("Invalid input.")
                    
                    while True:
                        print()
                        will_stop = input("Would you like to stop the yacht?: ")
                        print()
                        if will_stop == "y":
                            yacht1.stop()
                            break    
                        elif will_stop == "n":
                            print("You are still driving the yacht.")
                        else:
                            print("Invalid input.")

                    break

                elif will_drive == "n":
                    yacht1.stop()
                    break
                else:
                    print("Invalid choice.\n")
            

        elif vehicle_choice == "4":
            print()
            passenger_limit = int(input("Enter max amount of passengers: "))
            fuel_type = input("Enter your fuel type: ")
            load_capacity = int(input("Enter the maximum load to carry: "))
            trailer = input("Enter your trailer type: ")
            num_wheels = int(input("Enter the number of wheels: "))
            truck1 = Truck(0, passenger_limit, fuel_type, load_capacity, trailer, num_wheels)
            
            print()

            truck1.operate()
            truck1.limit()
            truck1.load_capacity()
            truck1.trailer_info()
            truck1.show_wheels()       
            print()
            print("Attempting to start the [TRUCK]...")
            print()
            truck1.start()
            truck1.fill()
            truck1.start()
            print()
                
            while True:
                will_drive = input("Would you like to drive the [TRUCK]? (Y/N): ").lower()
                if will_drive == "y":
                    speed = int(input("How fast would you like to go? (in km/h): "))
                    print()
                    truck1.speed = speed
                    truck1.drive()

                    while True:
                        print()
                        change_trailer = input("Would you like to change your trailer type? (Y/N): ").lower()
                        print()
                        if change_trailer == "y":
                            new_trailer = input("What would you like to change the trailer type to?: ")
                            print()
                            truck1.change_trailer(new_trailer)
                            break
                        elif change_trailer == "n":
                            print("Trailer type has not been changed.")
                            break
                        else:
                            print("Invalid input.")
                    
                    while True:
                        print()
                        will_stop = input("Would you like to stop the truck?: ")
                        print()
                        if will_stop == "y":
                            truck1.stop()
                            break    
                        elif will_stop == "n":
                            print("You are still driving the truck.")
                        else:
                            print("Invalid input.")

                    break

                elif will_drive == "n":
                    truck1.stop()
                    break

                else:
                    print("Invalid choice.\n")
            
        elif vehicle_choice == "q":
            break

        else:
            print("Invalid choice.")

    print()
    print("="*80)
    print(f"{"[GARAGE PROGRAM] Closed":^80}")
    print("="*80)

main()