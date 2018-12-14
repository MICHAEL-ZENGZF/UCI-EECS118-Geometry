import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class area_triangle:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.area_triangle
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
            self.value =self.get_by_CDE(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CDE(self,echain=[]):
        C=self.elist[elements.C].get_pt(echain)
        D=self.elist[elements.D].get_pt(echain)
        E=self.elist[elements.E].get_pt(echain)

        if C is not None and D is not None\
                and E is not None:
            tri=Triangle(C,D,E)
            if(isinstance(tri,polygon.Triangle)):
                value=tri.area
                return value

        return None

class area_circle:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.area_circle
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
            value=cir.area
            return value
        return None

class S1:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.S1
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
            self.value =self.get_by_CAGRARC1(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CAGRARC1(self,echain=[]):
        C = self.elist[elements.C].get_pt(echain)
        A=self.elist[elements.A].get_pt(echain)
        G = self.elist[elements.G].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)
        ARC1=self.elist[elements.ARC1].get_value(echain)

        if A is not None and R is not None\
                and C is not None and G is not None\
                and ARC1 is not None:
            CirSec=ARC1*R/2
            tri=Triangle(C,A,G)
            value=CirSec-tri.area
            return value
        return None

class S2:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.S2
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
            self.value =self.get_by_CAFRARC2(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CAFRARC2(self,echain=[]):
        C = self.elist[elements.C].get_pt(echain)
        A=self.elist[elements.A].get_pt(echain)
        F = self.elist[elements.F].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)
        ARC2=self.elist[elements.ARC2].get_value(echain)

        if A is not None and R is not None \
                and C is not None and F is not None \
                and ARC2 is not None:
            CirSec=ARC2*R/2
            tri=Triangle(C,A,F)
            value=CirSec-tri.area
            return value
        return None

class S3:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.S2
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
            self.value =self.get_by_IAHRARC4(echain)
            echain.remove(self.name)
            return self.value
    def get_by_IAHRARC4(self,echain=[]):
        I = self.elist[elements.I].get_pt(echain)
        A = self.elist[elements.A].get_pt(echain)
        H = self.elist[elements.H].get_pt(echain)
        R = self.elist[elements.R].get_value(echain)
        ARC4=self.elist[elements.ARC4].get_value(echain)

        if A is not None and R is not None \
                and I is not None and H is not None \
                and ARC4 is not None:
            CirSec=ARC4*R/2
            tri=Triangle(I,A,H)
            value=CirSec-tri.area
            return value
        return None

class S4:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.S4
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
            self.value =self.get_by_S1S2S3AreaCir(echain)
            echain.remove(self.name)
            return self.value
    def get_by_S1S2S3AreaCir(self,echain=[]):
        S1=self.elist[elements.S1].get_value()
        S2=self.elist[elements.S2].get_value()
        S3=self.elist[elements.S3].get_value()
        AreaCir=self.elist[elements.area_circle].get_value()

        if S1 is not None and S2 is not None \
                and S3 is not None and AreaCir is not None:

            value=AreaCir-S1-S2-S3
            return value
        return None

class S5:
    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.S5
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
            self.value =self.get_by_AFEIRARC3(echain)
            echain.remove(self.name)
            return self.value
    def get_by_AFEIRARC3(self,echain=[]):
        F=self.elist[elements.F].get_pt()
        E = self.elist[elements.E].get_pt()
        A = self.elist[elements.A].get_pt()
        I = self.elist[elements.I].get_pt()
        R = self.elist[elements.R].get_value()
        ARC3=self.elist[elements.ARC3].get_value()

        if F is not None and E is not None \
                and A is not None and I is not None \
                and R is not None and ARC3 is not None:
            poly=Polygon(F,E,A,I)
            CirSec=R*ARC3/2
            value=poly-CirSec
            return value
        return None

class S6:
    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.S6
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
            self.value =self.get_by_DGAHRARC5(echain)
            echain.remove(self.name)
            return self.value
    def get_by_DGAH(self,echain=[]):
        D=self.elist[elements.D].get_pt()
        G = self.elist[elements.G].get_pt()
        A = self.elist[elements.A].get_pt()
        H = self.elist[elements.H].get_pt()
        R = self.elist[elements.R].get_value()
        ARC5=self.elist[elements.ARC5].get_value()

        if D is not None and G is not None \
                and A is not None and H is not None \
                and R is not None and ARC5 is not None:
            poly=Polygon(D,G,A,H)
            CirSec=R*ARC5/2
            value=poly-CirSec
            return value
        return None