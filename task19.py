class Car:
    def __new__(cls, brand, model, year):

        print(f"Creating Car new instance.... with brand {brand}")
        return super().__new__(cls)

    def __init__(self, brand, model, year):
        self._brand = None
        self._model = None
        self._year = None
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand name must be a string")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model name must be a string")
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")
        if value < 1800:
            raise ValueError("Invalid year. The car's year must be 1800 or later.")
        self._year = value

try:
    car1 = Car("BMW", "3seris", 2015)
    print(f"created a car with brand {car1.brand}, model {car1.model}, year {car1.year}")
    car2 = Car("Audi", "RS4", 2010)
    print(f"created a car with brand {car2.brand}, model {car2.model}, year {car2.year}")
    car1.year = 2024
    car1.brand = "KIA"
    car1.model = "Optima"
    print(f"updated car with brand {car1.brand}, model {car1.model}, year {car1.year}")
    car2.year = 1750
    print(f"updated car with brand {car2.brand} to a new year {car2.year}")
except ValueError as e:
    print(e)