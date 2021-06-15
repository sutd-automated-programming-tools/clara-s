import pickle

def read_stations(f):
    name_station = []
    stations = []
    sub_stations = []
    new_dict = {}
    for line in f:
        line.strip()
        if line[0] == "=":
            name_station.append(line)
            stations.append(sub_stations)
            sub_stations = []
        else:
            new = line.split(",")
            sub_stations.extend(new)
    for i in range(len(name_station)):
        new_dict[name_station[i]] = stations[i]
    return new_dict

def get_stationline(mrt):
    new_dict = {}
    part_of = []
    for item in list(mrt.values()):
        for line in list(mrt.keys()):
            if item in mrt[line]:
                part_of.append(line)
        new_dict[item] = part_of
        part_of = []
    return new_dict

def get_interchange(stationLine):
    interchange = []
    new_dict = {}
    for item in list(stationLine.keys()):
        if len(stationLine[item]) > 1:
            interchange.append(item)
    for item in interchange:
        new_dict[item] = stationLine[item]
    return new_dict
  
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
    
    mrt = read_stations(f) #questiona
    mrt_to_line = get_stationline(mrt) #questionb
    list_interchange = get_interchange(mrt_to_line) #questionc
    for item in list(mrt.keys()):
        if start in mrt[item] and end in mrt[item]:
            pass
        else:
            pass