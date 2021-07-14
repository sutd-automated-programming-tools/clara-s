import pickle

def read_stations(f):
	lines = f.readlines()
	mrtline = ""
	dicti = {}

	for line in lines:
		# Remove whitespaces from line
		formatted_line = line.strip()

		# Check if this is a day or an entry
		if "Line" in formatted_line:
			# If it's a day, change the current day and add it to the dictionary
			mrtline = formatted_line
			dicti[mrtline] = []
		elif mrtline != "":
			# If not a day, add data to the current day
			# Create a tuple from the data
			station = formatted_line.split(' ')
			dicti[mrtline].append(station)

	return dicti

def get_stationline(mrt):
    leest=[]
    for i in read_stations(f):
        if mrt in dict[i]:
            leest.append(i)
    return leest
            

def get_interchange(stationline):
    pass


  
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