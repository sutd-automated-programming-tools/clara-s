def area_square(s):
    area = s*s
    return area


# In[ ]:


import math
def vol_frustum(top_area,bottom_area,height):
    vol = height/3 * (top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return round(vol,3)
vol_frustum(1,4,2)


# In[ ]:


def get_volume(s1,s2,height):
    area1 = area_square(s1)
    area2 = area_square(s2)
    vol = vol_frustum(area1,area2,height)
    return round(vol,3)
