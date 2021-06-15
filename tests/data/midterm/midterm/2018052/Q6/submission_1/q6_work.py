import pickle

def read_stations(f):
    data=f.read().split()
    dictionary = {}
    
    for i in range(int((len(data)/2))):
        i *= 2 #this is kinda splitting each of the elements into group of 2s
        dictionary[data[i]] = (data[i+1])
    return dictionary
        

def get_stationline(mrt):
    dic={}
    lystofmrt= list(mrt.values())
    for i in range(len(lystofmrt))
        if lystofmrt[i] in mrt.values()
            dic[lystofmrt[i]]=mrt.key()
    return dic
    
def reverse_lookup(d, v): #d is the dictionary, v is the value
	for k in d:
		if d[k]==v:
			return k 
        
def get_interchange(stationline):
    interchangedic={}
    for i in range (stationline)):
        if len (stationline.values()>1:
            interchangedic[stationline.key()]=stationline.values()
    return interchangedic
    
    


  
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