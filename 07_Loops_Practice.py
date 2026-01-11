# Repeat the loop until the number is not in between 1 and 10
# Solution:
while True:
   number=int(input("enter a number between 1 and 10: "))
   if 1<=number<=10:
    print("you are in the range")
    break
   else:
     print("out of range!")    
   