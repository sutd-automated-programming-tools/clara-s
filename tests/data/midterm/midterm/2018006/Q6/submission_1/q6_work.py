import pickle

def read_stations(f):
    list_files = f.readlines()
#    print(list_files)
    mrt_dict = {}
    line_names = []
    for i in range(0, len(list_files), 2):
        list_files2 = list_files[i].strip('\n')
        line_names.append(list_files2.strip('='))
    for i in range(1, len(list_files), 2):
        station_names = []
        list_files2 = list_files[i].strip('\n').split(',')
        station_names.append(list_files2)
        print(station_names)
        mrt_dict[line_names[i]] = station_names
#    print(list_files)
    return mrt_dict

def get_stationline(mrt):
    dict_station = {}
    for key,value in mrt:
        for i in range(len(value)):   
            if value[i] not in dict_station:
                dict_station[value[i]] = key
            else:
                dict_station[value[i]] += key
    return dict_station

def get_interchange(stationline):
    interchange_dict = {}
    for key, value in mrt:
        if len(value) > 1:
            interchange_dict[key] = value
    return interchange_dict


  
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
    mrt_d = read_station(f)
    lines = get_stationline(mrt_d)
    interchange = get_interchange(mrt_d)
    start_line = get_stationline(start)
    end_line = get_stationline(end)
#    if any start_line == any end_line:
    return start