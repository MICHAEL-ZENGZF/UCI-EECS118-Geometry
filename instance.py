import os
import elements
import numpy as np
from core import angle,arc,area,circle,intersection,\
                    line,lineseg,lineseg_overlap,perimeter,vertice

element={}

element[elements.C]=vertice.C(elementlist=element)
element[elements.E]=vertice.E(elementlist=element)
element[elements.D]=vertice.D(elementlist=element)

element[elements.F]=intersection.F(elementlist=element)
element[elements.I]=intersection.I(elementlist=element)
element[elements.H]=intersection.H(elementlist=element)
element[elements.G]=intersection.G(elementlist=element)

element[elements.A]=circle.A(elementlist=element)

element[elements.R]=circle.R(elementlist=element)

element[elements.CF]=lineseg.CF(elementlist=element)
element[elements.FE]=lineseg.FE(elementlist=element)
element[elements.EI]=lineseg.EI(elementlist=element)
element[elements.IH]=lineseg.IH(elementlist=element)
element[elements.HD]=lineseg.HD(elementlist=element)
element[elements.DG]=lineseg.DG(elementlist=element)
element[elements.GC]=lineseg.GC(elementlist=element)

element[elements.CE]=line.CE(elementlist=element)
element[elements.ED]=line.ED(elementlist=element)
element[elements.DC]=line.DC(elementlist=element)

element[elements.EH]=lineseg_overlap.EH(elementlist=element)
element[elements.ID]=lineseg_overlap.ID(elementlist=element)

element[elements.S1]=area.S1(elementlist=element)
element[elements.S2]=area.S2(elementlist=element)
element[elements.S3]=area.S3(elementlist=element)
element[elements.S4]=area.S4(elementlist=element)
element[elements.S5]=area.S5(elementlist=element)
element[elements.S6]=area.S6(elementlist=element)


element[elements.Alpha]=angle.Alpha(elementlist=element)
element[elements.Beta]=angle.Beta(elementlist=element)
element[elements.Gamma]=angle.Gamma(elementlist=element)

element[elements.ARC1]=arc.ARC1(elementlist=element)
element[elements.ARC2]=arc.ARC2(elementlist=element)
element[elements.ARC3]=arc.ARC3(elementlist=element)
element[elements.ARC4]=arc.ARC4(elementlist=element)
element[elements.ARC5]=arc.ARC5(elementlist=element)

element[elements.perimeter_triangle]=perimeter.perimeter_triangle(elementlist=element)
element[elements.perimeter_circle]=perimeter.perimeter_circle(elementlist=element)

element[elements.area_triangle]=area.area_triangle(elementlist=element)
element[elements.area_circle]=area.area_circle(elementlist=element)