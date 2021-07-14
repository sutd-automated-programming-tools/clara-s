#q3
import math 

def area_square(s):
    a=s*s
    return a

def vol_frustum(top_area,bottom_area,height):
    vo=(height/3)(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return vo

def get_volume(s1,s2,height):
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    v=(height/3)(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return v

print(vol_frustum(1,4,2))
