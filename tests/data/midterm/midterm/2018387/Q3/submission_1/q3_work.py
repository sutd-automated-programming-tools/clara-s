# MID-TERM EXAM: QUESTION 3

import math
#take side of square length as input and calculate area
def area_square(s):
    return (s**2)

#input top area, bottom area, height, calc vol
def vol_frustum(t, b, h):
    t = float(t)
#    print (t)
    b = float(b)
#    print (b)
    h = float(h)
#    print("inside vol frus h")
#    print(h)
    return((t+b+(math.sqrt(t*b)))*(h/3))

#calc vol, by inputting sides, height
def get_volume(s1, s2, h):
    a1 = area_square(s1)
    a2 = area_square(s2)
    return(round(vol_frustum(a1, a2, h), 3))
    
print('{:.3f}'.format(area_square(2)))
print('{:.3f}'.format(area_square(3)))
print('{:.3f}'.format(vol_frustum(1.0, 4.0, 2.0)))
print('{:.3f}'.format(vol_frustum(2.0, 2.0, 2.0)))
print('{:.3f}'.format(get_volume(1, 2, 2)))
print('{:.3f}'.format(get_volume(1.5, 3.3, 5.0)))
print('{:.3f}'.format(get_volume(3.6, 6.4, 4.0)))
