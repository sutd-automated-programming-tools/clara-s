import pickle

def read_stations(f):
    mrtMap = {}
    mrt = []
    for i in f:
        mrt = []
        if len (i.strip().split('=')) == 3:
            x = i.strip().split('=')
            mrtMap[x[1]] = mrt
        if len(i.strip().split(', ')) >= 3:
            mrt = (i.strip().split(', '))
            mrtMap[x[1]] = mrt
         
    return mrtMap
        

def get_stationline(mrt):
    mydict={}
    for k,v in mrt.items():
        for i in range(len(v)):
            if len(mydict[v[i]]) == 1:
                mydict[v[i]] += [k]
            else:
                mydict[v[i]] = [k]

    return(mydict)

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