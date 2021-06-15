import pickle

def read_stations(f):
    adic={}
    lines=f.readline()
    print(lines)
    while lines:
        if lines=='\n':
            pass
        elif lines[0].isalpha()==False:
            erm=lines.strip()
            a=erm.strip('=')
            adic[a]=[]
        else:
            b=lines.strip().split(',')
            for i in b:
                adic[a].append(i.strip(" "))
        lines=f.readline()
    return adic
    pass

def get_stationline(mrt):
    newdic={}
    for i in mrt.keys():
        for j in range(len(mrt[i])):
            if newdic.get(mrt[i][j])==None:
                newdic[mrt[i][j]]=[i]
            else:
                newdic[mrt[i][j]].append(i)
    return newdic
    pass

def get_interchange(stationline):
    anotherdic={}
    for i in stationline.keys():
        if len(stationline[i])>1:
            anotherdic[i]=stationline[i]
    return anotherdic
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