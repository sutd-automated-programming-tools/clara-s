from math import sqrt
 
def area_square(s):
    #area is side x side
    a = s*s
    return a
     
def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    H = height
    vol = (H/3)*(A1+A2+(sqrt(A1*A2)))
    return vol
     
 
def get_volume(s1,s2,height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    totvol = vol_frustum(top_area,bottom_area,height)
    return totvol
