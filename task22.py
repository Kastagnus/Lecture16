import json
import pickle
import dill


class Animal():

    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

    def describe_pet(self):
        print(f"The animal details:\n\tName: {self.name}\n\tAge: {self.age}\n\tPet_type: {self.pet_type}")


myanimal = Animal("rex", "2", "Doggo")
student = {"name": "will", "age": "28", "university": "Cambridge"}
lambda_func = lambda x: x ** 3


def serialization(object, filename="object.csv"):
    pickle_ser = False
    dill_ser = False
    try:
        with open(filename, "w") as file:
            json.dump(object, file, indent=4)
        print("JSON was successful with serialization this object")
    except:
        print("Can not be serialized by JSON")
        pickle_ser = True

    while pickle_ser:
        try:
            with open(filename, 'wb') as file:
                pickle.dump(object, file)
                print("Pickle was successful with serialization this object")
                break
        except:
            dill_ser = True
            print("Can not be serialized by pickle")
            break
    while dill_ser:

        with open(filename, 'wb') as file:
            dill.dump(object, file)
            print("Dill was successful with serialization this object")
            break




def deserialization(filename="object.csv"):
    pickle_deser = False
    dill_deser = False
    try:
        with open(filename, 'r') as file:
            obj = json.load(file)
            print("JSON was successful with deserialization this object")
    except:
        print("Can not deserialized by JSON ")
        pickle_deser = True

    while pickle_deser:
        try:
            with open(filename, mode='rb') as file:
                obj = pickle.load(file)
                print("Pickle was successful with deserialization this object")
                break
        except:
            dill_deser = True
            print("Can not be deserialized by pickle ")
            break
    while dill_deser:
        with open(filename, mode='rb') as file:
            obj = dill.load(file)
            print("Dill was successful with deserialization this object")
            break

    return obj


# ჩაწერს და წაიკითხავს JSON-ი
serialization(student)
obj = deserialization("object.csv")
print(obj)

# ცდის ჩაწერას და წაკითხვას ჯეისნოთ, თუ არ გამოვიდა მიმართავს pickle-ს
serialization(myanimal)
obj = deserialization("object.csv")
obj.describe_pet()

#ცდის ჩაწერას ჯეისონით, მერე pickle-ით, ბოლოს თუ ესენი წარუმატებელია მიმართვს Dill-ს
serialization(lambda_func)
obj = deserialization("object.csv")
print(obj(2))


