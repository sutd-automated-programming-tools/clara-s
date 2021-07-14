# MID-TERM EXAM: QUESTION 3

import math

'''done'''
def area_square(s):
    area = s**2
    #return ('{0:.3f}'.format(area))
    return area
#print(area_square(3))

'''done'''

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3) * (top_area + bottom_area + math.sqrt(top_area*bottom_area))
    #return ('{:.3f}'.format(vol))
    return vol
#print(vol_frustrum(2,2,2))

'''done'''
def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = vol_frustum(top_area, bottom_area, height)
    return ('{0:.3f}'.format(volume))