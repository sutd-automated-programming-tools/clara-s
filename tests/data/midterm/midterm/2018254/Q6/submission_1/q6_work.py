import pickle

def read_stations(f):
    lineName = ""
    stations = []
    out = {}
    print("**********************")
    for line in f:
        if line[0] == "=":
            lineName = str(line.strip())[1:-1]
            print(lineName)
        elif line[0] == "\n":
            pass
        else:   
            stations = line.split(",")
            for i in range(len(stations)):
                stations[i] = stations[i].strip()
            print(stations)
        out[lineName] = stations
        print (out)
    return out

def get_stationline(mrt):
    out = {}
    for i,k in zip(mrt.values(),mrt.keys()):
        for j in i:
            if j not in out:
                out[j] = []
            out[j].append(k)
    return out

def get_interchange(stationline):
    out = {}
    for i,j in zip(stationline.values(),stationline.keys()):
        if len(i) > 1:
            out[j] = i
    return out

  
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
    for i in mrt_d.values():
        if (start in i) and (end in i):
            return i[i.index(start):i.index(end)]

        