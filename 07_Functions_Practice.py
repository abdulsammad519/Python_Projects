#Function with*args(arguments)-->"Find Sum"
#solution:
def sum_all(*args):   # '*' means to take and return multiple arguments
  print(args)
  for i in args:
    print(i*2)         
  return sum(args)         
print(sum_all(1,2))
print(sum_all(1,2,3,4,5,6,7,8))
