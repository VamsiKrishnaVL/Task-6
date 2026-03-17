# Problem 3: Vehicle Rental System
# ---------------------------------

class Vehicle:
    """Base class for vehicles"""

    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        """Calculate rental cost"""
        return self.rental_rate * days


class Car(Vehicle):
    """Car rental with extra charge"""

    def __init__(self, model, rental_rate, insurance_fee):
        super().__init__(model, rental_rate)
        self.insurance_fee = insurance_fee

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.insurance_fee


class Bike(Vehicle):
    """Bike rental with discount"""

    def calculate_rental(self, days):
        total = self.rental_rate * days
        return total * 0.9  # 10% discount


class Truck(Vehicle):
    """Truck rental with load charge"""

    def __init__(self, model, rental_rate, load_charge):
        super().__init__(model, rental_rate)
        self.load_charge = load_charge

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.load_charge


# ----------- Testing -----------
print("\n--- Vehicle Rental Test ---")

vehicles = [
    Car("Honda City", 2000, 500),
    Bike("Yamaha", 500),
    Truck("Tata", 3000, 1000)
]

days = 3

for vehicle in vehicles:
    print(f"{vehicle.model} Rental Cost: {vehicle.calculate_rental(days)}")
