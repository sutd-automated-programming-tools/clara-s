import pickle

def read_stations(f):
    stations = {}
    lines = []
    stationlist = []
    for i in f:
        for j in i:
            line = False
            for ch in j:
                if ch == "=":
                    line = True
                else:
                    line = False
            if line:
                linename = ""
                for ch in j:
                    if ch == "=":
                        pass
                    else:
                        linename += ch
                lines.append(linename)
            elif j == None:
                pass
            else:
                stationlist.append(j.split(", "))
    for i in range(0, len(lines)):
        stations[lines[i]] = stationlist[i]
    return stations
            
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