import pickle

def read_stations(f):
    dict={}
    a=f.read()
    a=a.split('\n')
    ew=a[1].split(', ')
    cg=a[4].split(', ')
    ns=a[7].split(', ')
    dict.update({'EastWestLine (EW)':ew,'EastWestLine (CG)':cg,'NorthSouthLine':ns})
    return dict

def get_stationline(mrt):
    dict={}
    for x,y in mrt.items():
        for i in len(y):
            dict.update({y[i]:,x})
    return dict
            


def get_interchange(stationline):
    dict={}
    for x,y in stationline.items():
        if len(y)>1:
            dict.update({x:y})
    return dict
    


  
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