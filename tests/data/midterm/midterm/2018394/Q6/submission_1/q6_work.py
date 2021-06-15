import pickle

f = open('mrt_lines_short.txt', 'r')
def read_stations(f):
    lines = f.readlines()
    station = ""
    station_dict = {}
    for line in lines:
        formatted_line = line.strip()
        if "Line" in formatted_line:
            line_name = formatted_line
            station_dict[line_name] = []
        elif line_name != "":
            line_list = formatted_line.split('')
            line_list = [str(name) for name in line_list]
            
            station_dict[line_name].append(line_list)
            
    return station_dict

def get_stationline(mrt):
    pass

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