import pickle

def read_stations(f):
    data = f.readlines()
    dic = {}
    names = []
    dataset = []
    for i in range(len(data)):
        new = []
        if i%2 == 0:
            name = data[i][1:(len(data[i]-3)]
            names.append(name)
        else:
            i = i.split()
            new = []
            for j in i:
                if j[-1] == ',':
                    commagone = j[:len(j)]
                else: commagone = j
                new.append(commagone)
        dataset.append(new)
        
    for k in range(len(names)):
        dic[names[k]] = dataset[k]
    
    return dic


def get_station(mrt):
    stations = mrt.values()
    new_dic = {}
    for i in station:
        for j in i:
            new_dic[j] = i]
    
def get_interchange(stationline):
    new_dic = {}
    for i in stationline:
        if len(stationline[i]) > 1:
            new_dic[i] = stationline[i]
    return new_dic


  
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