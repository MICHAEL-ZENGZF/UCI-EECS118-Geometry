import os
import elements
import numpy as np

import instance



class InvalidPointException(Exception):
    pass
class InvalidValueException(Exception):
    pass

def set_points(element, value=None, x=None, y=None):
    if element in elements.points:
        #print("try to set point "+element)
        if isinstance(value,tuple) \
            and not None in value \
            and not any((x,y)) :
            instance.element[element].set_value(value)
        elif value is None \
            and not None in (x,y) :
            instance.element[element].set_value((x,y))
        else:
            #print("please input a tuple or x and y directly, not both or others")
            raise InvalidPointException

def set_values(element, value=None, x=None, y=None):
    if element in elements.values:
        #print("try to set value "+element)
        if value>=0 and  not any((x,y)):
            instance.element[element].set_value(value)
            #print("success ")
        else:
            raise InvalidValueException

############################################################
############################################################


#Entities
def set_value(element,value=None,x=None,y=None):
    set_points(element,value,x,y)
    set_values(element,value,x,y)

def get_value(element):
    if element in elements.element:
        return instance.element[element].get_value()


#Sample
if __name__=='__main__':
    set_value(elements.A,(0,0))
    set_value(elements.R, 2)

    set_value(elements.C, (0, 2))
    set_value(elements.E, (3, -1))
    set_value(elements.D, (-3, -1))

    Alpha = get_value(elements.Alpha)
    Beta = get_value(elements.Beta)
    Gamma = get_value(elements.Gamma)

    print(Alpha)
    print(Beta)
    print(Gamma)

    area_triangle=get_value(elements.area_triangle)
    area_circle=get_value(elements.area_circle)
    print(area_triangle)
    print(area_circle)



