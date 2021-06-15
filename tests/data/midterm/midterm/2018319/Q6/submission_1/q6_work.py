import pickle
def read_stations(f):
	f = f.readlines()
	route = f[0].strip().strip('=')
	dic = {}
	ls = []
	for line in f:
		line = line.strip()
		if line=='':
			continue
		if line[0]=='=':
            
			dic[route] = ls
			ls = []
			route = line.strip('=')
			continue
		ls.extend(line.split(', '))
	dic [route] = ls
	return dic

def get_stationline(mrt):
	lines = mrt.keys()
	dic = {}
	for train_line in lines:
		for stations in mrt[train_line]:
			if stations in dic:
				x = dic[stations]
				if len(x)==2:
					x = [x[0], x[1], train_line]
				
				if len(x)==1:
					x = [x[0],train_line]
				
				
				dic[stations] = x
			else:
				dic[stations] = [train_line]
	return dic

def get_interchange(stationline):
	dic = {}
	for station in stationline.keys():
		if len(stationline[station])>1:
			dic[station] = stationline[station]
	return dic
  
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