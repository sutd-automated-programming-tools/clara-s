import pickle

def read_stations(f):
	output = dict()
	for line in f:
		# print(line)
		if line[0] == "=":
			line = line[1:-2]
			key = line



		else:
			line = line.split(',')
			line_p = [e.strip() for e in line]
			output[key] = line_p

			f.readline()

	return(output)

def find_path(f,start,end):

	stations = read_stations(f)
	stationline = get_stationline(stations)
	dict_interchange = get_interchange(stationline)

	for k,v in stations.items():
		if start in v and end in v:
			print(v)
			a = (v.index(start))
			b = v.index(end)
			print(a,b)
			if b > a:
				return v[a:b]

			elif a > b:
				print("yes")
				return v[::-1][-a-1:-b]

		else: 
			return None
            
            
         

# f = open("mrt_lines_short.txt", "r")
# # print(f)
# print(read_stations(f))

# def get_stationline(mrt):

def get_stationline(mrt):

	output = dict()
	for k,v in mrt.items():

		for station in v:
			output[station] = []
			for k,v in mrt.items():
				if station in v:
					output[station].append(k)

	return output

f = open("mrt_lines_short.txt", "r")
# print(get_stationline(read_stations(f)))

def get_interchange(stationline):
	output = {}
	for k,v in stationline.items():
		if len(v) > 1:
			output[k] = v
	return output


  
##### Testing get_stationline ###########
with open('stations_short.pickle','rb') as f:
    mrt_d = pickle.load(f)
    print(get_stationline(mrt_d))
#########################################

##### Testing get_interchange ###########
with open('lines_short.pickle','rb') as f:
    lines = pickle.load(f)
    print(get_interchange(lines))
#########################################

###### Testing find_path ################
# You can use these three variables in your find_path
# to get the output of
# mrt_d = read_station()
# lines = get_stationline()
# interchange = get_interchange()
# even if you haven't finished these three functions
#########################################
def find_path(f,start,end):
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass