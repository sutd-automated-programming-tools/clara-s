import pickle

def read_stations(f):
    trainlines=f.readlines
    trainlines[0]=trainlines[0].strip("=")
    for i in trainlines[1]:
        a=i.split("\t")
        EWstations=a.strip()
    for i in trainlines[3]:
        a=i.split("\t")
        CGstations=i.strip()
    for i in trainlines[1]:
    
    NSstations=[(trainlines[1].split("\t")).strip()]
    D[trainlines[0]]=EWstations
    D[trainlines[2]]=CGstations
    D[trainlines[3]]=NSstations
    return D
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