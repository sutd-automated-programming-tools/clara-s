# MID-TERM EXAM: QUESTION 3

def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    H = height
    vol = H/3*(A1 + A2 + (A1*A2)**0.5)
    return vol


def get_volume(s1, s2, height):
    
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = vol_frustum(top_area, bottom_area, height)
    return volume
