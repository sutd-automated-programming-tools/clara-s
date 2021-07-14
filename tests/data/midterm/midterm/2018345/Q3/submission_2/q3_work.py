
import math

def area_square(s):
    s=float(s)
    area=s**2
    return float(area)

def vol_frustum(top_area, bottom_area, height):
    top_area=float(top_area)
    bottom_area=float(bottom_area)
    height=float(height)
    volume= (height/3)*(top_area+bottom_area+(math.sqrt(top_area+bottom_area)))
    return float(volume)

def get_volume(s1, s2, height):
    s1=float(s1)
    s2=float(s2)
    height=float(height)
    
    area1=area_square(s1)
    area2=area_square(s2)
    
    answer=vol_frustum(area1,area2,height)
    return round(answer,3)