import math

def area_square(s):
    area = s**2
    return area


def vol_frustum(top_area, bottom_area, height):
    vol = (height/3)*(top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return vol


def get_volume(s1, s2, height):
    volumes = vol_frustum(area_square(s1),area_square(s2),height)
    return volumes