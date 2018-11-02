import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class EH:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.EH
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
            self.value =self.get_by_EH(echain)
            echain.remove(self.name)
            return self.value
    def get_by_EH(self,echain=[]):
        H=self.elist[elements.H].get_pt(echain)
        E=self.elist[elements.E].get_pt(echain)

        if H is not None and E is not None:
            value=H.distance(E)
            return value

        return None

class ID:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.ID
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
            self.value =self.get_by_ID(echain)
            echain.remove(self.name)
            return self.value
    def get_by_ID(self,echain=[]):
        D=self.elist[elements.D].get_pt(echain)
        I=self.elist[elements.I].get_pt(echain)

        if D is not None and I is not None:
            value=D.distance(I)
            return value

        return None

