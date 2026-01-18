#Addition of Class Variable
#(Add a class variable to car that keeps the number of the cars created)
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
     
class ElectricCar(Car):
  def __init__(self,name_of_car,brand,model):
    super().__init__(name_of_car,brand,model)
  def fuel_type(self):
    return "electric"
My_car_info=ElectricCar("Model S","2020","Tesla") # variables are only here for the hold of their reference n the memory 
print(My_car_info.fuel_type())
My_Sec_Car_info=Car("TATA","Safari","2003") 
print(My_Sec_Car_info.fuel_type())
print(Car.total_num_car)



#Note:
# some time your meory stores your return value and makes your output late the only reason is this is that the "garbage collector" did'nt 
# come immediately so sometimes you may have to close your system because the system holds the values in the memory for the optimization.

#"THERE IS NO IMMEDIATE GARBAGE COLLECTION IN PYTHON"
