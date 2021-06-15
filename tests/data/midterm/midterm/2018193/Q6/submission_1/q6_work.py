import pickle

def read_stations(f):
    d = {}
    for line in f.readlines():
        line = line.strip()
        if line == "=EastWestLine (EW)=":
            d['EastWestLine (EW)']=[]
        d['EastWestLine (EW)'].append(line.split(","))
        if line == "=EastWestLine (CG)=":
            d['EastWestLine (CG)']=[]
        d['EastWestLine (CG)'].append(line.split(","))
        if line == '=NorthSouthLine=':
            d['NorthSouthLine']= []
        d['NorthSouthLine'].append(line.split(","))
    return d

def get_stationline(mrt):
    d={}
    for value in mrt.values():
        if str(value) not in d:
            d[str(value)]=[]
        for key in mrt.keys():
            for value in mrt[key]:
                if value in d:
                    d[value].append(key)
    return d
    

def get_interchange(stationline):
    d={}
    for key in stationline.keys():
        if len(stationline[key])>1:
            d[key]=stationline[key]
    return d
            

  
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
    mrt = read_stations(f)
    stationline = get_stationline(mrt)
    interchange = get_interchange(stationline)
    for key in stationline.keys():
        if start in stationline[key] and end in stationline[key]:
            for i in range(len(stationline[key])):
                if stationline[key][i]==start:
                    a = int(i)
                if stationline[key][i]==end:
                    b = int(i)
            return stationline[key][a:b]
    if start in stationline['NorthSouthLine'] and start in stationline['EastWestLine (CG)']:
        return None
    if start in stationline['EastWestLine (CG)'] and end in stationline['EastWestLine (EW)']:
            a = stationline['EastWestLine (CG)'].index(start)
            b = stationline['EastWestLine (EW)'].index(end)
            l=[]
            if a>3:
                l.extend(stationline['EastWestLine (EW)'][a-len(stationline['EastWestLine (EW)']):3-len(stationline['EastWestLine (EW)'])])
                l.extend(stationline['EastWestLine (CG)'][0:b])
            else:
                l.extend(stationline['EastWestLine (EW)'][a:3])
                l.extend(stationline['EastWestLine (CG)'][0:b])
            return (l)
    if end in stationline['EastWestLine (CG)'] and start in stationline['EastWestLine (EW)']:
        if start in stationline['EastWestLine (CG)'] and end in stationline['EastWestLine (EW)']:
            a = stationline['EastWestLine (EW)'].index(start)
            b = stationline['EastWestLine (CG)'].index(end)
            l=[]
            if a>3:
                l.extend(stationline['EastWestLine (EW)'][a-len(stationline['EastWestLine (EW)']):3-len(stationline['EastWestLine (EW)'])])
                l.extend(stationline['EastWestLine (CG)'][0:b])
            else:
                l.extend(stationline['EastWestLine (EW)'][a:3])
                l.extend(stationline['EastWestLine (CG)'][0:b])
            return (l)
    