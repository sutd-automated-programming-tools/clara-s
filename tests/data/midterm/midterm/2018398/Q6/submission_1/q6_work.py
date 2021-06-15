import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    lines = mrt.readlines()
    current_station = ""
    station_dict = {}
    for line in lines:
        formatted_line = line.strip()
        if "Line" in formatted_line:
            current_line = formatted_line.split(' ')
            line_list = [int(timing) for timing in schedule_list]
            station_dict[current_station].append(line_list)
        else:
            current_station = formatted_line
            station_dict[current_station] = []
    return station_dict

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