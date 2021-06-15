import pickle

def read_stations(f):
    outp = {}
    for line in f:
        line_s = line.strip()
        
    
    
    

def get_stationline(mrt):
    dic = {}
    for keys in mrt:
        list1 = mrt[keys]
        leng = len(list1)
        for i in range(leng):
            if list1[i] not in dic:
                dic[list1[i]]=[keys]
            else:
                dic[list1[i]] += [keys]
    return dic

def get_interchange(st):
    outp = {}
    for keys in st:
        a = st[keys]
        leng = len(a)
        if leng > 1:
           oupt[keys] = st[keys]
    
    return outp


  
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