# MID-TERM EXAM: QUESTION 3

##Q3

def area_square(s):
    area=s**2
    return area
#print(area_square(2))
    
def vol_frustum(top_area,bottom_area,height):
    A1=top_area
    A2=bottom_area
    H=height
    volume=(H/3)*(A1+A2+(A1*A2)**0.5)
    return volume
#print(vol_frustum(3,4,2))

def get_volume(s1,s2,height):
    toparea=area_square(s1)
    bottomarea=area_square(s2)
    volume=vol_frustum(toparea,bottomarea,height)
    return round(volume,3)
