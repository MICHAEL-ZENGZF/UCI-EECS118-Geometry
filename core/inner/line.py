import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class CE:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.CE
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
            self.value =self.get_by_CE(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CE(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        E=self.elist[elements.E].get_pt(echain)

        if C is not None and E is not None:
            value=C.distance(E)
            return value

        return None

class ED:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.ED
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
            self.value =self.get_by_ED(echain)
            echain.remove(self.name)
            return self.value
    def get_by_ED(self,echain=[]):
        D=self.elist[elements.D].get_pt(echain)
        E=self.elist[elements.E].get_pt(echain)

        if D is not None and E is not None:
            value=D.distance(E)
            return value

        return None

class DC:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.DC
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
            self.value =self.get_by_DC(echain)
            echain.remove(self.name)
            return self.value
    def get_by_DC(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)

        if C is not None and D is not None:
            value=C.distance(D)
            return value

        return None