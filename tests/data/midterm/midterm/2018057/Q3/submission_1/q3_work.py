# MID-TERM EXAM: QUESTION 3

def area_square(s):
    return s**2

def vol_frustum(top,btm,h):
    import math
    return round((top + btm + math.sqrt(top*btm))*h/3,3)

def get_volume(s1,s2,h):
    return vol_frustum(area_square(s1),area_square(s2),h)
