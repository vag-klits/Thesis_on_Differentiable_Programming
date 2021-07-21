import math
import struct_and_math_functions as smf


def add_sub_diff (x):
    if x.parents[1][0].isdigit ()==True:
        for i in smf.primitives_list:
            if i.name==x.parents[1]:
                break
        return [x.parents[0], None]
    return [x.parents[0], x.parents[1]]


def mult_diff (x, dx):
    if x.parents[1][0].isdigit ()==True:
        if x.parents[1].find ('.')>-1:
            num=float (x.parents[1])
        else:
            num=int (x.parents[1])
        for i in smf.primitives_list:
            if i.name==x.parents[1]:
                break
        smf.primitives_list.remove (i)
        dif=differentiate (x.parents[0], dx.name)
        return [num, dif, x.parents[0], None]


    dif1=differentiate (x.parents[0], dx.name)
    dif2=differentiate (x.parents[1], dx.name)

    for i in smf.primitives_list:
        if i.name==x.parents[0]:
            p0=i
        if i.name==x.parents[1]:
            p1=i

    if dif1==0:
        if dif2==0:
            return [0, None, None, None]
        else:
            return [p0.value, p1, None, None]
    else:
        if dif2==0:
            return [p1.value, p0, None, None]
        else:
            return [p1.value, p0, p1, p0.value]


def div_diff (x, dx):
    if x.parents[1][0].isdigit ()==True:
        if x.parents[1].find ('.')>-1:
            num=float (x.parents[1])
        else:
            num=int (x.parents[1])
        for i in smf.primitives_list:
            if i.name==x.parents[1]:
                break
        smf.primitives_list.remove (i)
        dif=differentiate (x.parents[0], dx.name)
        return [num, dif, x.parents[0], None, 1, None]

    if x.parents[0][0].isdigit ()==True:
        if x.parents[1].find ('.')>-1:
            num=float (x.parents[1])
        else:
            num=int (x.parents[1])
        for i in smf.primitives_list:
            if i.name==x.parents[0]:
                break
        smf.primitives_list.remove (i)
        dif=differentiate (x.parents[1], dx.name)
        return [num, dif, x.parents[1], None, 0, None]


    dif1=differentiate (x.parents[0], dx.name)
    dif2=differentiate (x.parents[1], dx.name)

    for i in smf.primitives_list:
        if i.name==x.parents[0]:
            p0=i
        if i.name==x.parents[1]:
            p1=i

    if dif1==0:
        if dif2==0:
            return [0, None, None, None, None, None]
        else:
            return [p0.value, p1, None, None, -1, p1.value]
    else:
        if dif2==0:
            return [p1.value, p0, None, None, 1, p1.value]
        else:
            return [p1.value, p0, p1, p0.value, None, p1.value]



def exp_dif (x, dx):
    dif1=differentiate (x.parents[0], dx.name)
    dif2=differentiate (x.parents[1], dx.name)
    if dif1==0:
        if dif2==0:
            return [None, None, None]
        else:
            if x.parents[0][0].isdigit ()==True:
                if x.parents[0].find ('.')>-1:
                    base=float (x.parents[0])
                else:
                    base=int (x.parents[0])
                for i in smf.primitives_list:
                    if i.name==x.parents[0]:
                        break
                smf.primitives_list.remove (i)
            else:
                for i in smf.primitives_list:
                    if i.name==x.parents[0]:
                        break
                base=i.value
            return [base, x.parents[1], "exp"]
    else:
        if dif2==0:
            if x.parents[1][0].isdigit ()==True:
                if x.parents[1].find ('.')>-1:
                    exp=float (x.parents[1])
                else:
                    exp=int (x.parents[1])
                for i in smf.primitives_list:
                    if i.name==x.parents[1]:
                        break
                smf.primitives_list.remove (i)
            else:
                for i in smf.primitives_list:
                    if i.name==x.parents[1]:
                        p=i
                        break
                exp=p.value
            return [exp, x.parents[0], "base"]


def sin_dif (x, dx):
    dif=differentiate (x.parents[0], dx.name)
    for i in smf.primitives_list:
        if i.name==x.parents[0]:
            xp=i
            break
    num=math.cos (xp.value)
    return [num, dif, xp]


def cos_dif (x, dx):
    dif=differentiate (x.parents[0], dx.name)
    for i in smf.primitives_list:
        if i.name==x.parents[0]:
            xp=i
            break
    num=math.sin (xp.value)
    num*=-1
    return [num, dif, xp]


def log_dif (x, dx):
    dif=differentiate (x.parents[0], dx.name)
    if dif==0:
        return [None, None]

    for i in smf.primitives_list:
        if i.name==x.parents[0]:
            xp=i
            break

    num=1/(xp.value*math.log (x.parents[1]))
    return [num, xp]

def ln_dif (x, dx):
    dif=differentiate (x.parents[0], dx.name)
    if dif==0:
        return [None, None]

    for i in smf.primitives_list:
        if i.name==x.parents[0]:
            xp=i
            break

    return [1/xp.value, xp]


def differentiate (d, dx):
    if d==None:
        return 0
    if d.find (dx)>-1:
        return 1
    else:
        return 0
    return 0
