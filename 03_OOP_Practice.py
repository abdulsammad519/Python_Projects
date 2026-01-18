#Concept of Inheritance:
#(Create an electric car class that inherits from the car class and has an additional battery size)
class Car:
  def __init__(self,name_of_car,brand,model):
    self.name_of_car=name_of_car
    self.brand=brand
    self.model=model
  def full_name(self):
     return f"{self.brand} {self.model} {self.name_of_car}"
#Inheritance:
class ElectricCar(Car):
  def __init__(self,name_of_car,brand,model,battery_size):
    super().__init__(name_of_car,brand,model)
    self.battery_size=battery_size
My_car_info=ElectricCar("Model S","Tesla","2020","100kwh")
print(My_car_info. full_name() )
