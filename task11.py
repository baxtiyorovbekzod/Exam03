class Vehicle:
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model
       
    def move(self):
        return "Vehicle is moving"
    
class Car(Vehicle):
    def move(self):
        return "Car is driving"
    
t1 = Vehicle("BMW", "Bike")
print(t1.move())

t2 = Car("Toyota", "Camry")
print(t2.move())