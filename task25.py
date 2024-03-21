from abc import ABC, abstractmethod
# Single Responsibility Principle
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Pricing:
    def __init__(self, book, price):
        self.book = book
        self.price = price

    def get_discount_price(self, discount):
        return self.price * (1 - discount)

# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Example usage
def process_payment(payment_processor: PaymentProcessor, amount):
    payment_processor.process_payment(amount)

# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle
class Vehicle:
    def energy_storage_info(self):
        raise NotImplementedError("Subclass must implement abstract method")

class FuelCar(Vehicle):
    def energy_storage_info(self):
        return "Fuel capacity is 100 liters"

class ElectricCar(Vehicle):
    def energy_storage_info(self):
        return "Battery capacity is 100 kWh"

# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle

class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self):
        pass

class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self):
        pass

class MusicPlayer(AudioPlayer):
    def play_audio(self):
        print("Playing audio...")

class VideoStreamingPlayer(AudioPlayer, VideoPlayer):
    def play_audio(self):
        print("Playing audio from video...")

    def play_video(self):
        print("Playing video...")

# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass


class ConsoleDisplay(Display):
    def show(self, data):
        print(data)


class WeatherStation:
    def __init__(self, display: Display):
        self.display = display

    def report(self):
        self.display.show("Weather Data")