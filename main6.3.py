#Problem 3: Vehicle Rental
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


class Car(Vehicle):
    def calculate_rental(self, days):
        return super().calculate_rental(days) + 500  # fixed charge


class Bike(Vehicle):
    def calculate_rental(self, days):
        return super().calculate_rental(days)


class Truck(Vehicle):
    def calculate_rental(self, days):
        return super().calculate_rental(days) + (days * 200)  # extra load charge