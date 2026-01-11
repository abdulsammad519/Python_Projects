# Find the factorial of number
# solution:

factorial_of_num=5
factorial=1

print(f"{factorial_of_num}!=")
while factorial_of_num>0:
     factorial=factorial*factorial_of_num
     factorial_of_num=factorial_of_num - 1


print(factorial)