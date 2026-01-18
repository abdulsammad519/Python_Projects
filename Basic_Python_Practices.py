#Problem-01: Age Declaration
#Solution :
age=18
if age<13:
   print("child")
elif age>13 and age<19:
  print("Teenager")
elif age>=20 and age<59:
  print("Adult")
elif age>60:
   print("Senior")

#Problem#02: Movie Ticket Price
#Solution:
age=15
day="wednesday"
if age>=18:
   price=12
else:
   price=8
if day=="wednesday":
   price=price-2
   print(price)

#Problem 03:Student's score and progress
#Solution:
student_score=90
if  student_score>=90:
   grade="A"
elif student_score>=80:
   grade="B"
elif student_score>=70:
   grade="C"
elif student_score>=60:
   grade="D"
else:
   grade="F"
   
print("On the basis of student's score grade will be ",grade)

#Problem 04:Checking of fruit ripeness
#Solution:

color="Yellow"
Fruit="Bananna"
if color=="Green":
   Taste="unripe"
elif color=="Yellow":
   Taste="ripe"
elif color=="Brown":
   Taste="overripe"
else:
   print("on the base of your fruit and with given color, taste is not in our knowledge")

print(Taste)

#Problem 05: Activity according to weather's nature
#Solution:

Weather="Rainy"
if Weather=="Sunny":
   Activity="Go For A Walk"
elif Weather=="Rainy":
   Activity="Read A Book"
elif Weather=="Snowy":
   Activity="build a snowman"
else:
  Activity="invalid input"
  
print(Activity)

#Problem 06: Mode_of_Transportation according to Distance
#Solution:
  
Distance=43
if Distance<3:
   Mode_of_Transportation= "walk"
elif Distance<=15:
   Mode_of_Transportation= "bike"
else:
   Mode_of_Transportation= "car"


print(Mode_of_Transportation)

#Problem 07: Coffee Customization
#Solution:
  
order_size="medium"
extra_shot=True
if extra_shot:
   coffee=order_size+"coffee with an extra shot"
else:
   coffee=order_size+"coffee"

print(coffee)

#Problem 08: Animal specie with its Food checker
#Solution:
  
Animal_type = "Dog"
Dog_Age = 1
Cat_Age = 9

if Animal_type == "Dog":
    if Dog_Age < 2:
        Recommendation = "Puppy Food"
    else:
        Recommendation = "invalid input" 

elif Animal_type == "Cat":
    if Cat_Age > 5:
        Recommendation = "Senior Cat Food"
    else:
        Recommendation = "invalid input"
      
else:
  
    Recommendation = "Unknown Species"

print(f"For the {Animal_type}, the recommendation is: {Recommendation}")

#Problem 09: Password Checker
#Solution:

Password="Gangster@777"
if len(Password)<6:
   Nature_of_password="weak"
elif len(Password)>6 and len(Password)<10:
   Nature_of_password="Medium"
elif len(Password)>10:
   Nature_of_password="Strong"

print(f"your password:{Password} has {Nature_of_password} nature")


#Problem 10: Leap Year Checker
#Solution:

year = 2028
if (year % 4 == 0 and year % 400 == 0 ) or( year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")



#Prblem 11: print "hello world"
#solution:
print("Hello World")

#Prblem 12:Add two numbers
#solution:
num1=2
num2=4
add=num1+num2
print(add)

#Prblem 13:Find square root
#solution:
x=25
square_root=x**0.5
print(int(square_root))


#Prblem 14: Area of the triangle
#solution:
base=3
height=4
Area=0.5*base*height
print(Area)

#Prblem 15: Quadratic equation
#solution:
a=1
b=3
c=1
disc=b**2-4*a*c
if disc>0:
  sol1=-b+(b**2-4*a*c)**0.5/(2*a)
  sol2=-b-(b**2-4*a*c)**0.5/(2*a)
  print(f"for positive is : {sol1:.2f} \nand for negative is : {sol2:.2f}")
else:
  print("your discriminant is negative , cannot handle the complex numbers")

# Problem 16: Swap two variables
# solution:
a=4
b=5
temp=a
a=b
b=temp
print(a)
print(b)

# Problem 17: Make the power of the base
# solution:
base=2
for i in range(10):
   power_calculate=base**i
   print(f"{base} raised to the power {i} is : {power_calculate}")
   
# Problem 18: Get the random number
# solution:
import random
print(random.randint(0,9))

# Problem 19: Check number is positive or negative
# solution:
x=0
if x>0:
  print("number is positive")
elif x<0:
  print("number is negative")
else:
  print("number is equal to zero")
  
# Problem 20: Leap year
# solution:
year=2025
if (year%4==0 and year%100!=0) or(year%400==0):
   print("it is a leap year")
else:
   print("not a leap year")

# Problem 21: Even or odd
# solution:
x=3
print("even number") if x%2==0  else print("odd number")

# Problem 22: Convert KM into Miles
# solution:
distance_in_KM=230098456
if distance_in_KM>0:
   distance_in_Miles=distance_in_KM*0.621371
   print(distance_in_Miles)
else:
  print("distance is always positive ")

# Problem 23: Convert the temperature
# solution:

#Case 01: celsius into Farhenhiet
temp_in_C=37
temp_in_F=(temp_in_C*(9/5))+32
print(f"{temp_in_F:.2f}")

#Case 02: Farhenhiet into celsius
temp_in_F=45
temp_in_C=(temp_in_F-32)*(5/9)
print(f"{temp_in_C:.2f}")

# Problem 24: Print Prime numbers
# solution:
lower=900
upper=1000
for num in range(lower,upper+1):
   if num>1:
     for i in range(2,int(num**0.5)+1):
      if(num%i)==0:
       break
     else:
       print(num)
       
       
# Problem 25: Factorial of the Number
# solution:
fact=1
num=7
for i in range(1,num+1):
   fact=fact*num
   num=num-1
print(f"The factorial of given number is : {fact}")

# Problem 26: Check prime numbers
# solution:
num=15
if num>1:
 for i in range(2,num):
   if(num%i)==0:
    print(f"not a prime number because\n{i} times {num//i} is {num}") # tells the First priority,// is the modulus operator
    break
 else:
    print("prime number")
else:
   print("should be greater than 1")