import struct_and_math_functions as smf
import grad as gd

x=smf.primitive ("x", 10, "None", [])

y=smf.ln (x)

print ("grad=", gd.grad (y, x))

# gradient of y=ln(x)
# at x=10
