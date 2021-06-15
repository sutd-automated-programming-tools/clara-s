# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
	return s**2

def vol_frustum(top_area, bottom_area, height):
	return (1/3)*height*(top_area+bottom_area + (top_area*bottom_area)**0.5)

def get_volume(s1, s2, height):
	area1 = area_square(s1)
	area2 = area_square(s2)
	Volume = vol_frustum(area1,area2,height)
	return Volume
