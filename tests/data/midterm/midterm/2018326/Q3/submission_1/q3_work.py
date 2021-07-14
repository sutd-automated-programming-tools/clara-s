import math
def area_square(s):
    return s**2

def vol_frustum(top_area,bottom_area,height):
    vol=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return vol

def get_volume(s1,s2,height):
    area1=area_square(s1)
    area2=area_square(s2)
    volum=vol_frustum(area1,area2,height)
    return round(float(volum),3)
