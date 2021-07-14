# MID-TERM EXAM: QUESTION 3

import math
import cmath
import numpy
import scipy
import sympy
import itertools

def area_square(s):
    area=s**2
    return area

def vol_frustum(top_area,bottom_area,height):
    Volume=(height/3)*(top_area+bottom_area+(math.sqrt(top_area*bottom_area)))
    return Volume

def get_volume(s1,s2,height):
    area1=area_square(s1)
    area2=area_square(s2)
    Volume=vol_frustum(area1,area2,height)
    return round(Volume,3)