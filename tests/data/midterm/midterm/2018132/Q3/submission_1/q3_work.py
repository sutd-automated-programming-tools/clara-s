# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = float(s**2)
    return area


def vol_frustrum(top_area, bottom_area, height):
    volume = (height / 3) * (top_area + bottom_area + math.sqrt(top_area * bottom_area))
    return float(volume)

def get_volume(s1, s2, height):
    area_t = area_square(s1)
    area_b = area_square(s2)
    volume = vol_frustrum(area_t, area_b, height)
    
    return round(volume, 3)

print('{:.3f}'.format(area_square(2)))
print('{:.3f}'.format(area_square(3)))
print('{:.3f}'.format(vol_frustrum(1,4,2)))
print('{:.3f}'.format(vol_frustrum(2,2,2)))