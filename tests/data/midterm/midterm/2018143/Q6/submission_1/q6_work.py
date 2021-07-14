import pickle

def read_stations(f):
        mrt_map = {}
    for line in f:
        line = line.strip()
        line = line.split()
    print(line)
    print(mrt_map)

def get_stationline(mrt):
    lines = {}
    ewl = []
    nsl = []
    for i in range(len(mrt["EastWestLine (EW)"])):
        if mrt["EastWestLine (EW)"][i] not in lines:
            ewl.append("EastWestLine (EW)")
            lines[mrt["EastWestLine (EW)"][i]] = ewl
            ewl =[]
    for j in range(len(mrt["EastWestLine (CG)"])) :
        if mrt["EastWestLine (CG)"][j] not in lines:
            ewl.append("EastWestLine (CG)")
            lines[mrt["EastWestLine (CG)"][j]] = ewl       
            ewl = [] 

    for k in range(len(mrt["NorthSouthLine"])) :
        if mrt["NorthSouthLine"][k] not in lines:
            nsl.append("NorthSouthLine")
            lines[mrt["NorthSouthLine"][k]] = nsl
            nsl = []
   
    return lines

def get_interchange(stationline):
    intchange = {}
    for el in stationline:
        if len(stationline[el])>1:
            intchange[el] = stationline[el]
    return intchange

  
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