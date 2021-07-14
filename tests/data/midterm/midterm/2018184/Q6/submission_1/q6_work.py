import pickle

def read_stations(f):
    lines = f.readlines()
    station_dict = {}
    train_line = []
    for line in lines:
        formatted_line = line.strip("\n")
        if "=" in formatted_line:
            train_line = formatted_line.strip("=")
        elif formatted_line != "":
            station_dict[train_line] = formatted_line.split(", ")
    return station_dict

#def get_stationline(mrt):
#    stationline_dict = {}
#    for value in mrt.values():
#        for station in value:
#            if station not in stationline_dict.keys():
#                stationline_dict[station] = mrt[station]
#    return None

def get_interchange(stationline):
    interchange_dict = {}
    for item in stationline.items():
        if len(item[1]) > 1:
            interchange_dict[item[0]] = item[1]
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
    pass