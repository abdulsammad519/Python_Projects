#Polymorphism:
#(Demonstrate polymorphism by defining a method fuel_type in both car and electric car classes but with different behaviors)

class Car:
  def __init__(self,name_of_car,brand,model):
    self.name_of_car=name_of_car
    self.brand=brand
    self.model=model
  def get_brand(self):
    return self.brand + "!"
    
  def full_name(self):
     return f"{self.__brand} {self.model} {self.name_of_car}"
  def fuel_type(self):
    return "petrol or diesel"
     
class ElectricCar(Car):
  def __init__(self,name_of_car,brand,model):
    super().__init__(name_of_car,brand,model)
  def fuel_type(self):
    return "electric"
My_car_info=ElectricCar("Model S","2020","Tesla") # for inner class "ElectricCar"
print(My_car_info.fuel_type())
My_Sec_Car_info=Car("TATA","Safari","2003") # for the outer class "Car"
print(My_Sec_Car_info.fuel_type())

