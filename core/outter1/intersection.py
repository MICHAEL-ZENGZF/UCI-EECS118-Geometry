import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class F:
    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.F
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
            self.pt =self.get_by_CEAR(echain)
            echain.remove(self.name)
            return self.pt
    def get_by_CEAR(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        E=self.elist[elements.E].get_pt(echain)
        A=self.elist[elements.A].get_pt(echain)
        R=self.elist[elements.R].get_value()

        if C is not None and E is not None and\
            A is not None and R is not None:
            CE=Line(C,E)
            O=Circle(A,R)
            i = intersection(CE, O)
            pt = [p for p in i if p != C]
            return pt[0]

        return None

class I:
    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.I
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
            self.pt =self.get_by_EDAR(echain)
            echain.remove(self.name)
            return self.pt
    def get_by_EDAR(self,echain=[]):
        E=self.elist[elements.E].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)
        A=self.elist[elements.A].get_pt(echain)
        R=self.elist[elements.R].get_value()

        if E is not None and D is not None and\
            A is not None and R is not None:
            ED=Line(E,D)
            O=Circle(A,R)
            i=intersection(ED,O)
            if i[0].distance(E)<i[1].distance(E):
                pt=i[0]
            else:
                pt=i[1]
            return pt

        return None

class H:
    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.H
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
            self.pt =self.get_by_EDAR(echain)
            echain.remove(self.name)
            return self.pt
    def get_by_EDAR(self,echain=[]):
        E=self.elist[elements.E].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)
        A=self.elist[elements.A].get_pt(echain)
        R=self.elist[elements.R].get_value()

        if E is not None and D is not None and\
            A is not None and R is not None:
            ED=Line(E,D)
            O=Circle(A,R)
            i=intersection(ED,O)
            if i[0].distance(E)<i[1].distance(E):
                pt=i[1]
            else:
                pt=i[0]
            return pt

        return None

class G:
    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.G
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
            self.pt =self.get_by_CDAR(echain)
            echain.remove(self.name)
            return self.pt
    def get_by_CDAR(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)
        A=self.elist[elements.A].get_pt(echain)
        R=self.elist[elements.R].get_value()

        if C is not None and D is not None and\
            A is not None and R is not None:
            CD=Line(C,D)
            O=Circle(A,R)
            i = intersection(CD, O)
            pt=[p for p in i if p!=C]
            return pt[0]

        return None