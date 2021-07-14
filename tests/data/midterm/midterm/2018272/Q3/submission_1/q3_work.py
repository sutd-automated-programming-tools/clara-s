# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(tarea,barea,h):
    vol = h*(tarea+barea+(tarea*barea)**0.5)/3
    return vol

def get_volume(s1,s2,h):
    tarea = area_square(s1)
    barea = area_square(s2)
    vol = vol_frustum(tarea,barea,h)
    return round(vol,3)
