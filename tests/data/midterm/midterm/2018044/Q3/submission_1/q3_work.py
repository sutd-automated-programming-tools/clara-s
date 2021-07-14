# MID-TERM EXAM: QUESTION 3

def area_square(s):
    a = s*s
    return a

def vol_frustum(ta, ba, h):
    vol = (h/3)*(ta + ba + (ta*ba)**0.5)
    return round(vol, 3)

def get_volume(s1, s2, h):
    a1 = area_square(s1)
    a2 = area_square(s2)
    vol = vol_frustum(a1,a2,h)
    return vol
