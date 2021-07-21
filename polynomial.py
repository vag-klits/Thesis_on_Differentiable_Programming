import struct_and_math_functions as smf
import grad as gd

x=smf.primitive ("x", 3, "None", [])

y=(x**6)*3-(x**2)*5+x

print ("grad=", gd.grad (y, x))

# gradient of y(x)=3*x^6 - 3*x^2 + x
# at x=3
