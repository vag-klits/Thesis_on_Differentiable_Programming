import math

primitives_list=[]
is_reversed=False

class primitive:
    def __init__ (self, name, value, function, parents):
        self.value=value
        self.diff=None
        self.function=function
        self.parents=parents
        if function!="None":
            self.name=name
        else:
            self.name="$"+name+"$"

        primitives_list.append (self)
        return

    def insert_parent (self, x, y):
        self.parents.append (x)
        self.parents.append (y)
        return

    def myprint (self):
        print ("Node    :", self.name)
        print ("Value   :", self.value)
        print ("Function:", self.function)
        print ("Parents :", self.parents)
        print ("////////////////////////")

    def __add__ (self, other):
        if (isinstance(self, int) and isinstance(other, int)) or (isinstance(self, float) and isinstance(other, float)):
            return self+other

        if isinstance(self, int) or isinstance(self, float):
            new_name=str (self)+"+"+other.name
            res=self+other.value
            new_node=primitive (new_name, res, "Add", [str (self), other.name])
            num=primitive (str (self), self, None, [])
            primitives_list.append (num)

        elif isinstance(other, int) or isinstance(other, float):
            new_name=self.name+"+"+str (other)
            res=self.value+other
            new_node=primitive (new_name, res, "Add", [self.name, str (other)])
            num=primitive (str (other), other, None, [])
            primitives_list.append (num)

        else:
            new_name=self.name+"+"+other.name
            res=self.value+other.value
            new_node=primitive (new_name, res, "Add", [self.name, other.name])

        primitives_list.append (new_node)
        return new_node

    def __sub__ (self, other):
        if (isinstance(self, int) and isinstance(other, int)) or (isinstance(self, float) and isinstance(other, float)):
            return self-other

        if isinstance(self, int) or isinstance(self, float):
            new_name=str (self)+"-"+other.name
            res=self-other.value
            new_node=primitive (new_name, res, "Sub", [str (self), other.name])
            num=primitive (str (self), self, None, [])
            primitives_list.append (num)

        elif isinstance(other, int) or isinstance(other, float):
            new_name=self.name+"-"+str (other)
            res=self.value-other
            new_node=primitive (new_name, res, "Sub", [self.name, str (other)])
            num=primitive (str (other), other, None, [])
            primitives_list.append (num)

        else:
            new_name=self.name+"-"+other.name
            res=self.value-other.value
            new_node=primitive (new_name, res, "Sub", [self.name, other.name])

        primitives_list.append (new_node)
        return new_node


    def __mul__ (self, other):
        if (isinstance(self, int) and isinstance(other, int)) or (isinstance(self, float) and isinstance(other, float)):
            return self*other

        if isinstance(self, int) or isinstance(self, float):
            new_name=str (self)+"*"+other.name
            res=self*other.value
            new_node=primitive (new_name, res, "Mult", [str (self), other.name])
            num=primitive (str (self), self, None, [])
            primitives_list.append (num)

        elif isinstance(other, int) or isinstance(other, float):
            new_name=self.name+"*"+str (other)
            res=self.value*other
            new_node=primitive (new_name, res, "Mult", [self.name, str (other)])
            num=primitive (str (other), other, None, [])
            primitives_list.append (num)

        else:
            new_name=self.name+"*"+other.name
            res=self.value*other.value
            new_node=primitive (new_name, res, "Mult", [self.name, other.name])

        primitives_list.append (new_node)
        return new_node

    def __pow__ (self, other):
        if (isinstance(self, int) and isinstance(other, int)) or (isinstance(self, float) and isinstance(other, float)):
            return self**other

        if isinstance(self, int) or isinstance(self, float):
            new_name=str (self)+"^"+other.name
            res=self**other.value
            new_node=primitive (new_name, res, "Exp", [str (self), other.name])
            num=primitive (str (self), self, None, [])
            primitives_list.append (num)

        elif isinstance(other, int) or isinstance(other, float):
            new_name=self.name+"^"+str (other)
            res=self.value**other
            new_node=primitive (new_name, res, "Exp", [self.name, str (other)])
            num=primitive (str (other), other, None, [])
            primitives_list.append (num)

        else:
            new_name=self.name+"^"+other.name
            res=self.value**other.value
            new_node=primitive (new_name, res, "Exp", [self.name, other.name])

        primitives_list.append (new_node)
        return new_node

    def __truediv__ (self, other):
        if (isinstance(self, int) and isinstance(other, int)) or (isinstance(self, float) and isinstance(other, float)):
            return self/other

        if isinstance(self, int) or isinstance(self, float):
            new_name=str (self)+"/"+other.name
            res=self/other.value
            new_node=primitive (new_name, res, "Div", [str (self), other.name])
            num=primitive (str (self), self, None, [])
            primitives_list.append (num)

        elif isinstance(other, int) or isinstance(other, float):
            new_name=self.name+"/"+str (other)
            res=self.value/other
            new_node=primitive (new_name, res, "Div", [self.name, str (other)])
            num=primitive (str (other), other, None, [])
            primitives_list.append (num)

        else:
            new_name=self.name+"/"+other.name
            res=self.value/other.value
            new_node=primitive (new_name, res, "Div", [self.name, other.name])

        primitives_list.append (new_node)
        return new_node


def sin (x):
    if isinstance (x, int) or isinstance (x, float):
        return math.sin (x)

    new_name="sin(" + x.name + ")"
    res=math.sin (x.value)
    new_node=primitive (new_name, res, "Sin", [x.name])

    primitives_list.append (new_node)
    return new_node


def cos (x):
    if isinstance (x, int) or isinstance (x, float):
        return math.cos (x)

    new_name="cos(" + x.name + ")"
    res=math.cos (x.value)
    new_node=primitive (new_name, res, "Cos", [x.name])

    primitives_list.append (new_node)
    return new_node


def log (x, base):
    if isinstance (x, int) or isinstance (x, float):
        return math.log (x, base)

    new_name="log(" + x.name + ")"
    res=math.log (x.value, base)
    new_node=primitive (new_name, res, "Log", [x.name, base])

    primitives_list.append (new_node)
    return new_node


def ln (x):
    if isinstance (x, int) or isinstance (x, float):
        return math.log (x)

    new_name="ln(" + x.name + ")"
    res=math.log (x.value)
    new_node=primitive (new_name, res, "Ln", [x.name])

    primitives_list.append (new_node)
    return new_node
