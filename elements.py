import os
import numpy as np

#coords
C='C'
F='F'
E='E'
I='I'
H='H'
G='G'
D='D'

A='A'


#value
Alpha='Alpha'
Beta='Beta'
Gamma='Gamma'

perimeter_triangle='perimeter_triangle'
perimeter_circle='perimeter_circle'

area_triangle='area_triangle'
area_circle='area_circle'

R='R'



CF='CF'
FE='FE'
EI='EI'
IH='IH'
HD='HD'
DG='DG'
GC='GC'

CE='CE'
EH='EH'
ID='ID'
ED='ED'
DC='DC'

ARC1='ARC1'
ARC2='ARC2'
ARC3='ARC3'
ARC4='ARC4'
ARC5='ARC5'

S1='S1'
S2='S2'
S3='S3'
S4='S4'
S5='S5'
S6='S6'


points=[C,E,D,F,I,H,G,A]

values=[R,
        CF,FE,EI,IH,HD,DG,GC,
        CE,ED,DC,
        EH,ID,
        S1,S2,S3,S4,S5,S6,
        Alpha,Beta,Gamma,
        ARC1,ARC2,ARC3,ARC4,ARC5,
        perimeter_triangle,perimeter_circle,
        area_triangle,area_circle]

element=[C,E,D,F,I,H,G,A,
         R,
         CF, FE, EI, IH, HD, DG, GC,
         CE, ED, DC,
         EH, ID,
         S1, S2, S3, S4, S5, S6,
         Alpha, Beta, Gamma,
         ARC1, ARC2, ARC3, ARC4, ARC5,
         perimeter_triangle, perimeter_circle,
         area_triangle, area_circle]

vertice=[C,E,D]
intersection=[F,I,H,G]
line=[CE,ED,DC]
angles=[Alpha,Beta,Gamma]
lineseg=[CF,FE,EI,IH,HD,DG,GC]
lineseg_DC=[DG,GC]
lineseg_CE=[CF,FE]
lineseg_ED=[EI,IH,HD]
overlap_lineseg_ED=[EH,ID]
areas_triangle=[S4,S5,S6]

arcs=[ARC1,ARC2,ARC3,ARC4,ARC5]
areas_circle=[S1,S2,S3,S4]

areas=[S1,S2,S3,S4,S5,S6]



