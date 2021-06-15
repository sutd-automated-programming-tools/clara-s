# MID-TERM EXAM: QUESTION 3

import math

def vol_frustum(top_area, bottom_area, height):
    return (top_area + bottom_area + (top_area*bottom_area)**0.5)*height/3
    
def area_square(x):
    return x**2

def get_volume(s1, s2, height):
    x=area_square(s1)
    y=area_square(s2)
    return vol_frustum(x,y,height)
    

print('{:.3f}'.format(vol_frustum(1,4,2)))
print('{:.3f}'.format(vol_frustum(2,2,2)))
print('{:.3f}'.format(get_volume(1,2,2)))
print('{:.3f}'.format(get_volume(1.5,3.3,5.0)))
print('{:.3f}'.format(get_volume(3.6,6.4,4.0)))