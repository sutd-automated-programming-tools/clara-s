import math
def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area,bottom_area, height):
    Volume= (height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return Volume

def get_volume(s1,s2,height):
    top=area_square(s1)
    bottom=area_square(s2)
    vol=vol_frustum(top,bottom,height)
    return round(vol,3)
