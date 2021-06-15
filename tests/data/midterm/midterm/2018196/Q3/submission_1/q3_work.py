from math import sqrt

def area_square(s):
    area = float(s*s)
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = float ( (height/3) * (top_area + bottom_area + sqrt(top_area*bottom_area)) )
    return volume

def get_volume(s1, s2, height):
    A_s1 = area_square(s1)
    A_s2 = area_square(s2)
    total_volume = float (vol_frustum(A_s1, A_s2, height))
    return round(total_volume,3)