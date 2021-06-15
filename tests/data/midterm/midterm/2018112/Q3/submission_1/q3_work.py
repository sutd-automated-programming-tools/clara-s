# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
	squarearea = s**2
	return squarearea

def vol_frustum(top_area, bottom_area, height):
	volume = (height/3) * (top_area + bottom_area + math.sqrt(top_area * bottom_area))
	return volume

def get_volume(s1, s2, height):
	smaller_area = area_square(s1)
	larger_area = area_square(s2)
	final_vol = vol_frustum(smaller_area, larger_area, height)
	return round(final_vol,3)