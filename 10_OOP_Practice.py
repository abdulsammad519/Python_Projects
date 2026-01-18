#Multiple Inheritance:
#(create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance)


class Car:
  def __init__(self,user_brand,user_model):
    self.brand=user_brand
    self.model=user_model
class Battery:
  def battery_info(self):
    return "this is battery"
  
  
class Engine:
  def engine_info(self):
    return "this is engine"

class Electricvehicle(Battery,Engine,Car):
  pass
my_new_sawari=Electricvehicle("Tesla","Model S")
print(my_new_sawari.engine_info())
print(my_new_sawari.battery_info())