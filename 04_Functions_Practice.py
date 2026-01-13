#concept of returning multiple values
#solution:
import math
def circle_stats(radius):
  area=math.pi*radius**2
  circumference=2*math.pi*radius
  return area,circumference
a,c=circle_stats(5)
print(f"Area of circle is : {a:.2f} \ncircumference of the circle is : {c:.2f}")