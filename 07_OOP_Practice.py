# Concept of Static Method:
#            "A method that belongs to a class rather than an instance of a class"     
   
#(Add a static method to the Car class that returns a general description of the car)

class Car:
  total_num_car=0
  def __init__(self,name_of_car,brand,model):
    self.name_of_car=name_of_car
    self.brand=brand
    self.model=model
    Car.total_num_car+=1
  def get_brand(self):
    return self.brand + "!"
  def full_name(self):
     return f"{self.__brand} {self.model} {self.name_of_car}" 
  def fuel_type(self):
    return "petrol or diesel"
  @staticmethod
  def info_of_car(): # self is not used bcz static method is a decorator and they do not deal with class
    return "The specs of the car"
     
class ElectricCar(Car):
  def __init__(self,name_of_car,brand,model):
    super().__init__(name_of_car,brand,model)
  def fuel_type(self):
    return "electric"
My_car_info=Car("Model S","2020","Tesla") 
#print(My_car_info.fuel_type())
Car("TATA","Safari","2003") 
#print(My_Sec_Car_info.fuel_type())
#print(Car.total_num_car)
#print(My_car_info.info_of_car())
print(Car.info_of_car())   # to run this statement we have to make "self" connection so for that we are using "@staticmethod"
