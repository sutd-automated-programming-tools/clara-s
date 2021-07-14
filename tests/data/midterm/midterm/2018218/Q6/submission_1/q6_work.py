import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    # to get the full list of mrt stations
    stations = []
    new_dictionary = []
    for key in mrt:
        for value in key:
            if value not in stations:
                stations.append(value)
            else:
                pass
    # add the mrt stations into new dictionary         
    new_dictionary.append(stations)
    # add the 'mrt line values' for each station
    for name in stations:
        # to find the line at which the station occurs
        mrt_line = mrt.index(name)
        new_dictionary[name].append(mrt[mrt_line])
    return new_dictionary
    

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