#recursive function--> to calculate the factorial of number
#solution:
def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
print(f"the factorial  is : {factorial(5)}")
