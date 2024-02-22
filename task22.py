import json
import pickle


class Animal():

    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

    def describe_pet(self):
        print(f"The animal details:\n\tName: {self.name}\n\tAge: {self.age}\n\tPet_type: {self.pet_type}")


myanimal = Animal("rex", "2", "Doggo")
object = {"name": "will", "age": "28", "university": "Cambridge"}


def serialization(object, filename="object.csv"):
    pickle_ser = False
    try:
        with open(filename, "w") as file:
            json.dump(object, file, indent=4)
        print("JSON was successful with this object")
    except:
        print("Can not be serialized by JSON")
        pickle_ser = True

    while pickle_ser:
        with open(filename, 'wb') as file:
            pickle.dump(object, file)
            print("Pickle was successful with this object")
            break


def deserialization(filename="object.csv"):
    pickle_deser = False
    try:
        with open(filename, 'r') as file:
            object = json.load(file)
            print(object)
            print("JSON was successful with this object")
    except:
        print("Can not deserialized by JSON")
        pickle_deser = True

    while pickle_deser:
        with open(filename, mode='rb') as file:
            object = pickle.load(file)
            object.describe_pet()
            print("Pickle was successful with this object")
            break

# # ჩაწერს და წაიკითხავს JSON-ი
# serialization(object)
# deserialization("object.csv")

# # ცდის ჩაწერას და წაკითხვას ჯეისნოთ, თუ არ გამოვიდა მიმართავს pickle-ს
# serialization(myanimal)
# deserialization("object.csv")
