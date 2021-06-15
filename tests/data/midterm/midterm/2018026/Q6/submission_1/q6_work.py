import pickle

def read_stations(f):
    mrtdict={}
    for i in f:
        i=i.strip('\n')
        i=i.strip('=')
        i=i.split(',')
        if len(i)==1:
            mrtdict[i[0]]=None
            currentline=i[0]
            continue
        mrtdict[currentline]=i
    del mrtdict['']
        

    return(mrtdict)


def get_stationline(mrt):
    newdict={}
    for line,stationlist in mrt.items():
        for stations in stationlist:
            newdict[stations]=[]
         
        for station in stationlist:
            newdict[station]=newdict[station].append(line)
    return newdict


  
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