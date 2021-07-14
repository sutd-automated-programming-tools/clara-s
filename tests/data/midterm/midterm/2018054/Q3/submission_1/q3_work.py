# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    s = float(s) 
    areasq = (s*s) 
    return float(areasq)          #finding the area of a square

def vol_frustum(top_area, bottom_area, height):
    top_area= float(top_area)
    bottom_area= float(bottom_area) 
    vol = (height/3)*(top_area+ bottom_area +(math.sqrt(top_area*bottom_area))
    return float(vol)           #finding vol of the frustum 
    
def get_volume(s1, s2, height): 
                        
                    A1= area_square(s1)
                    A2= area_square(s2)
                    height = H 
                    finalout = vol_frustum (A1, A2, H) 
                    finalout= round(float(finalout), 3)
                    return finalout 
                    
