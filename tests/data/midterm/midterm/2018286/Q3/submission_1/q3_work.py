# MID-TERM EXAM: QUESTION 3


import math

def area_square(s):
	return s**2

def vol_frustum(top_area, bottom_area, height):
	output = (height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
	return output

def get_volume(s1, s2, height):
	t = area_square(s1)
	b = area_square(s2)

	return round(vol_frustum(t, b, height),3)