import math

def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    area3 = math.sqrt(top_area*bottom_area)
    volume = (height/3)*(top_area+bottom_area+area3)
    return volume

def get_volume(s1, s2, height):
    area1 = area_square(s1)
    area2 = area_square(s2)
    volume = vol_frustum(area1,area2,height)
    return volume
