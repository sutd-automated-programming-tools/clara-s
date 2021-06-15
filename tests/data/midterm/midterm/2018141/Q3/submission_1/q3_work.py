# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):

    return(s*s)

def vol_frustum(top_area, bottom_area, height):
    return((height/3)*(top_area + bottom_area+((top_area*bottom_area)**(0.5))))
    

def get_volume(s1, s2, height):
    return round(vol_frustum(area_square(s1),area_square(s2),height),3)
  # return round(((height/3)*(area_square(s1) + area_square(s2)+((area_square(s1)*area_square(s2))**(0.5)))),3)
