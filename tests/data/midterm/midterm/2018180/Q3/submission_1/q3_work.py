import math as m
def area_square(s):
    area=s**2
    return area

def vol_frustum(top_area, base_area, h):
    volume= h/3 * (top_area + base_area+ m.sqrt(top_area*base_area))
    return volume

def get_volume(s1, s2, height):
    ta=area_square(s1)
    ba=area_square(s2)
    volume_=vol_frustum(ta, ba, height)
    return volume_
# MID-TERM EXAM: QUESTION 3
