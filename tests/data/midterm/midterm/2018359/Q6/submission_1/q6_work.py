import pickle

def read_stations(f):
    alltrain=dict()
    lines3=[]
    for lines in f:
        lines2=lines.strip().split(', ')
        lines3.append(lines2)
    for i in lines3:
        if i==['']:
            lines3.remove(i)
    for j in lines3:
        for u in j:
            if u==['']:
                j.pop(j.index(u))
    for i in lines3:
        if '=' in i[0]:
            a=i[0].strip('=')
            u=a
        else:
            alltrain[u]=i
    return alltrain

def get_stationline(mrt):
    traindict=dict()
    for line, stationlist in mrt.items():
        for station in stationlist:
            traindict[station]=traindict.get(station,[])
            traindict[station].append(line)
    return traindict
def get_interchange(stationline):
    interdict=dict()
    for station, linelist in stationline.items():
        if len(linelist)>1:
            interdict[station]=linelist
    return interdict


  
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
    for lines, trains in mrt_d.items():
        if start and end in trains:
            return abs(trains.index(end)-trains.index(start))
    for lines, trains in mrt_d.items():
        if start in trains:
            lstarttran=lines
        if end in trains:
            endtran=lines
    for lines2 in  :
                pass
            else:
                return None