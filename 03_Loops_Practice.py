# Prnt the table of given number and skip the fifth iteration 
# solution:

Table_of=10
print(f"Table of {Table_of} is: \n ")
for i in range(1,11):
    if i==5:
      continue
    print(f"{Table_of}x{i}={Table_of*i}")
   