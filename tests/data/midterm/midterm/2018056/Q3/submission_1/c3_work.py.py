#part a

def area_square(s):
    area = s*s
    return area

#print(area_square(2))

#part b
    
import math

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3) * (top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return vol

#print(vol_frustum(2,2,2))    

#part c

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    
    vol = vol_frustum(a1,a2,height)
    
    return round(vol,3)

print('{:.3f}'.format(get_volume(1.5,3.3,5.0)))