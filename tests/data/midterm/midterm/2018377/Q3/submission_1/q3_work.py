import math
def area_square(s):
    area = s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3)*(top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return vol
    
def get_volume(s1, s2, height):
    top_sqr = area_square(s1)
    bot_sqr = area_square(s2)
    volume = vol_frustum(top_sqr, bot_sqr, height)
    return round(volume, 3)