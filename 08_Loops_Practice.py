#Prime Number Checker:
#Solution:
number=19
is_prime=True
if number>1:
  for i in range(2,number):
      if (number%i)==0:
         is_prime=False
         break
print(f" prime number={is_prime}")