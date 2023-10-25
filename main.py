class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"Starting the engine of {self.brand} {self.model}\n"
    def stop_engine(self):
        return f"Stopping the engine of {self.brand} {self.model}\n"


class Car(Vehicle):
    def __init__(self, brand, model, color, fuel_type):
        super().__init__(brand, model)
        self.color = color
        self.fuel_type = fuel_type

    def drive(self):
        return f"Driving the {self.color} {self.brand} {self.model}\n"

    def park(self):
        return f"Parking the {self.color} {self.brand} {self.model}\n"


class ElectricCar(Car):
    def __init__(self, brand, model, color, battery_capacity):
        super().__init__(brand, model, color, "Electric")
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"Charging the {self.color} {self.brand} {self.model} with a {self.battery_capacity} kWh battery\n"


vehicle = Vehicle("Toyota", "Camry")
print(vehicle.start_engine())
print(vehicle.stop_engine())


car = Car("Ford", "Focus", "Blue", "Gasoline")
print(car.start_engine())
print(car.drive())
print(car.park())


electric_car = ElectricCar("Tesla", "Model 3", "Red", 75)
print(electric_car.start_engine())
print(electric_car.drive())
print(electric_car.charge())