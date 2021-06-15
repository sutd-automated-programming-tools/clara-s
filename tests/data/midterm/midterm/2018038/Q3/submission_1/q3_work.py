def roundme(n): return lambda x: round(x,n)

round2 = roundme(2)
round3 = roundme(3)
round5 = roundme(5)

def area_square(s):
	return s**2

def vol_frustum(top_area, bottom_area, height):
	vol = height/3 * (top_area + bottom_area + (top_area * bottom_area)**0.5)
	return vol

def get_volume(s1, s2, height):
	top_area = area_square(s1)
	bottom_area = area_square(s2)
	return round3(vol_frustum(top_area, bottom_area, height))

