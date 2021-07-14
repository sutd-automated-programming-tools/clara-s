import pickle

def read_stations(f):
    ls = []
    raw = f.read().strip('\n').split('\n')
    for i in raw:
        ls.append(i.split(', '))
    d = {}
    c_int = ''
    
    for i in ls:
        if i[0].endswith('='):
            d[i[0].strip('=')] = None
            c_int = i[0].strip('=')
        elif i[0] == '':
            pass
        else:
            d[c_int] = i
    return(d)
            
            

def get_stationline(mrt):
    d_sta = {}
    for key, value in mrt.items():
        for i in value:
            if i not in d_sta:
                d_sta[i] = []
                d_sta[i].append(key)
            else:
                d_sta[i].append(key)
    return d_sta

def get_interchange(stationline):
    d_int = {}
    for key, value in stationline.items():
        if len(value) > 1:
            d_int[key] = value
        else:
            pass
    return d_int

    


  
##### Testing get_stationlineer =  ###########
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