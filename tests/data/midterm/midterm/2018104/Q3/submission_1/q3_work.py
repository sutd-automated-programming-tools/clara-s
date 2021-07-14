import math


def area_square(s):
    return s ** 2


def vol_frustum(top_a, bottom_a, height):
    a1a2 = math.sqrt(top_a * bottom_a)
    reduced_h = height / 3
    vol = reduced_h * (top_a + bottom_a + a1a2)
    return vol


def get_volume(s1, s2, height):
    top_a = area_square(s1)
    bottom_a = area_square(s2)
    vol = vol_frustum(top_a, bottom_a, height)
    return round(vol, 3)