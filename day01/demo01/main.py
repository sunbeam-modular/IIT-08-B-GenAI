import calculator
from calculator import multiply
import geomery as geo
import greeting

greeting.greet("Sachin")

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

calculator.add(num1, num2)
multiply(num1, num2)

geo.calc_rect_area(num1, num2)
geo.calc_rect_peri(num1, num2)
