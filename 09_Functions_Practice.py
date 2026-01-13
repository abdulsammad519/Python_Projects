#even number generator that yields the even numbers upto specified limit
#solution:
def even_generator(limit):
    for i in range(2,limit+1,2):
      yield i     # write 'return i' if you want numbers in the form of list
for num in even_generator(10):
      print(num)
      
# concept of yield--> it generates the value by running the program and take care of where it was in the memory, and aftersometime if it run again it will remember the place where it leaves and start it from that leaving place