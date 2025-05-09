## Garage OOP Program (Vehicle Management System)
Team Members:
1. De Leon, Kate Hannah P.
2. Pasia, Rheman E.
3. Rubala, Micha A.
4. Talagtag, Karl Andrei C.

## System Description
This is an interactive console application designed to simulate the operation of various types of vehicles, including cars, buses, yachts, and trucks. The program utilizes object-oriented programming principles, specifically inheritance and abstraction, to create a flexible and extensible system for managing different vehicle types.

## How to Run the Program
1. Ensure you have Python installed on your device.
2. Copy the entire code of the Vehicle Management Program provided above into a text editor or an Integrated Development Environment (IDE) such as PyCharm or Visual Studio Code.
3. Save the file with a '.py' extension, for example, 'garage.py'.
4. Execute the program on the text editor or IDE.
5. Follow the on-screen prompts
   
   * Once the program starts, you will see a welcome message and a prompt to select a vehicle type.
   * Enter the corresponding number for the vehicle you wish to operate (1 for ```Car```, 2 for ```Bus```, 3 for ```Yacht```, 4 for ```Truck```) and press Enter.
   * Follow the subsequent prompts to enter the maximum number of passengers, fuel type, and whether you want to drive the vehicle. The program will guide you through the process.
   
6. After entering the required information, you can start the vehicle, fill it with fuel, and choose to drive it at a specified speed. The program will provide feedback based on your actions.
7. Once you are done interacting with the vehicle, the program will display a closing message. You can then close the terminal or command prompt window.

## Code Snippet

```python
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
```

| Name | Username |
|------|----------|
| Kate | [username](https://github.com/)|
