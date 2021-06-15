import pickle

def read_stations(f):
    list_of_stations = f.readlines()
    list_of_stations = [item.strip() for item in list_of_stations]
#    print(list_of_stations)
    dict_of_stations = {}
    #split first then strip
    ew = list_of_stations[1].split(',')
    ewcg = list_of_stations[4].split(',')
    ns = list_of_stations[7].split(',')
    
    ew = [item.strip() for item in ew]
    ewcg = [item.strip() for item in ewcg]
    ns = [item.strip() for item in ns]
    
    dict_of_stations[list_of_stations[0].strip('=')] = ew
    dict_of_stations[list_of_stations[3].strip('=')] = ewcg
    dict_of_stations[list_of_stations[6].strip('=')] = ns
    
#    print(list_of_stations[7])
    return dict_of_stations

def get_stationline(mrt):
    newdict = {}
    for key, values in mrt.items():
        for i in range(len(values)):
            if values[i] in newdict.keys():
                newdict[values[i]] += [key]
            else:
                newdict[values[i]] = [key]
    return newdict

def get_interchange(stationline):
    newdict = {}
    for key, values in stationline.items():
        if len(values) > 1:
            newdict[key] = values
    return newdict


  
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