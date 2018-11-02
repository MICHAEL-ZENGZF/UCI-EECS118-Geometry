import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class CF:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.CF
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
            self.value =self.get_by_CF(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CF(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        F=self.elist[elements.F].get_pt(echain)

        if C is not None and F is not None:
            value=C.distance(F)
            return value

        return None

class FE:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.FE
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
            self.value =self.get_by_FE(echain)
            echain.remove(self.name)
            return self.value
    def get_by_FE(self,echain=[]):
        E=self.elist[elements.E].get_pt(echain)
        F=self.elist[elements.F].get_pt(echain)

        if E is not None and F is not None:
            value=E.distance(F)
            return value

        return None

class EI:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.EI
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
            self.value =self.get_by_EI(echain)
            echain.remove(self.name)
            return self.value
    def get_by_EI(self,echain=[]):
        E=self.elist[elements.E].get_pt(echain)
        I=self.elist[elements.I].get_pt(echain)

        if E is not None and I is not None:
            value=E.distance(I)
            return value

        return None

class IH:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.IH
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
            self.value =self.get_by_IH(echain)
            echain.remove(self.name)
            return self.value
    def get_by_IH(self,echain=[]):
        H=self.elist[elements.H].get_pt(echain)
        I=self.elist[elements.I].get_pt(echain)

        if H is not None and I is not None:
            value=H.distance(I)
            return value

        return None

class HD:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.HD
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
            self.value =self.get_by_HD(echain)
            echain.remove(self.name)
            return self.value
    def get_by_HD(self,echain=[]):
        H=self.elist[elements.H].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)

        if H is not None and D is not None:
            value=H.distance(D)
            return value

        return None

class DG:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.DG
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
            self.value =self.get_by_DG(echain)
            echain.remove(self.name)
            return self.value
    def get_by_DG(self,echain=[]):
        G=self.elist[elements.G].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)

        if G is not None and D is not None:
            value=G.distance(D)
            return value

        return None

class GC:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.GC
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
            self.value =self.get_by_GC(echain)
            echain.remove(self.name)
            return self.value
    def get_by_GC(self,echain=[]):
        G=self.elist[elements.G].get_pt(echain)
        C=self.elist[elements.C].get_pt(echain)

        if G is not None and C is not None:
            value=G.distance(C)
            return value

        return None