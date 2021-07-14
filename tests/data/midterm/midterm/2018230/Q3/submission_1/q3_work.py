# MID-TERM EXAM: QUESTION 3
#q3
import math
#a)
def area_square(s):
    aos = s*s
    return aos
print(area_square(2))

#b)
def vol_frustum(a1, a2, h):
    vof = (h/3)*(a1+a2+math.sqrt(a1*a2))
    return vof

#c)
def get_volume(s1,s2,h):
    a1 = area_square(s1)
    a2 = area_square(s2)
    vol = vol_frustum(a1,a2,h)
    return vol


