
import math

def area_square(s):
    s = float(s)
    ans = s**2
    return ans

def vol_frustum(top_area, bottom_area, height):
    height = float(height)
    volume = (height/3)*(top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return volume

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = vol_frustum(top_area,bottom_area,height)
    return round(volume,3)
    