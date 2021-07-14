import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    dictionary = read_stations(f)
    get_line1 = dictionary.get('East West Line (CG)')
    get_line2 = dictionary.get('East West Line (EW)')
    get_line3 = dictionary.get('NorthSouthLine')
    lines = ['firstline']
    a = [{mrt:lines}]
    if mrt in get_line1:
        mrt[0]= 'East West Line (CG)'
    if mrt in get_line2:
        lines.append('East West Line (EW)') 
    if mrt in get_line3:
        lines.append('NorthSouthLine')
    return a


def get_interchange(stationline):
    dictstn = get_stationline(mrt)
    interchange 


  
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