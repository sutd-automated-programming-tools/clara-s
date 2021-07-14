import pickle

def read_stations(f):
    ls = f.read().strip().split()
    
    d = {}
    ls1 = []
    ls2 = []
    ls4 = []
    for i in ls:
        if i.endswith('Line'):
            ls2.append(i)
            d[i] = []
        else:
            ls2.append(i)
    
    index_2 = 0
    for key in d:
        d[key] = ls2[index_2]
        index_2 += 1
        

    return(d)
            
    
    

def get_stationline(mrt):
    d1 = {}
    ls1 = list(mrt.values())
    ls2 = list(mrt.keys())
    for i in range(len(ls1)):
        for a in range(len(ls1[i])):
            d1.update({ls1[i][a]:[ls2[i]]})
    return d1

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