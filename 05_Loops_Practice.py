# Repeating Characters Count
# Solution:
input_str="seee"

for char in input_str:
    print(char)
    if input_str.count(char)==1:
       print("first non repeated chaarcter is : ",char)
       break
    elif input_str.count(char)!=1:
      print("Every single character is repeated")