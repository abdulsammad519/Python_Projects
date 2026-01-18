#Timing Function Execution:
#(Write a decorator that measures the time a function takes to execute)


#to calculate time:
import time
def timer(func):
  def wrapper(*args,**kwargs):
    start=time.time()
    result=func(*args,**kwargs)
    end=time.time()
    print(f"{func.__name__} ran in {end-start} time") #"__name__" tells you the name of the function automatically
    return result
  return wrapper

@timer #the example_function will never be called directly it has to pass through this decorator(@timer)
def example_function(n):
  time.sleep(n)
  
example_function(4)
  
  
  