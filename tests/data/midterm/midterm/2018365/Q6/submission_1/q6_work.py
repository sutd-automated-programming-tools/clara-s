import pickle

def read_stations(f):
    EWL={}
    lines=f.readlines()
    lines_n=[line.strip('\n') for line in lines]
    EWL[lines_n[0]]=[] #appends EastWestLine as a key to dict
    for i in lines_n:
        if i == '=EastWestLine (EW)=':
            EWL[i]=[]
        if i!='\n':
            EWL[lines_n[0]].append(i)
        print(i)
    return EWL

def get_stationline(mrt):
    for value in mrt.values:
        STATION_DICT=[]
        STATION_DICT[value]=[] #appends all station as keys to the new dictionary
        if STATION_DICT[value]== # checks for station corresponding to particular keys of the old dictionary
                                 # if it does, append key of old dictionary as value to STATION_DICT with respective stations as keys

def get_interchange(stationline):
   let me  pass pls


  
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