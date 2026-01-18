#Class Method and Self
#(Add a method (make a function) to the car that displays the full name of the car (brand and model))


#with the help of function
class Car:
  def __init__(self,name_of_car,brand,model):
    self.name_of_car=name_of_car
    self.brand=brand
    self.model=model
    def full_name(self):
     return f"{self.brand} {self.model} {self.name_of_car}"
My_car_info=Car("Yaris","Toyota","2020(fresh import of 2026)")
print(My_car_info.name_of_car)
print(My_car_info.brand)
print(My_car_info.model)


#with the help of function:
class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def full_name(self):
    return f"{self.brand} {self.model}"
my_car=Car("Haval","H6")
print(my_car.brand)
print(my_car.model)