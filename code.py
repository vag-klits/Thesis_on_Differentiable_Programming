import struct_and_math_functions as smf
import grad as gd


x=smf.primitive ("x", 7, "None", [])       #deleted false after number
y=smf.primitive ("y", 2, "None", [])


# smf.primitives_list.append (x)
# smf.primitives_list.append (y)

# a=x
# for i in range (1):
#     a+=x
#
# if a.value<0:
#     a=y
# else:
#     a=x*2

# b=y**x
# c=((x+1)**1.5)*4*x
# a=b/c


# b=x+1
# c=x+1
# a=c*b+y+c


# a=x**2
# b=y+1
# d=y+1
# c=a*b+d

# c=(x*5+z*10)/y-y**3+z

# a=x*5+z*10
# b=y**3
#
#
# c=a/y-b/x
# smf.primitives_list.reverse ()


# print ("//////")
#
# for i in primitives_list:
#     print (i.name)
#     break
#
# print ("//////")
a=x*2
b=smf.ln(a)
c=b+y

print ("grad=", gd.grad (c, x))
