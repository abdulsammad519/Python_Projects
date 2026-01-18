#Scopes or Namespace
# 1.global Variables
# 2.local  Variables


#Example_01:
username="Abdul Sammad"  #global Variable

def scope_fun():
  username="gangster"
  print(username)
print(username)      #will print "Abdul Sammad" because the function is not called
scope_fun()



#Example_02:
x=99
def func(y):
  z=x+y
  return z
result=func(1) # by inputing the value of y it is getting the value in the result which the function "func()" is returning
print(result)

#Example_03:
x=88
def func():
  global x
  x=12
func()
print(x)

#Example_04:
x=99
def f1():
  x=88
  def f2():
    print(x)   # if "x=88" is removed then we will use the global value x "x=99"
  f2()
f1()

#Example_05:
def f1():
  x=88
  def f2():
     print(x)
  return f2
result=f1()
result()


#Example_06:
def chaicoder(num):
  def actual(x):  #The mechanism of closure in this function is that the inner function 
    #"actual(x)" has access to the variable "num" from the enclosing scope of the outer function 
    # "chaicoder(num)". This allows "actual(x)" to use "num" even after "chaicoder(num)" 
    # has finished executing.
    return x**num
  return actual
f=chaicoder(3)    # here num=3
g=chaicoder(2)    # here num=2

print(f(5))  # here x=5
print(g(5)) 



#Example_07:
def function(x):
  def actual(num):
    return x**num
  return actual
a=function(3)
b=function(4)# gives x

print(a(2)) #gives num
print(b(2))


#Example_08:
def myfunc(x):
  def actual(y):
    return x**y
  return actual

a=myfunc(4) #x
b=myfunc(5)

print(a(2)) #y
print(b(3))
