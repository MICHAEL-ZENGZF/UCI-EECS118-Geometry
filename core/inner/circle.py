import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class A(object):
    def __init__(self, value=(None,None),elementlist={}):
        self.value=value
        if not None in value:
            self.pt=Point(value)
        else:
            self.pt=None
        self.name=elements.A
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
        '''else:
            echain.append(self.name)
            self.pt =self.get_by_EFGD(echain)
            return self.pt'''

class R:
    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.C
        self.elist=elementlist
    def set_value(self,value=None):
        self.value=value
    def get_value(self,echain=[]):
        return self.value