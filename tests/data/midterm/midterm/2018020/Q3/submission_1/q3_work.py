# MID-TERM EXAM: QUESTION 3

def area_square(s):
    sqarea = s*s
    return sqarea

def vol_frustum(top_area, bottom_area, height):
    v = (height / 3) * (top_area + bottom_area + (top_area * bottom_area)**0.5)
    return v

def get_volume(s1, s2, height):
    topsqarea = area_square(s1)
    botsqarea = area_square(s2)
    finalv = vol_frustum(topsqarea, botsqarea, height)
    return round(finalv, 3)