#Class Inheritance and isinstance() Function
#(Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and Electric car)
 

class Car:
  total_num_car=0
  def __init__(self,name_of_car,brand,model):
    self.name_of_car=name_of_car
    self.brand=brand
    self.__model=model
    Car.total_num_car+=1
  def get_brand(self):
    return self.brand + "!"
  def full_name(self):
     return f"{self.__brand} {self.__model} {self.name_of_car}" 
  def fuel_type(self):
    return "petrol or diesel"
  @staticmethod
  def info_of_car(): 
    return "The specs of the car"
  @property
  def model(self):
    return self.__model
     
class ElectricCar(Car):
  def __init__(self,name_of_car,brand,model):
    super().__init__(name_of_car,brand,model)
  def fuel_type(self):
    return "electric"
My_car_info=Car("Model S","2020","Tesla") 
#print(My_car_info.fuel_type())
#Car("TATA","Safari","2003") 
#My_car_info.model="city"
#print(My_Sec_Car_info.fuel_type())
#print(Car.total_num_car)
#print(My_car_info.info_of_car())
#print(My_car_info.model())   
print(isinstance(My_car_info,Car))
print(isinstance(My_car_info,ElectricCar))

#isinstance() means tha it will check the given object is the part of the given class or not 