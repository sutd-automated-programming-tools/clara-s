import pickle

def read_stations(f):
    dicty = {}
    readfile = f.readlines()
    greenlinevalues = []
    redlinevalues = []
    lines1 = readfile[1].strip()
    greenlinevalues.append(lines1)
    lines2 = readfile[7].strip()
    redlinevalues.append(lines2)
    lines3 = readfile[4].strip()
    line3 = readfile[0].strip("=")
    line3 = line3.strip("=\n")
    line4 = readfile[6].strip("=")
    line4 = line4.strip("=\n")
    line5 = readfile[3].strip("=")
    line5 = line5.strip("=\n")
    dicty[line3] = lines1.split(",")
    dicty[line5] = lines3.split(",")
    dicty[line4] = lines2.split(",")
    return dicty

def get_stationline(mrt):
    dicty2 ={}
    mrt_stations = read_stations(mrt)
    for i in mrt_stations.get("EastWestLine (EW)"):
        dicty2[mrt_stations[i]] = ["EastWestLine (EW)"]
    for j in mrt_stations.get("NorthSouthLine"):
        dicty2[mrt_stations[i]] = ["NorthSouthLine"]
    dicty2["Tanah Merah"] = ["EastWestLine (EW)","EastWestLine (CG)"]
    dicty2["City Hall"] = ["EastWestLine (EW)","NorthSouthLine"]
    dicty2["Raffles Place"] = ["EastWestLine (EW)","NorthSouthLine"]
    dicty2["Jurong East"] = ["EastWestLine (EW)","NorthSouthLine"]
    return dicty2

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