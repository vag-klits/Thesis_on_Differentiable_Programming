import struct_and_math_functions as smf
import grad as gd

x=smf.primitive ("x", 8, "None", [])

a=x**(1/2)

print ("grad=", gd.grad (a, x))

# gradient of square root of x
# at x=8
