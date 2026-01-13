#use of greet function
#solution:

#case 1:
def greet(name):
  return "hello : "+name+"!"
name="chaudhary"
result=greet("chaudhary") #passing the values
print(result)

#case 2:
def greet(name="user"):  # alredy declared
  return "hello : "+name+"!"
name="chaudhary"
result=greet()       #not passing the values
print(result)