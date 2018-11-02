import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class C:

    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.C
        self.elist=elementlist
    def set_value(self,value=(None,None)):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
    def get_value(self):
        pt = self.get_pt()
        if pt is not None:
            self.value=(pt[0],pt[1])
        return self.value
    def get_pt(self,echain=[]):
        if self.name in echain:
            return None
        elif self.pt !=None:
            return self.pt
        else:
            echain.append(self.name)
            self.pt =self.get_by_EFGD(echain)
            echain.remove(self.name)
            return self.pt
    def get_by_EFGD(self,echain=[]):
        E=self.elist[elements.E].get_pt(echain)
        F=self.elist[elements.F].get_pt(echain)
        G=self.elist[elements.G].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)

        if E is not None and F is not None and\
            G is not None and D is not None:
            EF=Line(E,F)
            GD=Line(G,D)
            if not Line.is_parallel(EF,GD):
                pt=intersection(EF,GD)
                return pt

        return None

class E:
    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.E
        self.elist=elementlist
    def set_value(self,value=(None,None)):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
    def get_value(self):
        pt = self.get_pt()
        if pt is not None:
            self.value=(pt[0],pt[1])
        return self.value
    def get_pt(self,echain=[]):
        if self.name in echain:
            return None
        elif self.pt !=None:
            return self.pt
        else:
            echain.append(self.name)
            self.pt =self.get_by_CFDH(echain)
            echain.remove(self.name)
            return self.pt
    def get_by_CFDH(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        F=self.elist[elements.F].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)
        H=self.elist[elements.H].get_pt(echain)

        if C is not None and F is not None and\
            D is not None and H is not None:
            CF=Line(C,F)
            DH=Line(D,H)
            if not Line.is_parallel(CF,DH):
                pt=intersection(CF,DH)
                return pt

        return None

class D:
    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.D
        self.elist=elementlist
    def set_value(self,value=(None,None)):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
    def get_value(self):
        pt = self.get_pt()
        if pt is not None:
            self.value=(pt[0],pt[1])
        return self.value
    def get_pt(self,echain=[]):
        if self.name in echain:
            return None
        elif self.pt !=None:
            return self.pt
        else:
            echain.append(self.name)
            self.pt =self.get_by_CGHE(echain)
            echain.remove(self.name)
            return self.pt
    def get_by_CGHE(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        G=self.elist[elements.G].get_pt(echain)
        H=self.elist[elements.H].get_pt(echain)
        E=self.elist[elements.E].get_pt(echain)

        if C is not None and G is not None and\
            H is not None and E is not None:
            CG=Line(C,G)
            HE=Line(H,E)
            if not Line.is_parallel(CG,HE):
                pt=intersection(CG,HE)
                return pt
        return None
