import math
def area_square(s):
    ans = float(s*s)
    return ans
#print(area_square(5.9))

def vol_frustum(top_area, bottom_area, height):
    ans = float((height/3)*((top_area+bottom_area)+ math.sqrt(top_area*bottom_area)))
    return ans

#print(vol_frustum(1,1,9))

def get_volume(s1,s2,height):
    side1 = area_square(s1)
    side2 = area_square(s2)
    ans = vol_frustum(side1,side2,height)
    return round(ans,3)

#print(get_volume(2,7,11))
