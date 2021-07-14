# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    areasq = s*s #find area of square by multiplying both sides
    return areasq

def vol_frustum(top_area, bottom_area, height):
    volf = (height/3)(top_area + bottom_area + math.sqrt(top_area + bottom_area) #find volume of frustum by using formula given
    return volf
    

def get_volume(s1, s2, height):
    top_area = area_square(s1) #find top area by calling function area_square and using value s1
    bottom_area = area_square(s2) #find bottom area by calling function area_square and using value s2
    finalvol = vol_frustum(top_area, bottom_area, height) #get volume by calling function vol_frustum and using values of top_area, bottom_area and heigh
                      
    return (round(finalvol,3)) #return finalvol and round to 3 dp
