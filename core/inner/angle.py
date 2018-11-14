import numpy as np
from sympy import *
from sympy.geometry import *
import elements

class Alpha:
    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.Alpha
        self.elist=elementlist
        self.rule_set=[self.law_of_cos,self.law_of_sin,self.law_of_angle]
    def set_value(self,value=None):
        self.value=value

    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value is not None:
            return self.value
        else:
            rs=[]
            echain.append(self.name)
            for rule in self.rule_set:
                rs.extend(rule(echain))
            echain.remove(self.name)
            if len(rs)>0:
                self.value=rs[0]
            return self.value

    def law_of_cos(self,echain):
        CE=self.elist[elements.CE].get_value(echain)
        DC=self.elist[elements.DC].get_value(echain)
        ED = self.elist[elements.ED].get_value(echain)
        angle=acos((DC*DC+ED*ED-CE*CE)/(2*DC*ED))
        return angle

    def law_of_sin(self,echain):
        CE =self.elist[elements.CE].get_value(echain)
        DC = self.elist[elements.DC].get_value(echain)
        ED = self.elist[elements.ED].get_value(echain)
        Beta = self.elist[elements.Beta].get_value(echain)
        Gamma = self.elist[elements.Gamma].get_value(echain)
        ratio1=DC/sin(Beta)
        ratio2=ED/sin(Gamma)
        ratio=ratio1 if ratio1 is not None else ratio2
        angle=asin(CE/ratio)
        return angle

    def law_of_angle(self,echain):
        Beta=self.elist[elements.Beta].get_value(echain)
        Gamma=self.elist[elements.Gamma].get_value(echain)
        angle=pi-Beta-Gamma
        return angle

class Beta:
    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.Beta
        self.elist=elementlist
        self.rule_set=[self.law_of_cos,self.law_of_sin,self.law_of_angle]
    def set_value(self,value=None):
        self.value=value

    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value is not None:
            return self.value
        else:
            rs=[]
            echain.append(self.name)
            for rule in self.rule_set:
                rs.extend(rule(echain))
            echain.remove(self.name)
            if len(rs)>0:
                self.value=rs[0]
            return self.value

    def law_of_cos(self,echain):
        CE = self.elist[elements.CE].get_value(echain)
        DC = self.elist[elements.DC].get_value(echain)
        ED = self.elist[elements.ED].get_value(echain)
        angle=acos((CE*CE+ED*ED-DC*DC)/(2*CE*ED))
        return angle

    def law_of_sin(self,echain):
        CE =self.elist[elements.CE].get_value(echain)
        DC = self.elist[elements.DC].get_value(echain)
        ED = self.elist[elements.ED].get_value(echain)
        Alpha = self.elist[elements.Alpha].get_value(echain)
        Gamma = self.elist[elements.Gamma].get_value(echain)
        ratio1=CE/sin(Alpha)
        ratio2=ED/sin(Gamma)
        ratio=ratio1 if ratio1 is not None else ratio2
        angle=asin(DC/ratio)
        return angle

    def law_of_angle(self,echain):
        Alpha=self.elist[elements.Alpha].get_value(echain)
        Gamma=self.elist[elements.Gamma].get_value(echain)
        angle=pi-Alpha-Gamma
        return angle

class Gamma:
    def __init__(self, value=None,elementlist={}):
        self.value=value
        self.name=elements.Gamma
        self.elist=elementlist
        self.rule_set=[self.law_of_cos,self.law_of_sin,self.law_of_angle]
    def set_value(self,value=None):
        self.value=value

    def get_value(self, echain=[]):
        if self.name in echain:
            return None
        elif self.value is not None:
            return self.value
        else:
            rs=[]
            echain.append(self.name)
            for rule in self.rule_set:
                rs.extend(rule(echain))
            echain.remove(self.name)
            if len(rs)>0:
                self.value=rs[0]
            return self.value

    def law_of_cos(self,echain):
        CE = self.elist[elements.CE].get_value(echain)
        DC = self.elist[elements.DC].get_value(echain)
        ED = self.elist[elements.ED].get_value(echain)
        angle=acos((CE*CE+DC*DC-ED*ED)/(2*CE*DC))
        return angle

    def law_of_sin(self,echain):
        CE =self.elist[elements.CE].get_value(echain)
        DC = self.elist[elements.DC].get_value(echain)
        ED = self.elist[elements.ED].get_value(echain)
        Alpha = self.elist[elements.Alpha].get_value(echain)
        Beta = self.elist[elements.Beta].get_value(echain)
        try:
            ratio1 = CE / sin(Alpha)
            ratio2 = ED / sin(Beta)
            ratio = ratio1 if ratio1 is not None else ratio2
            angle = asin(DC / ratio)
            return angle
        except Exception:
            return None

    def law_of_angle(self,echain):
        Alpha=self.elist[elements.Alpha].get_value(echain)
        Beta = self.elist[elements.Beta].get_value(echain)
        try:
            angle = pi - Alpha - Beta
            return angle
        except Exception:
            return None