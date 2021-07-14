def area_square(s):
    area = s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = (height/3) * (top_area + bottom_area + (top_area * bottom_area)**0.5)
    return volume

def get_volume (s1, s2, height):
    
    volll = vol_frustum (area_square(s1), area_square(s2), height)
    return volll
