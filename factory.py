from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)


# Абстрактний базовий клас
class Vehicle(ABC):
    def __init__(self, make, model, spec) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Класи автомобілів та мотоциклів, які успадковують Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


# Абстрактна фабрика для створення транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Motorcycle:
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


# Фабрика для ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
us_car.start_engine()

us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_engine()

eu_car = eu_factory.create_car("BMW", "3 Series")
eu_car.start_engine()
