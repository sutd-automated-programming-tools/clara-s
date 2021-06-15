import pickle

def read_stations(f):
	file=open(f,'r')
	mrt=file.readlines()
	dic={}
	for index, line in enumerate(mrt):
		a='=' in line
		if a== True:
			dic[line.strip().replace('=','')]=[mrt[index+1].strip()]
	return dic
	

def get_stationline(mrt):
	station={}
	inv=list(mrt.keys())
	for num, i in enumerate(mrt.values()):
		for j in i:
			station[j]=inv[num]
			

			# station[j]=
	return station

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