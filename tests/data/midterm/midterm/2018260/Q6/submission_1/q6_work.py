import pickle

def read_stations(f):
    dct = {}
    current_mrt = ''
    for lines in f:
        formatted_line = lines.strip().strip('=')
        if '(' in formatted_line:
            current_mrt = formatted_line
            dct[current_mrt] = []
        elif ', ' in formatted_line:
            dct[current_mrt] = formatted_line.split(', ')
    return dct


def get_stationline(mrt):
    dct = {}
    for key, value in mrt.items():
        for station in value:
            dct[station] = list()

    for keys,values in mrt.items():
        for _station in values:
            dct[_station].append(keys)

    return dct

def get_interchange(stationline):
    dct = {}
    for key, value in stationline.items():
        if len(value) != 1:
            dct[key] = value
    return dct


  
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
    lst = list()
    interchange = get_interchange(stationline).keys()
    for k,v in f.items():
        for stations in v:
            if stations == start:
                
                
    return lst