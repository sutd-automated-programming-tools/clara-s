import pickle

def read_stations(f):
    mrt_stations = {}
    temp_list = []
    all_lines = f.readlines()
    #print(all_lines)
    for element in all_lines:
        #print(element)
        every_line = element.strip().split(',')
        #print (every_line)
        temp_list.append(every_line)
    mrt_stations['EastWestLine (EW)'] = temp_list[1]
    mrt_stations['EastWestLine (CG)'] = temp_list[4]
    mrt_stations['NorthSouthLine'] = temp_list[7]
    return mrt_stations

def get_stationline(mrt):
    mrtlines = {}
    
    return mrtlines

def get_interchange(stationline):
    interchange = {}
    return interchange


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
    path_lst = []
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    return path_lst