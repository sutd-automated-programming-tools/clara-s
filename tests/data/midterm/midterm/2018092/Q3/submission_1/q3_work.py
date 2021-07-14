# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s**2
    return area

# print('{:.3f}'.format(area_square(2)))
# print('{:.3f}'.format(area_square(3)))

def vol_frustum(top_area, bottom_area, height):
    volume = (height/3)*(top_area+bottom_area+(math.sqrt(top_area*bottom_area)))
    return volume

# print('{:.3f}'.format(vol_frustum(1,4,2)))
# print('{:.3f}'.format(vol_frustum(2,2,2)))

def get_volume(s1,s2,height):
    top_area = area_square(s1)
    # print("hi", top_area)
    bottom_area = area_square(s2)
    # print("hi", bottom_area)
    vol = vol_frustum(top_area,bottom_area,height)
    return round(vol,3)
# s1,s2,height = 1,2,2
# get_volume(s1,s2,height)
#print('{:.3f}'.format(get_volume(1,2,2)))
#print('{:.3f}'.format(get_volume(1.5,3.3,5.0)))
#print('{:.3f}'.format(get_volume(3.6,6.4,4.0)))
