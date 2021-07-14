# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
	return s**2
def vol_frustum(top_area, bottom_area, height):
	vol  = height/3*(top_area+bottom_area+(top_area*bottom_area)**0.5)
	return vol

def get_volume(s1,s2,height):
	s1 = area_square(s1)
	s2 = area_square(s2)
	return vol_frustum(s1,s2, height)
