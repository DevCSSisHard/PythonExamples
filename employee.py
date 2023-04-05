from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_pay(self):
        pass

    def __repr__(self):
        return ("Employee "+ self.name+ " ID number: "+ str(self.emp_id))


class HourlyEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __repr__(self):
        return ("Hourly Employee "+ self.name+ " ID number: "+ str(self.emp_id) + " earned "+ str(self.calculate_pay()))


class SalaryEmployee(Employee):
    def __init__(self, name, emp_id, annual_salary):
        super().__init__(name, emp_id)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 12

    def __repr__(self):
        return ("Salary Employee "+ self.name+ " ID number: "+ str(self.emp_id) + " earned " + str(self.annual_salary))
