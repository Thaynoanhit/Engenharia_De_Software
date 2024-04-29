# Classe abstrata que define a interface para um veículo
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# Classe concreta que implementa a interface para um carro
class Car(Vehicle):
    def move(self):
        print("O carro está se movendo.")

# Classe concreta que implementa a interface para um avião
class Airplane(Vehicle):
    def move(self):
        print("O avião está decolando.")

# Função que pode trabalhar com qualquer veículo
def move_vehicle(vehicle: Vehicle):
    vehicle.move()

# Exemplo de uso
car = Car()
airplane = Airplane()

move_vehicle(car)  # Output: O carro está se movendo.
move_vehicle(airplane)  # Output: O avião está decolando.