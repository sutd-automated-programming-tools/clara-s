import math

def area_square(s):
    
    area=s*s
    return area
    pass

def vol_frustum(top_area, bottom_area, height):
    
    vol=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return vol    
    pass

def get_volume(s1, s2, height):
    
    topA=area_square(s1)
    botA=area_square(s2)
    volume=vol_frustum(topA,botA,height)
    
    return round(volume,3)