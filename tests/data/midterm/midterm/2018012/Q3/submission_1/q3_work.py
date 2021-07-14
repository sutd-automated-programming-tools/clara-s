import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3)*(top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return vol

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = vol_frustum(top_area, bottom_area, height)
    return volume

