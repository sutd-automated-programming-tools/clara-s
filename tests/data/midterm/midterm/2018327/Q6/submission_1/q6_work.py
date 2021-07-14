import pickle

def read_stations(f):
    raw_list=f.readlines()
    station_dict={}
    for i in range(len(raw_list),2):
        station_dict.update({raw_list[i].strip('=')},{raw_list[i+1].split(',').strip()})
    return station_dict
    pass

def get_stationline(mrt):
    line_dict={}
    for i in mrt.values():
        for j in i:
            line_dict.setdefault(j,[])
        for k in line_dict:
            if k in j and j not in line_dict[k]:
                line_dict[k].append(j)
    return line_dict
    pass

def get_interchange(stationline):
    interchange_dict={}
    for station in stationline:
        if len(stationline[station])>1:
            interchange_dict.setdefault(station,stationline[station])
    return interchange_dict
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
    lineline=read_stations(f)
    stationline=get_station_line(lineline)
    interchanges=get_interchange(stationline)
    for i in stationline[start]:
        if i in stationline[end]:
            return lineline[lineline.index(start):lineline.index(end)]
    pass