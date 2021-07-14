#question 3 part a, area of square

import math

def area_square(s):
    area=float(s)**2
    return area

print(area_square(5))

#question 3 part b

def vol_frustum(top_area,bottom_area,height):
    volume=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return volume

#question 3 part c
print(vol_frustum(4,4,4))

def get_volume(s1,s2,height):
    answer=vol_frustum(area_square(s1),area_square(s2),height)
    return round(answer,3)