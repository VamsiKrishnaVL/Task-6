# Problem 2: Employee Management


class Employee:
    """Base class for employees"""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        """Method to calculate salary"""
        return self.salary


class RegularEmployee(Employee):
    """Full-time employee"""

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        """Salary includes bonus"""
        return self.salary + self.bonus


class ContractEmployee(Employee):
    """Contract-based employee"""

    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Salary based on hours worked"""
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    """Manager with incentives"""

    def __init__(self, name, salary, incentive):
        super().__init__(name, salary)
        self.incentive = incentive

    def calculate_salary(self):
        """Salary includes incentives"""
        return self.salary + self.incentive


# ----------- Testing -----------
print("\n--- Employee Management Test ---")

employees = [
    RegularEmployee("Vamsi", 30000, 5000),
    ContractEmployee("Ravi", 500, 40),
    Manager("Kiran", 50000, 10000)
]

for emp in employees:
    print(f"{emp.name} Salary: {emp.calculate_salary()}")
