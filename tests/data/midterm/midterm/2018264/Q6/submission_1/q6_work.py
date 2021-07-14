import pickle

def read_stations(f):
    mrtstationlist={}
    mrtlist=[]
    for line in f:
        line=line.strip()
        if line == '=EastWestLine (EW)=':
            mrtstationlist['EastWestLine (EW)']=0
        elif line== '=EastWestLine (CG)=':
            mrtstationlist['EastWestLine (CG)']=0
        elif line== '=NorthSouthLine (NS)=':
            mrtstationlist['NorthSouthLine (NS)']=0
        else:
            line=line.strip(',')
            mrtlist.append(line)
            if line=='Tuas Link':
                mrtstationlist['EastWestLine (EW)']=mrtlist
                mrtlist=[]
            if line=='Changi Airport':
                mrtstationlist['EastWestLine (CG)']=mrtlist
                mrtlist=[]
            if line== 'Marina Bay':
                mrtstationlist['NorthSouthLine (NS)']=mrtlist
                mrtlist=[]
    return mrtstationlist


def get_stationline(mrt):
    whatline={}
    for line in mrt:
        for station in line:
            if station not in whatline:
                whatline[station]=[line]
            else:
                whatline[station]+=line
    return whatline

def get_interchange(stationline):
    interchange={}
    for station in stationline:
        if station.count>1:
            interchange[station]=stationline[station]
    return interchange


  
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