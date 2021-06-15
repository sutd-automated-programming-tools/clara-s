import pickle

def read_stations(f):
	data = f.read()
	datals = data.split('\n')

	subls = []
	sortedls = []
	for i in datals:
		if '=' in i:
			if subls:
				sortedls.append(subls)
			subls = [i]
		else:
			subls.append(i)
	sortedls.append(subls)
	print(sortedls)

	for i,subls in enumerate(sortedls):
		x = sortedls[i][0].strip('=')
		sortedls[i][0] = x

	dic = {}
	for i in sortedls:
		for j in range(1,len(i)-1):
			dic[i[0]] = i[j].split(', ') 

	return dic

def get_stationline(mrt):
	dic = {}
	for k,v in mrt.items():
		for s in v:
			if s not in dic.keys():
				dic[s] = [k]
			elif s in dic.keys():
				dic[s].append(k)
	return dic

def get_interchange(mrt):
	dic = {}
	for k,v in mrt.items():
		if len(v) > 1:
			dic[k] = v
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
    mrt = read_stations(f)
    stlines = get_stationline(mrt)
    intstops = get_interchange(mrt)
    startline = ''
    stopline = ''
    interchange = ''

    for k,v in mrt.items:
        if start in v:
            startline = k
        if end in v:
            stopline = k

    if startline == stopline:
        for i,v in enumerate(mrt[k]):
            ls = []
            if v == start:
                startcount = True
            if v == end:
                ls.append(v)
                startcount = False
            if startcount:
                ls.append(v)
        return ls
    elif startline != stopline:
        for i,v in stlines.items():
            if startline in v and stopline in v:
                interchange = i
        pass