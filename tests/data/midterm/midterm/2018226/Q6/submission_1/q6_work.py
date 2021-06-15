import pickle

def read_stations(f):
	lines = dict()
	z = f.readlines()
	for j in z:
		a = j.strip().split(' ')
		c= a.pop(0)
		lines[c] = a
	return lines


def get_stationline(mrt):
	key = dict()
	for i in mrt:
		for j in mrt[i]:
			key.update({mrt[i][j]: mrt[i]})
	return key


def get_interchange(dictschedule):
	for i in dictschedule:
		master_set = {}
		for j in range(len(dictschedule[i])):
			key1,key2 = dictschedule[i][j]
			if master_set == {} or master_set == set1:
				master_set = set1
			else:
				if bool(master_set & set1) == True:
					check = True
				else:
					check = False
		dictschedule.update({i:check})
	return dictschedule


  
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