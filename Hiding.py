# Encapsulation allows for the Hiding of the internal state and requiring all interactions to occur through well-defined
# interfaces this concept helps in data abstraction, data hiding and modularity in software design
# promoting better code
class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__year = year  # private attribute
        self.__is_started = False

    def start_engine(self):
        self.__is_started = True
        print("Engine started")

    def stop_engine(self):
        self.__is_started = False
        print("Engine stopped")

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def is_engine_started(self):
        return self.__is_started

my_car = Car("Toyota", "Fortuner", 2020)
print("MAKE :", my_car.get_make())
print("MODEL :", my_car.get_model())
print("YEAR :", my_car.get_year())

# If we access private key directly it give an error example below(Attribute error)
# print("MAKE:",my_car.__make)

my_car.start_engine()
print("Engine started :", my_car.is_engine_started())

my_car.stop_engine()
print("Engine started :", my_car.is_engine_started())
