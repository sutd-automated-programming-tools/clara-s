import pickle

def read_stations(f):
    dic={}
    ls=f.readlines()

    for i in ls:
        x=i.strip()
        n=x.split(", ")
        for o in n:
            if "=" in o:
                s=o.strip("=")
                dic[s]=[]
                y=dic[s]
            else:
                y.append(o)
    return dic

def get_stationline(mrt):
    dic={}
    for i in mrt:
        for o in mrt[i]:
            if o not in dic:
                dic[o]=[i]
            else:
                dic[o].append(i)
    return dic

def get_interchange(stationline):
    dic={}
    for i in stationline:
        if len(stationline[i])>1:           
            dic[i]=stationline[i]    
    return dic


  
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
    
    mrt_lines=read_stations(f)
    line_change=[]
    for i in mrt_lines:
        if start in mrt_lines[i] and end in mrt_lines[i]:
            return mrt_lines[i][mrt_lines[i].index(start):mrt_lines[i].index(end)]
        elif start in mrt_lines[i] or end in mrt_lines[i]:
            line_change.append(i)
        else:
            pass
        
    stations=get_stationline(mrt_lines)
    route=[]
    for i in stations:
        if all(o for o in line_change in stations[i]):
            route.extend()#add sublist of values corresponding to the mrt line to the list route, would have been done via indexing the values of the corresponding keys in dictionart mrt_lines