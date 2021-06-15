import pickle

def read_stations(f):
    dic = {}
    x = []
    while True:
        theline = f.readline()
        if len(theline) == 0:
            break
        if '=' in theline:
            x = []
            dic[theline[1:-2]] = x
            continue
            
        while '\n' in theline:
            theline = theline[:-1]    
            
        string = theline.split(', ')

        for i in string:
            if i != '':
                x.append(i)
    return dic
        

def get_stationline(mrt):
    dic = {}
    for (k,v) in mrt.items():
        for i in v:
            dic[i] = dic.get(i,[]).append(k)
    return dic

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