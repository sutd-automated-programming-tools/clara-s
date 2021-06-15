import math as m

def area_square(s):
    sq_area= s**2
    
    return sq_area

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3) * (top_area + bottom_area + m.sqrt(top_area * bottom_area))
    return vol
    
    

def get_volume(s1, s2, height):
    area1= area_square(s1)
    area2= area_square(s2)
    ans = vol_frustum(area1, area2, height)
    
    return ans
