def getMRT(f):
	f_lines = f.readlines()
	result_dict = {}

	for line in f_lines:
		formatted_line = line.strip()
		data_list = formatted_line.split(',')

		# Remove whitespace from items in data_list
		data_list = [x.strip() for x in data_list]

		r = data_list[0]
		result_dict[r] = data_list[1:]

	return result_dict



def get_stationline(mrt):
    d=getMRT(f)
    f={}
    f[d.values()]=[d.keys()]
    return f

def get_interchange(stationline):
    e={}