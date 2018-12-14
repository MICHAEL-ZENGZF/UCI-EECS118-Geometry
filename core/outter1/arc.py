import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class ARC1:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.ARC1
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
            self.value =self.get_by_CAGR(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CAGR(self,echain=[]):
        pt1=self.elist[elements.C].get_pt(echain)
        O=self.elist[elements.A].get_pt(echain)
        pt2=self.elist[elements.G].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)

        if pt1 is not None and O is not None\
                and pt2 is not None and R is not None:
            l1=Line(pt1,O)
            l2=Line(pt2,O)
            rad=l1.smallest_angle_between(l2)
            value=rad*R
            return value

        return None

class ARC2:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.ARC2
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
            self.value =self.get_by_CAFR(echain)
            echain.remove(self.name)
            return self.value
    def get_by_CAFR(self,echain=[]):
        pt1=self.elist[elements.C].get_pt(echain)
        O=self.elist[elements.A].get_pt(echain)
        pt2=self.elist[elements.F].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)

        if pt1 is not None and O is not None\
                and pt2 is not None and R is not None:
            l1=Line(pt1,O)
            l2=Line(pt2,O)
            rad=l1.smallest_angle_between(l2)
            value=rad*R
            return value

        return None

class ARC3:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.ARC3
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
            self.value =self.get_by_IAFR(echain)
            echain.remove(self.name)
            return self.value
    def get_by_IAFR(self,echain=[]):
        pt1=self.elist[elements.I].get_pt(echain)
        O=self.elist[elements.A].get_pt(echain)
        pt2=self.elist[elements.F].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)

        if pt1 is not None and O is not None\
                and pt2 is not None and R is not None:
            l1=Line(pt1,O)
            l2=Line(pt2,O)
            rad=l1.smallest_angle_between(l2)
            value=rad*R
            return value

        return None

class ARC4:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.ARC4
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
            self.value =self.get_by_IAHR(echain)
            echain.remove(self.name)
            return self.value
    def get_by_IAHR(self,echain=[]):
        pt1=self.elist[elements.I].get_pt(echain)
        O=self.elist[elements.A].get_pt(echain)
        pt2=self.elist[elements.H].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)

        if pt1 is not None and O is not None\
                and pt2 is not None and R is not None:
            l1=Line(pt1,O)
            l2=Line(pt2,O)
            rad=l1.smallest_angle_between(l2)
            value=rad*R
            return value

        return None

class ARC5:

    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.ARC5
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
            self.value =self.get_by_GAHR(echain)
            echain.remove(self.name)
            return self.value
    def get_by_GAHR(self,echain=[]):
        pt1=self.elist[elements.G].get_pt(echain)
        O=self.elist[elements.A].get_pt(echain)
        pt2=self.elist[elements.H].get_pt(echain)
        R=self.elist[elements.R].get_value(echain)

        if pt1 is not None and O is not None\
                and pt2 is not None and R is not None:
            l1=Line(pt1,O)
            l2=Line(pt2,O)
            rad=l1.smallest_angle_between(l2)
            value=rad*R
            return value

        return None