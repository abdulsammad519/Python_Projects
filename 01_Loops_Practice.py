#  Counting Positive Numbers in a List
# Solution :

numbers=[1,2,3,4,5,6,7,8,-9,-8,-7,-6,-6,-5,5,4,-3]
positive_number_count=0
for num in numbers:
   if num>0:
        positive_number_count+=1
print(f"In your given list of numbers there are {positive_number_count} positive numbers")