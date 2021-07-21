import struct_and_math_functions as smf
import grad as gd

x=smf.primitive ("x", 40, "None", [])

y=smf.log (x, 3)

print ("grad=", gd.grad (y, x))

# gradient of log base 3 of x
# at x=40
