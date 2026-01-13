#use of keyword arguments ---> implementation of list "key:value"
#solution:
def print_kwargs(**kwargs):
   for key,value in kwargs.items():
     print(f"{key}:{value}")
print_kwargs(name="shark",power="animal")
print_kwargs(name="shark",power="lazer")