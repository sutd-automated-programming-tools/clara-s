# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s*s
    return area
print ("{:3f}".format(area_square(2)))

def vol_frustum(top_area, bottom_area, height):
    H=float(height)
    A1=float(top_area)
    A2=float(bottom_area)
    vol=(H/3.0)*(A1+A2 +math.sqrt(A1*A2))
    return vol

                 
def get_volume(s1, s2, height):
    top_area=area_square(s1)            
    bottom_area=area_square(s2)
    ans=vol_frustum(top_area,bottom_area,height)
    return ans

