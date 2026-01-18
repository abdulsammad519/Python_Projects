#Concept of Encapsulation:
#(Modify the car  class to encapsulate the brand attribute,making it private, and provide a getter method for it)
class Car:
  def __init__(self,name_of_car,brand,model):
    self.name_of_car=name_of_car
    self.__brand=brand
    self.model=model
  def chai_brand(self):
    return self.__brand + "!"
    
  def full_name(self):
     return f"{self.__brand} {self.model} {self.name_of_car}"
     
class ElectricCar(Car):
  def __init__(self,name_of_car,brand,model,battery_size):
    super().__init__(name_of_car,brand,model)
    self.battery_size=battery_size
My_car_info=ElectricCar("Model S","Tesla","2020","100kwh")
print(My_car_info. full_name() )
#print(My_car_info.chai_brand()) # to call alone the brand name you have to call this function

