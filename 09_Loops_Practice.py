# Find repetitive item in the list
# solution:

items_in_list=["apple","bananna","orange","apple","mango"]
unique_item=set()
for item in items_in_list:
    if item in unique_item:
      print("Duplicate item found: ",item)
      break
    unique_item.add(item)
    