#Basic Class and objects
#(create a car class with {attributes} like brand and model. Then create an {instance} of this class.)
                             #|->means variables                                #|->means object

class Car:
  def __init__(self,user_brand,user_model):
    self.brand=user_brand
    self.model=user_model
    
my_car=Car("Haval","H6")
print(my_car.brand)
print(my_car.model)
    
  
class Jeep:
  def __init__(self,year_of_deleivery,imported_country):
    self.year=year_of_deleivery
    self.country=imported_country
my_jeep=Jeep("2001","Japan")
print(my_jeep.country)
print(my_jeep.year)

class My_Tractor:
  def __init__(self,company_name,produce_country):
    self.company_name=company_name
    self.produce_country=produce_country
my_tractor=My_Tractor("Millat","Pakistan")#--->instance(calling a function) 
print(my_tractor.company_name)
print(my_tractor.produce_country)
my_tractor=My_Tractor("Henry's","England")
print(my_tractor.company_name)
print(my_tractor.produce_country)
