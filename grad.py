import differentiation_rules as df
import struct_and_math_functions as smf


def grad (f, x):
    if smf.is_reversed==False:
        smf.primitives_list.reverse ()
        smf.is_reversed==True
    f.myprint ()
    if f.name==x.name:
        return 1

    if f.function=="Add":
        [a, b]=df.add_sub_diff (f)

        for i in smf.primitives_list:
            if i.name==a:
                ap=i
            if b!=None and b==i.name:
                bp=i
            if i.name==f.name:
                fp=i

        d1=df.differentiate (ap.name, x.name)
        if b!=None:
            d2=df.differentiate (bp.name, x.name)

        for i in smf.primitives_list:
            for j in i.parents:
                if j==f.name:
                    i.parents.remove (j)

        if d1!=0:
            if b!=None:
                if d2!=0:
                    return d1*grad (ap, x)+d2*grad (bp, x)
            return d1*grad (ap, x)
        else:
            if b!=None:
                if d2!=0:
                    return d2*grad (bp, x)
            return 0
    elif f.function=="Sub":
        [a, b]=df.add_sub_diff (f)

        for i in smf.primitives_list:
            if i.name==a:
                ap=i
            if b!=None and b==i.name:
                bp=i
            if i.name==f.name:
                fp=i

        d1=df.differentiate (ap.name, x.name)
        if b!=None:
            d2=df.differentiate (bp.name, x.name)

        smf.primitives_list.remove (fp)
        for i in smf.primitives_list:
            for j in i.parents:
                if j==f.name:
                    i.parents.remove (j)

        if d1!=0:
            if b!=None:
                if d2!=0:
                    return d1*grad (ap, x)-d2*grad (bp, x)
            return d1*grad (ap, x)
        else:
            if b!=None:
                if d2!=0:
                    return (-1)*d2*grad (bp, x)
            return 0
    elif f.function=="Mult":
        [a,b,c,d]=df.mult_diff (f, x)
        for i in smf.primitives_list:
            if i.name==f:
                smf.primitives_list.remove (i)
                break

        if b==None:
            return 0
        else:
            if isinstance (b, int):
                if b==0:
                    return 0
                else:
                    for i in smf.primitives_list:
                        if i.name==c:
                            cp=i
                            break
                    return a*grad (cp, x)
            else:
                if c==None:
                    return a*grad (b, x)
                else:
                    return a*grad (b, x)+d*grad (c, x)
    elif f.function=="Div":
        [a,b,c,d,e,f]=df.div_diff (f, x)
        for i in smf.primitives_list:
            if i.name==f:
                smf.primitives_list.remove (i)
                break

        if b==None:
            return 0
        else:
            if isinstance (b, int):
                if b==0:
                    return 0
                else:
                    for i in smf.primitives_list:
                        if i.name==c:
                            cp=i
                            break

                    if e==1:
                        return grad (cp, x)/a
                    else:
                        a*=-1
                        return a*grad(cp, x)/cp.value**2
            else:
                if c==None:
                    return e*a*grad (b, x)/f**2
                else:
                    return (a*grad (b, x)-d*grad (c, x))/f**2
    elif f.function=="Exp":
        [a, b, c]=df.exp_dif (f, x)
        if b==None:
            return 0

        if c=="base":
            for i in smf.primitives_list:
                if i.name==b:
                    bp=i
                    break
            return a*(bp.value**(a-1))*grad (bp, x)

        if c=="exp":
            for i in smf.primitives_list:
                if i.name==b:
                    bp=i
                    break
            return (a**bp.value)*math.log (a)*grad (bp, x)

    elif f.function=="Sin":
        [a, b, c]=df.sin_dif (f, x)
        if b==0:
            return 0
        return a*grad (c, x)

    elif f.function=="Cos":
        [a, b, c]=df.cos_dif (f, x)
        if b==0:
            return 0
        return a*grad (c, x)

    elif f.function=="Log":
        [a, b]=df.log_dif (f, x)
        if a==None:
            return 0
        return a*grad (b, x)

    elif f.function=="Ln":
        [a, b]=df.ln_dif (f, x)
        if a==None:
            return 0
        return a*grad (b, x)

    if f.function=="None":
        print ("Unknown function")
        for i in smf.primitives_list:
            if i.name==f.name:
                break
        return 0

    if smf.primitives_list==[]:
        return 0

    return
