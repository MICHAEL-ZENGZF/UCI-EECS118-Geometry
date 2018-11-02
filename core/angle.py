import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class Alpha:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.Alpha
        self.elist=elementlist
    def set_value(self,value=None):
        self.value=value
    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value is not None:
            return self.value
        else:
            rs=[]
            echain.append(self.name)
            side1=[elements.G,elements.C]
            side2=[elements.H,elements.I,elements.E]
            rs.extend(self.get_by_pt(elements.D,side1,side2,echain))

            echain.remove(self.name)

            if len(rs)>0:
                self.value=rs[0]
            return self.value

    def get_by_pt(self,vertice,side1,side2,echain):
        sets=[(A,B) for A in side1 for B in side2]
        rs=[]
        for set in sets:
            A,B=set
            V=self.elist[vertice].get_pt(echain)
            A = self.elist[A].get_pt(echain)
            B = self.elist[B].get_pt(echain)
            if V is not None and A is not None and \
                    B is not None:
                VA = Line(V, A)
                VB = Line(V, B)
                value = VA.smallest_angle_between(VB).evalf()
                rs.append(value)

        return rs


class Beta:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.Beta
        self.elist=elementlist
    def set_value(self,value=None):
        self.value=value
    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value is not None:
            return self.value
        else:
            rs=[]
            echain.append(self.name)
            side1=[elements.F,elements.C]
            side2=[elements.H,elements.I,elements.D]
            rs.extend(self.get_by_pt(elements.E,side1,side2,echain))

            echain.remove(self.name)
            if len(rs)>0:
                self.value=rs[0]
            return self.value

    def get_by_pt(self,vertice,side1,side2,echain):
        sets=[(A,B) for A in side1 for B in side2]
        rs=[]
        for set in sets:
            A,B=set
            V=self.elist[vertice].get_pt(echain)
            A = self.elist[A].get_pt(echain)
            B = self.elist[B].get_pt(echain)
            if V is not None and A is not None and \
                    B is not None:
                VA = Line(V, A)
                VB = Line(V, B)
                value = VA.smallest_angle_between(VB)
                rs.append(value)

        return rs

class Gamma:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.Gamma
        self.elist=elementlist
    def set_value(self,value=None):
        self.value=value
    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value is not None:
            return self.value
        else:
            rs=[]
            echain.append(self.name)
            side1=[elements.G,elements.D]
            side2=[elements.F,elements.E]
            rs.extend(self.get_by_pt(elements.C,side1,side2,echain))

            echain.remove(self.name)
            if len(rs)>0:
                self.value=rs[0]
            return self.value

    def get_by_pt(self,vertice,side1,side2,echain):
        sets=[(A,B) for A in side1 for B in side2]
        rs=[]
        for set in sets:
            A,B=set
            V=self.elist[vertice].get_pt(echain)
            A = self.elist[A].get_pt(echain)
            B = self.elist[B].get_pt(echain)
            if V is not None and A is not None and \
                    B is not None:
                VA = Line(V, A)
                VB = Line(V, B)
                value = VA.smallest_angle_between(VB)
                rs.append(value)

        return rs