# Calcukating sum of even number upto n
# Solution:

n=10
sum_even=0
for i in range(1,n+1):
   if i%2==0:
     sum_even+=i
print("The sum of even numbers in the given range is : ",sum_even)
