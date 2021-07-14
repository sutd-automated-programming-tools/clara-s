def area_square(s):
    return(s**2)

def vol_frustum(top_area, bottom_area, height):
    H = height
    A1 = top_area
    A2 = bottom_area
    Volume = (H / 3) * (A1 + A2 + (A1 * A2) ** 0.5)
    return Volume

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    return(vol_frustum(top_area, bottom_area, height))