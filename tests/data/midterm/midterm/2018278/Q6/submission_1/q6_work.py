import pickle


def read_stations(f):
    mainew = []
    sideew = []
    nsline = []
    stationsdict = {'EastWestLine (EW)': [],'EastWestLine (CG)':[], 'NorthSouthLine': []}
    content = f.read().strip().splitlines()
    print(content)
    for i in range(1, 34):
        mainew.append(content[i])
    for i in range(36,39):
        sideew.append(content[i])
    for i in range(41, 68):
        nsline.append(content[i])
    stationsdict = {'EastWestLine (EW)': mainew,'EastWestLine (CG)':sideew, 'NorthSouthLine': nsline}
    return stationsdict


def get_stationline(mrt):
    newmrt = {}
    for i in mrt:
        l = mrt[i] 
        for element in l:
            li = []
            li.append(i)
            newmrt[element] = li
    return newmrt


def get_interchange(stationline):
    interchanges = {}
    for key in stationline:
        if len(stationline[key]) >= 2:
            interchanges[key] = stationline[key]
    return interchanges 


  
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
    
    d = read_stations(f)
    for key in d:
        if start in d[key] and end in d[key]:
