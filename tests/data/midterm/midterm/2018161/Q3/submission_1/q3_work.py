# MID-TERM EXAM: QUESTION 3

def area_square(s):
    a = s**2
    return a

def vol_frustum(top_area, bottom_area, height):
    v = (height/3)*(top_area + bottom_area + (top_area*bottom_area)**0.5)
    return v

def get_volume(s1, s2, height):
    top = area_square(s1)
    bottom = area_square(s2)
    top_area = top
    bottom_area = bottom
    final_vol = vol_frustum(top_area, bottom_area, height)
    return final_vol
