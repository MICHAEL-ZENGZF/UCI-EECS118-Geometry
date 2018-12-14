import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class perimeter_triangle:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.perimeter_triangle
        self.elist=elementlist
    def set_value(self,value=None):
        self.value=value
    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value !=None:
            return self.value
        else:
            echain.append(self.name)
            self.value =self.get_by_CED(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CED(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        E=self.elist[elements.E].get_pt(echain)
        D = self.elist[elements.D].get_pt(echain)

        if C is not None and E is not None\
                and D is not None:
            tri=Triangle(C,E,D)
            value=tri.perimeter
            return value

        return None

class perimeter_circle:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.perimeter_circle
        self.elist=elementlist
    def set_value(self,value=None):
        self.value=value
    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value !=None:
            return self.value
        else:
            echain.append(self.name)
            self.value =self.get_by_AR(echain)
            echain.remove(self.name)
            return self.value
    def get_by_AR(self,echain=[]):
        A=self.elist[elements.A].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)

        if A is not None and R is not None:
            cir=Circle(A,R)
            value=cir.perimeter
            return value

        return None