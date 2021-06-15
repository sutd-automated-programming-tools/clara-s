import math

def area_square(s):
    area_of_square=s*s
    return area_of_square
#print(area_square(3))


def vol_frustum(top_area,bottom_area,height):
    volume=(height/3)*(top_area+bottom_area+(math.sqrt(top_area*bottom_area)))
    return volume
#print(vol_frustum(2,2,2))
def get_volume(s1,s2,height):
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    ans=vol_frustum(top_area,bottom_area,height)
    return ans
#print(get_volume(3.6,6.4,4))
