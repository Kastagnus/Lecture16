from datetime import date
class Car:
    __number_of_cars = 0
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.__number_of_cars += 1
    def car_info(self):
        print(
            f"make of your car is {self.brand}, model of your car is {self.model}, year of your car is {self.year}")
    def age_of_car(self):
        age = date.today().year - int(self.year)
        return print(f"your vehicle age is {age}")

    @classmethod
    def total_cars(cls):
        return cls.__number_of_cars

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"your battery life is {self.battery_life} hrs")


car1 = Car("audi", "a4", "2010")
car2 = Car("mercedes", "c63", "2017")
car3 = ElectricCar("audi", "a7", "2015", "3000")
print(Car.total_cars())
car1.car_info()
car2.age_of_car()
car3.battery_info()


