import pickle

def read_stations(f):
    lines = f.read().split("\n")
    mydic = {}
    curkey = "EastWestLine (EW)"
    for line in lines:
        if "(EW)" in line:
            curkey = "EastWestLine (EW)"
        elif "(CG)" in line:
            curkey = "EastWestLine (CG)"
        elif "NorthSouthLine" in line:
            curkey = "NorthSouthLine"
        else:
            if curkey == "EastWestLine (EW)":
                ls = line.split(",")
                mydic[curkey] = ls
            elif curkey == "EastWestLine (CG)":
                ls = line.split(",")
                mydic[curkey] = ls
            elif curkey == "NorthSouthLine":
                ls = line.split(",")
                mydic[curkey] = ls 
    return mydic

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