# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    area=float(area)
    return area



def vol_frustrum(top_area, bottom_area, height):
    top_area=float(area_square(s1))
    bottom_area=float(area_square(s2))
    height=float(height)
    
    volume=(top_area + bottom_area + (top_area*bottom_area)**2)*(height/3.0)
    
    return volume


def get_volume(s1,s2,height):
    s1=float(s1)
    s2=float(s2)
    height=float(height)
    area1=area_square(s1)
    area2=area_square(s2)
    volume=vol_frustrum(top_area,bottom_area,height)
    volume=round(volume,3)
    return volume