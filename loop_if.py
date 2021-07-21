import struct_and_math_functions as smf
import grad as gd

x=smf.primitive ("x", 6, "None", [])
y=smf.primitive ("y", 1, "None", [])

for i in range (4):
    y=y*x

if y.value>1:
    y+=x
else:
    y=x

print ("grad=", gd.grad (y, x))

# gradient of y=x*x*x*x + x=x^4+x
# at x=6
