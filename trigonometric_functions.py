import struct_and_math_functions as smf
import grad as gd
import math

p=math.pi/3

x=smf.primitive ("x", p, "None", [])

a=smf.sin (x)
b=smf.cos (x)

y=a*2-b*5

print ("grad=", gd.grad (y, x))

# gradient of y(x)=2*sin(x) - 5*cos(x)
# at x=pi/3
