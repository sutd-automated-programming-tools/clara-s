import math

def area_square(s):
    area_of_square_base=float(s)**2
    return area_of_square_base

def vol_frusturm(top_area, bottom_area, height):
    vol=float(height)/3*(float(top_area)+ float(bottom_area)+ math.sqrt(float(top_area)+ float(bottom_area)))
    return vol

def get_volume(s1, s2, height):
    area1=area_square(s1)
    area2=area_square(s2)
    vol_ans=vol_frusturm(area1, area2, height)
    return round(vol_ans,3)
