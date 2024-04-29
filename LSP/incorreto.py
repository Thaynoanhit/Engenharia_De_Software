class Vehicle:
    def move(self):
        print("O veículo está se movendo.")

class Car(Vehicle):
    def move(self):
        print("O carro está se movendo.")
        self.drive()  # Método específico de Car

    def drive(self):
        print("O carro está dirigindo.")

class Airplane(Vehicle):
    def move(self):
        print("O avião está decolando.")
        self.fly()  # Método específico de Airplane

    def fly(self):
        print("O avião está voando.")

def move_vehicle(vehicle: Vehicle):
    vehicle.move()

car = Car()
airplane = Airplane()

move_vehicle(car)  # Output: O carro está se movendo. O carro está dirigindo.
move_vehicle(airplane)  # Output: O avião está decolando. O avião está voando.