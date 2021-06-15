import pickle

def read_stations(f):
	dic = {}
	aline = f.readline()
	x1 = aline.split('=')
	aline = f.readline()
	y1 = aline.split(', ')
	aline = f.readline()
	aline = f.readline()
	x2 = aline.split('=')
	aline = f.readline()
	y2 = aline.split(', ')
	aline = f.readline()
	aline = f.readline()
	x3 = aline.split('=')
	aline = f.readline()
	y3 = aline.split(', ')
	dic[x1[1]] = y1
	dic[x2[1]] = y2
	dic[x3[1]] = y3
	return dic

def get_stationline(mrt):
    pass

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