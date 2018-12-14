import numpy as np
from sympy import *
from sympy.geometry import *
from ..inner import angle as iangle
import elements

class Alpha(iangle.Alpha):
    def __init__(self, value=None,elementlist={}):
        super().__init__(value,elementlist)

        self.rule_set.extend(self.get_by_pt)
    def set_value(self,value=None):
        self.value=value

    def get_value(self, echain=[]):
        value=super().get_value(echain)
        return value

    def get_by_pt(self,echain):
        vertice=elements.D
        side1 = [elements.G, elements.C]
        side2 = [elements.H, elements.I, elements.E]
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

class Beta(iangle.Alpha):
    def __init__(self, value=None,elementlist={}):
        super().__init__(value,elementlist)

        self.rule_set.extend(self.get_by_pt)
    def set_value(self,value=None):
        self.value=value

    def get_value(self, echain=[]):
        value=super().get_value(echain)
        return value

    def get_by_pt(self,echain):
        vertice=elements.E
        side1 = [elements.F, elements.C]
        side2 = [elements.H, elements.I, elements.D]
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

class Gamma(iangle.Alpha):
    def __init__(self, value=None,elementlist={}):
        super().__init__(value,elementlist)

        self.rule_set.extend(self.get_by_pt)
    def set_value(self,value=None):
        self.value=value

    def get_value(self, echain=[]):
        value=super().get_value(echain)
        return value

    def get_by_pt(self,echain):
        vertice=elements.C
        side1 = [elements.G, elements.D]
        side2 = [elements.F, elements.E]
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