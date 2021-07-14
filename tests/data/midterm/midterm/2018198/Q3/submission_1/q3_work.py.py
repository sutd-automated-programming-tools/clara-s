# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:06:49 2018

@author: Jia Yi
"""
import math
#3
#s = float(input("Length of side of square: ")) 
def area_square(s): 
    s = float(input("Length of side of square: ")) 
    area = s**2
    return area
#print(area_square(s))
    
#print('{:.3f}'.format(area_square(2)))
#print('{:.3f}'.format(area_square(3)))

#s1 = float(input("Length of side of top square: ")) 
#s2 = float(input("Length of side of bottom square: ")) 
#height = float(input("Height of frustum: "))
#
#def top_area(s1): 
#    area = s1**2
#    return area
#
#def bottom_area(s2): 
#    area = s2**2
#    return area
import math

def vol_frustum(top_area, bottom_area, height): 
    volume = (height/3) * (top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return volume

#print('{:.3f}'.format(vol_frustum(1,4,2)))
#print('{:.3f}'.format(vol_frustum(2,2,2)))


#s1 = float(input("Length of side of top square: ")) 
#s2 = float(input("Length of side of bottom square: ")) 
#height = float(input("Height of frustum: "))

def get_volume(s1,s2,height):
#    s1 = float(input("Length of side of top square: ")) 
#    s2 = float(input("Length of side of bottom square: ")) 
#    height = float(input("Height of frustum: "))
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    vol = vol_frustum(top_area, bottom_area, height)
    return round(vol,3)
    
#print(get_volume(1.5,3.3,4.0))